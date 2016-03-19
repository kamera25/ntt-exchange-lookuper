import urllib.request
import pandas
import xlrd
import json
import value

lat = 35.668764
lon = 139.795263
appidY = value.defineVariable()

xls = pandas.ExcelFile("ntt.xls", encoding="SHIFT-JIS")
df = xls.parse(xls.sheet_names[0], header=1, skip_footer=9)
df.columns = [ 'Prefecture', 'Address1', 'Address2', 'Address3', 'ExchangeBill', "Notes"]

# Reverse Geocoder.
url = 'http://reverse.search.olp.yahooapis.jp/OpenLocalPlatform/V1/reverseGeoCoder?lat=' + str(lat) +'&lon=' + str(lon) + '&output=json&appid=' + appidY
geoReq = urllib.request.urlopen(url)

decode_str = geoReq.read().decode('utf-8')
json = json.loads(decode_str)

# Extraction Address.
address=5*[0]
for i in range(0, 5):
    address[i]=json["Feature"][0]["Property"]["AddressElement"][i]["Name"] 
    
    
# Search exchanger office of ntt.

exOffice = \
df[ df['Prefecture'].str.contains(address[0])\
& df['Address1'].str.contains(address[1]) \
& df['Address2'].str.contains(address[2]) \
& df['Address3'].str.contains(address[3])]

print (exOffice['ExchangeBill'].values)