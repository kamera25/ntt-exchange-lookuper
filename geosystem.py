import requests
import json
import value

class GeoSystem:
    
    
    def reverseGeoCoder( self, lat, lon):
        
        # Load Yahoo! secret appid.
        appidY = value.defineVariable()
        
        # Request yahoo! reverse geocoder.
        url = 'http://reverse.search.olp.yahooapis.jp/OpenLocalPlatform/V1/reverseGeoCoder?lat=' + str(lat) +'&lon=' + str(lon) + '&output=json&appid=' + appidY
        geoReq = requests.get(url)

        # Parse json.
        ljson = json.loads(geoReq.text)
        
        return ljson