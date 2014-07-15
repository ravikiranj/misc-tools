#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import simplejson
from termcolor import colored

# Boston current weather
data = {}
# Boston WOEID = 2367105
# Mountain View WOEID = 12797128
# Palo Alto WOEID = 2467861
city = "Palo Alto"
woeid = "2467861"
data['q'] = "select item.condition.temp,item.condition.text from weather.forecast where woeid=" + woeid
data['format'] = "json"
wQueryParams = urllib.urlencode(data)
baseUrl = "http://query.yahooapis.com/v1/public/yql"
wUrl = baseUrl + '?' + wQueryParams
try:
    #print wUrl
    res = urllib2.urlopen(wUrl).read()
    res = simplejson.loads(res)
    # Check if we have valid results
    if (res and res['query'] and res['query']['results'] and res['query']['results']['channel'] and res['query']['results']['channel']['item'] and res['query']['results']['channel']['item']['condition']):
        res = res['query']['results']['channel']['item']['condition']
        if(res['temp'] and res['text']):
            temp = int(res['temp'])
            temp = (int(temp) - 32) * (5.0/9.0)
            text = res['text']
            print "%s, %d°C, %s" % (city, temp, text)
        else:
           print "Failed to fetch weather data" 
           print "Check http://weather.yahoo.com/ for details"
except urllib2.URLError as e:
    print "Failed to fetch Weather data"
    print "Error Code = %d, Message = %s" % (e.code, e.reason)

# TripAdvisor Inc., Stock Price
data = {}
data['s'] = 'TRIP'
data['format'] = 'bc1p2a'
sQueryParams = urllib.urlencode(data)
baseUrl = 'http://download.finance.yahoo.com/d/quotes.csv'
sUrl = baseUrl + '?' + sQueryParams
try:
    #print sUrl
    res = urllib2.urlopen(sUrl).read()
    if (res != ""):
        splitRes = res.split(",")
        if (len(splitRes) < 3):
            print "Bad data format, check %s for details" % (sUrl)
        else:
            #print splitRes
            price = "$" + splitRes[0]
            changeRaw = float(splitRes[1])
            changePerc = float(splitRes[2].strip('"').rstrip('\%'))
            color = "green"
            arrowStr = ""
            if (changeRaw < 0):
                arrowStr = "↓"
                color = "red"
            elif (changePerc > 0):
                arrowStr = "↑"
            print "TRIP,", price, colored("(%.2f%s" % (changeRaw, arrowStr), color, attrs=['bold']), colored("%.2f%%%s)" % (changePerc, arrowStr), color, attrs=['bold'])

    else:
       print "Failed to fetch stock price data for TRIP" 
       print "Check %s for details" % (sUrl)
except urllib2.URLError as e:
    print "Failed to fetch stock price data for TRIP" 
    print "Error Code = %d, Message = %s" % (e.code, e.reason)
