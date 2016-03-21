import geosystem
import create_db 
import pandas


class nttLookup:
    
    lat = 35.668764
    lon = 139.795263
    
    cdb = 0
    geo = 0
    df = 0
    
    # Initialize.
    def __init__(self):
        
        self.cdb = create_db.Create_DB()
        self.geo = geosystem.GeoSystem()

        self.df = self.cdb.dbData()
        print("initialize<br>")


    def searchEO( self, lat, lon):
        
        json = self.geo.reverseGeoCoder( lat, lon)
        
        # Extraction Address.

        addressEle = json["Feature"][0]["Property"]["AddressElement"]
        count = len(addressEle)
        address=count*[0]
        for i in range(0, count):
            address[i] = addressEle[i]["Name"] 
            print(address[i].encode('utf-8'))
    
    
        # Search exchanger office of ntt.
        exOffice = \
        self.df[ self.df['Prefecture'].str.contains(address[0])\
        & self.df['Address1'].str.contains(address[1]) \
        & self.df['Address2'].str.contains(address[2])]

        print( "<br>NTT Exchange Office : ")

        exo = exOffice['ExchangeBill'].values.tolist()
        print ( exo[0].encode('utf-8'))