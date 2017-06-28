
# coding: utf-8

# ###### Get information about location using ncdc dataset

# In[1]:

import requests, json
ACCESS_TOKEN = 'devmGBigHBrnpTdPSCKggBbwNwTeiItx' #Access token to request data from NCDC API
def ncdc_getdata():
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/FIPS:37'
    results = requests.get(url, headers={'token': ACCESS_TOKEN})
    return results.json()
data = ncdc_getdata()
data


# ###### Get current temperature of a city using Wunderground API

# In[22]:

import urllib.request #import extensible library for opening URL

f = urllib.request.urlopen('http://api.wunderground.com/api/a13e2cb8b6838af0/geolookup/conditions/q/MA/Boston.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print ("Current temperature in %s is: %s" % (location, temp_f))
f.close()


# ###### Get today's forecast in Fahrenheit of a city using Wunderground API

# In[3]:

import urllib.request, json

f = urllib.request.urlopen('http://api.wunderground.com/api/a13e2cb8b6838af0/forecast/q/MA/Boston.json')
json_string = f.read()                         # Read JSON data
parsed_json = json.loads(json_string)
time = parsed_json['forecast']['txt_forecast']
for each in time['forecastday']:
    print(each['title']  +': '+ each['fcttext'])
f.close()


# ###### Get information about WTI Crude Oil Price using Quandl dataset

# In[23]:

import quandl
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = "USZdexsqJv1bxsSZrnsx"
data = quandl.get("EIA/PET_RWTC_D", start_date="2017-01-01", end_date="2017-01-10", returns="numpy")   #Filter data using date range 
df=pd.DataFrame(data, columns = ['Date', 'Value'])
print(df)
plt.plot(df.Value)
plt.show()


# ###### Get Open and Previous Closing Price of a Stock using yahoo_finance python Package

# In[24]:

from yahoo_finance import Share

yahoo = Share('YHOO') #Use stock code to get data
print(yahoo.get_open())
print(yahoo.get_prev_close())


# ###### Using information using Python API for FRED (Federal Reserve Economic Data)

# In[19]:

from Fred import Fred

fr = Fred(api_key='fb0432249a13111c11d8c2157b3001e3',response_type='dict')
params = {
         'limit':2,
         'tag_names':'trade;goods'
         }
res = fr.category.series(125,params=params)

for record in res:
    print(record)


# ###### Get Minimum and Maximum temperature in celcius of Next days 3 and plot group bar chart

# In[25]:

import urllib.request, json
import plotly as py
import plotly.graph_objs as go
py.offline.init_notebook_mode() #Run this command at the start of every ipython notebook to use plotly.offline

f = urllib.request.urlopen('http://api.wunderground.com/api/a13e2cb8b6838af0/forecast/q/MA/Boston.json')
json_string = f.read()
parsed_json = json.loads(json_string)
time = parsed_json['forecast']['simpleforecast']['forecastday']
low = []
high= []
day= []
for each in time:
    low.append(each['low']['celsius'])
    high.append(each['high']['celsius'])
    day.append(each['date']['pretty'])

# Plot group bar chart for Miniumn and Maximum temperature against Day
group1 = go.Bar(x =day, y=low, name='Minimum')
group2 = go.Bar(x=day, y=high, name='Maximum')
data = [group1, group2]
layout = go.Layout(barmode='group')

fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig, filename='jupyter/group-bar-chart')
f.close()


# In[ ]:



