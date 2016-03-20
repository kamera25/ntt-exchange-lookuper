import os
import requests
import value
import pandas

class Create_DB:

    prefecture = ["tokyo", "kanagawa", "chiba", "saitama", "ibaraki", "tochigi", "gunma", "yamanashi",\
    "nagano", "niigata", "miyagi", "fukushima", "iwate", "aomori", "yamagata", "akita", "hokkaido"]

    df = pandas.DataFrame()
    isLoad = False

    def downloadData(self, path, url):
        
        print("Start download :" + url)
        
        # ファイルのダウンロード
        r = requests.get(url)
        data = r.content
        
        # ファイルの保存
        f = open(path, 'wb')
        f.write(data)
        f.close()
        
        print("Finish download :" + url)
        

    def downloadNTTEOData(self):
        
        tmpdir = "tmp"
        if( os.path.exists(tmpdir) != True):
            os.mkdir(tmpdir)
        
        # NTT交換局データの一括ダウンロードを行う
        for pre in self.prefecture:
            
            # ヘッダーを読み込む
            url = 'https://www.ntt-east.co.jp/info-st/info_dsl/area-' + pre + '.xls'
            res = requests.head(url)
            size = int(res.headers["content-length"])
            
            # データをダウンロードすべきかチェックする
            xlsfile = tmpdir + "/" + pre + ".xls"
            if( os.path.exists(xlsfile) == True):
                if( os.path.getsize( xlsfile) != size):
                    self.downloadData( xlsfile, url)
                else:
                    print("Not modified : " + url)
            else:
                self.downloadData(xlsfile,url)
        
        
    def BuildDB( self):
        
        isLoad = True
        
        
        # 全てのデータを結合して読みます
        for pre in self.prefecture:     
            path = "./tmp/" + pre + ".xls"
            
            xls = pandas.ExcelFile( path, encoding="SHIFT-JIS")
            loaddf = xls.parse( xls.sheet_names[0], header=1, skip_footer=9)
            loaddf.columns = [ 'Prefecture', 'Address1', 'Address2', 'Address3', 'ExchangeBill', "Notes"]

            self.df = pandas.concat([ self.df, loaddf])
            
        print( "Load data from xls, successful.")
        
        
    def dbData( self):
        
        if( self.isLoad == False):
            self.BuildDB()
        return self.df
        