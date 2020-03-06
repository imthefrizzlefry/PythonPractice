import urllib.request
import json
import datetime

def printJsonResults(data):
    theJSON = json.loads(data)

    if 'title' in theJSON['metadata']:
        print(theJSON['metadata']['title'])

    for quake in theJSON['features']:
        print('{0} had a magnitude {1:.2f} earthquake'.format(quake['properties']['place'], quake['properties']['mag']))

def GrabGoogle():
    webUrl = urllib.request.urlopen('http://google.com')
    print('result code: {0}'.format(str(webUrl.getcode())))
    data = webUrl.read()
    print(data)

def getEarthquakeJSON():
    urlData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

    webUrl = urllib.request.urlopen(urlData)
    
    if webUrl.getcode() == 200:
        data = webUrl.read()
        printJsonResults(data)


if __name__ == '__main__':
    getEarthquakeJSON()