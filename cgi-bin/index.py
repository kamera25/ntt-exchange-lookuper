#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/ubuntu/workspace/ntt-exchange-lookuper')
import create_db

print "Content-type: text/html"
print ""

print """
<html>

<head><title>Sample CGI Script</title></head>

<body>
  <h3>NTT東日本 収容局検索システム</h3>
  
  <form action="./index.py" method="get">
    緯度：<input type="text" name="lat" size="40"><br>
    経度：<input type="text" name="lon" size="40"><br>
    <input type="submit" value="送信">
  </form?
  
</body>
</html>
"""