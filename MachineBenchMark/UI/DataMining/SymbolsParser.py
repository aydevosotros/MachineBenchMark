'''
Created on Dec 22, 2013

@author: antonio
'''

import json
import urllib
import re

def getSymbols(query):
    url = 'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query='+query+'&callback=YAHOO.Finance.SymbolSuggest.ssCallback'
    json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
    data = urllib.urlopen(url)
    data = json.loads(data.read().split('(')[1].split(')')[0])
#     print(data)
#     for k,v in data.iteritems():
#         for element in v['Result']:
#             print(element['name'])
    return data['ResultSet']['Result']