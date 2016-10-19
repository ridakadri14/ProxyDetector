# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:15:13 2016

@author: admin
"""
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '9ae736cb9dbd45f6a04d4d3928faec2e',
}

params = urllib.parse.urlencode({
})
try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/spid/v1.0/verificationProfiles?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
json_data = json.loads(data)
print (json_data)