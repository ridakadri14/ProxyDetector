# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:18:21 2016

@author: admin
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '9ae736cb9dbd45f6a04d4d3928faec2e',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    body=open('F:\\test.wav','rb')
    conn.request("POST", "/spid/v1.0/verify?verificationProfileId=5982f24d-ce5c-4c92-a9e5-ba391cd4a5de&%s" % params,body.read(), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))