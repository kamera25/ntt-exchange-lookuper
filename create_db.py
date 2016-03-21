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
        
        # Download file.
        r = requests.get(url)
        data = r.content
        
        # Save file.
        f = open(path, 'wb')
        f.write(data)
        f.close()
        
        print("Finish download :" + url)
        

    def downloadNTTEOData(self):
        
        tmpdir = "tmp"
        if( os.path.exists(tmpdir) != True):
            os.mkdir(tmpdir)
        
        # Download all exchange office data.
        for pre in self.prefecture:
            
            # Read headder.
            url = 'https://www.ntt-east.co.jp/info-st/info_dsl/area-' + pre + '.xls'
            res = requests.head(url)
            size = int(res.headers["content-length"])
            
            # Check data, if is it needed donwload.
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
        
        
        # Join all data. 
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
        