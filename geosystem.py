import requests
import json
import value

class GeoSystem:
    
    
    def reverseGeoCoder( self, lat, lon):
        
        # 秘匿データの読み込み
        appidY = value.defineVariable()
        
        # Yahooジオコーダにリクエストを送った
        url = 'http://reverse.search.olp.yahooapis.jp/OpenLocalPlatform/V1/reverseGeoCoder?lat=' + str(lat) +'&lon=' + str(lon) + '&output=json&appid=' + appidY
        geoReq = requests.get(url)

        # Json のパース
        ljson = json.loads(geoReq.text)
        
        return ljson