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
data['symbol'] = 'TRIP'
sQueryParams = urllib.urlencode(data)
baseUrl = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json'
sUrl = baseUrl + '?' + sQueryParams
try:
    res = urllib2.urlopen(sUrl).read()
    res = simplejson.loads(res)
    if res["Status"] == "SUCCESS":
        price = "$" + str(res["LastPrice"])
        changeRaw = float(res["Change"])
        changePerc = float(res["ChangePercent"])
        color = "green"
        arrowStr = ""
        if (changeRaw < 0):
            arrowStr = "↓"
            color = "red"
        elif (changePerc > 0):
            arrowStr = "↑"
        print "TRIP,", price, colored("(%.2f%s" % (changeRaw, arrowStr), color, attrs=['bold']), colored("%.2f%%%s)" % (changePerc, arrowStr), color, attrs=['bold'])
    else:
        print "Failed to fetch stock price data for TRIP, url = %s" % (sUrl)
except urllib2.URLError as e:
    print "Failed to fetch stock price data for TRIP, url = %s" % (sUrl)
    print "Error Code = %d, Message = %s" % (e.code, e.reason)
