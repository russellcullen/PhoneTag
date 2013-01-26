import httplib
import urllib

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

#CONNECTION1
#httpServ = httplib.HTTPConnection("127.0.0.1", 5000)

#CONNECTION2
#httpServ = httplib.HTTPConnection("http://maps.googleapis.com", 80)
#httpServ.connect()


#origins:
    #origins=Bobcaygeon+ON|41.43206,-81.38992
#destinations:
    #destinations=Darling+Harbour+NSW+Australia|24+Sussex+Drive+Ottawa+ON|Capitola+CA
#sensor: Indicates whether your application is using a sensor (such as a GPS locator) to determine the user's location.
    #sensor=true
    #sensor=false
#-------optional
#mode: driving | walking | bicycling
#language: en-US
#avoid: 
    #avoid=tolls
    #avoid=highways
#units:
    #units=metric
    #units=imperial

import json
import urllib2


dic = {"origins" : "5232 Forbes Avenue Pittsburgh Pennsylvania", 
        "destinations" : "133 North Dithridge Pittsburgh Pennsylvania", 
        "sensor" : "false", 
        "mode" : "walking", 
        "language" : "en-US"}
#print dic
params = urllib.urlencode(dic)
#print "PARAMETERS"
#print params

contactURL = "http://maps.googleapis.com/maps/api/distancematrix/json?" + params
#print contactURL
data = urllib2.urlopen(contactURL)

#print data
j = json.load(data)
elems = j.get("rows")[0].get("elements")[0]
print elems
distance = elems.get("distance")
distText = distance.get("text")
distVal = distance.get("value")
duration = elems.get("duration")
status = elems.get("status")

print distance
print distText
print distVal

#for elem in elems:
#print elem.get(

#print j
#for key, value in j.items():
#    print key, value


#k = [i for i, j, k in j[1]]
#l = json.dumps(k)

#httpServ.request("GET", "/maps/api/distancematrix/json?%s" % params)
#response = httpServ.getresponse()
#printText(response.read())

#params = urllib.urlencode({"name" : "YOLOSWAG1", "ACM" : "10b"})
#httpServ.request("GET", "/updateUser?%s" % params)
#response = httpServ.getresponse()
#printText(response.read())

#httpServ.close()

#if response.status == httplib.OK:
#print "Output from HTML request"
#printText (response.read())

#httpServ.request('GET', '/cgi_form.cgi?name=Brad&quote=Testing.')

#response = httpServ.getresponse()
#if response.status == httplib.OK:
#print "Output from CGI request"
#printText (response.read())
