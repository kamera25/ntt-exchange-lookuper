import geosystem
import create_db 
import pandas

lat = 35.668764
lon = 139.795263


cdb = create_db.Create_DB()
geo = geosystem.GeoSystem()

df = cdb.dbData()
json = geo.reverseGeoCoder( lat, lon)


# Extraction Address.
address=5*[0]
for i in range(0, 5):
    address[i]=json["Feature"][0]["Property"]["AddressElement"][i]["Name"] 
    print(address[i])
    
    
# Search exchanger office of ntt.

exOffice = \
df[ df['Prefecture'].str.contains(address[0])\
& df['Address1'].str.contains(address[1]) \
& df['Address2'].str.contains(address[2])]

print (exOffice['ExchangeBill'].values)