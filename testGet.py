import httplib
import urllib

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

#CONNECTION1
httpServ = httplib.HTTPConnection("127.0.0.1", 5000)

#CONNECTION2
#httpServ = httplib.HTTPConnection("www.python.org", 80)
#httpServ.connect()



#GET1
#httpServ.request('GET', "/")
#response = httpServ.getresponse()
#printText(response.read())

#GET2
#httpServ.request('GET', "/story/18237")
#response = httpServ.getresponse()
#printText(response.read())

#GET3
#httpServ.request('GET', "/story/18237/apple/2323")
#response = httpServ.getresponse()
#printText(response.read())

id = "YOLOSWAG5"
name = "jonnyboy1"
#GET3
params = urllib.urlencode({"phoneID" : id, "name" : name})
httpServ.request("GET", "/newUser?%s" % params)
response = httpServ.getresponse()
printText(response.read())

params = urllib.urlencode({"phoneID" : id, "token" : "YOLOSWAG_" + id, "latitude" : 123.323, "longitude" : 121.323})
httpServ.request("GET", "/updateUser?%s" % params)
response = httpServ.getresponse()
printText(response.read())

httpServ.close()

#if response.status == httplib.OK:
#print "Output from HTML request"
#printText (response.read())

#httpServ.request('GET', '/cgi_form.cgi?name=Brad&quote=Testing.')

#response = httpServ.getresponse()
#if response.status == httplib.OK:
#print "Output from CGI request"
#printText (response.read())
