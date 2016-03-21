#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgitb; cgitb.enable()

import sys
sys.path.append('/home/ubuntu/workspace')
import cgi
import io
import locale
import main
import value

form = cgi.FieldStorage()

f_lon = form.getvalue('lon','')
f_lat = form.getvalue('lat','')

print "Content-type: text/html"
print ""

	    
print """
<html>

<head><title>NTT-East Exchange Office lookup</title></head>

<body>
  <h3>NTT東日本 収容局検索システム</h3>
  
  <form action="./index.py" method="get">
    緯度：<input type="text" name="lat" size="40" placeholder="35.668764"><br>
    経度：<input type="text" name="lon" size="40" placeholder="139.795263"><br>
    <input type="submit" value="送信">
  </form>
"""


if( len(f_lon) == 0 | len(f_lat) == 0):
  sys.exit()

lookup = main.nttLookup()
lookup.searchEO( float(f_lat), float(f_lon))

print """
<div id="map" style="width:400px; height:300px"></div>

<script type="text/javascript" charset="utf-8" src="http://js.api.olp.yahooapis.jp/OpenLocalPlatform/V1/jsapi?appid="""+ value.defineVariable()+"""
"></script>
<script type="text/javascript">
window.onload = function(){
    var ymap = new Y.Map("map");
    ymap.drawMap(new Y.LatLng("""+ f_lat +"," + f_lon + """), 17, Y.LayerSetId.NORMAL);
    
    var control = new Y.CenterMarkControl();
    ymap.addControl(control);
}

</script>

"""

print """
</body>
</html>
"""
