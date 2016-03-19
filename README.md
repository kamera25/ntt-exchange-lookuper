# ntt-exchange-lookuper
## これは何?
緯度経度からNTT収容局を検索するためのスクリプトです。  (NTT東日本限定)

緯度経度情報から住所を割り出し、そこから収容局を特定します。  

住所割り出しは [Yahoo!リバースジオコーダAPI](http://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/reversegeocoder.html)
を使っています(APIの利用には申請が必要です)。  
収容局情報は[収容局毎のカバーエリア - NTT東日本](https://www.ntt-east.co.jp/info-st/info_dsl/area.html)を使っています。

## ライセンス
MITライセンスです。お好きにお使いください。