import os
import requests

class Create_DB:

    prefecture = ["tokyo", "kanagawa", "chiba", "saitama", "ibaraki", "tochigi", "gunma", "yamanashi", "nagano", "niigata",\
    "miyagi", "fukushima", "iwate", "aomori", "yamagata", "akita", "hokkaido"]

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
        
            #url = 'https://www.ntt-east.co.jp/info-st/info_dsl/area-' + pre + '.xls'
            #local_filename, headers = urllib.request.urlretrieve(url)
            #html = open(local_filename)
        
        
        
cdb = Create_DB()
cdb.downloadNTTEOData()

