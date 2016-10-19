# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:16:26 2016

@author: admin
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '9ae736cb9dbd45f6a04d4d3928faec2e',
}

params = urllib.parse.urlencode({
})

ids={1 : '5982f24d-ce5c-4c92-a9e5-ba391cd4a5de',2:'b8490458-4db4-459e-9277-bf1e3390c059'}

for i in range(1,len(ids)+1):
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        body=open('F:\\rida4.wav','rb')
        conn.request("POST", "/spid/v1.0/verify?verificationProfileId=%s&%s" % (ids[i],params),body.read(), headers)
        response = conn.getresponse()
        data = response.read()
        print(ids[i])
        print(data)
        conn.close()
        a=data.decode("utf-8")
        if "Accept" in a:
            text_file=open("F:\\output.txt","a")
            text_file.writelines(ids[i]+" : Present \n")
            continue
        else:
            text_file=open("F:\\output.txt","a")
            text_file.writelines(ids[i]+" : Absent \n")
            for j in range(1,len(ids)+1):
                if j!=i:
                    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
                    body=open('F:\\rida1.wav','rb')
                    conn.request("POST", "/spid/v1.0/verify?verificationProfileId=%s&%s" % (ids[j],params),body.read(), headers)
                    response = conn.getresponse()
                    data = response.read()
                    print ("the culprit is :")
                    conn.close()
                    b=data.decode("utf-8")
                    if "Accept" in b:
                        d=True
                    if d==True:
                        print(ids[j])
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
text_file.writelines("\n")

