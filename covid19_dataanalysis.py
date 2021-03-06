# -*- coding: utf-8 -*-
"""Covid19_DataAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ojLUpK7YIwsb_fwobs7AZcC8jZ8w0ie7
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')         #gives grids to graph
# %matplotlib inline

import seaborn
import plotly
import plotly.express as px
import plotly.graph_objects as go
import cufflinks as cf            #uses pandas with plotly and binds them together 
import plotly.offline as pyo 
from plotly.offline import init_notebook_mode, plot, iplot

import folium                     #for maps

pyo.init_notebook_mode(connected=False)
cf.go_offline()

def configure_plotly_browser_state():
  import IPython
  display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-1.5.1.min.js?noext',
            },
          });
        </script>
        '''))

def enable_plotly_in_cell():
  import IPython
  from plotly.offline import init_notebook_mode
  display(IPython.core.display.HTML('''<script 
  src="/static/components/requirejs/require.js"></script>'''))
  init_notebook_mode(connected=False)

df = pd.read_excel("Covid cases in India.xlsx")
df.head()

#we dont need s. no column
df.drop(['S. No.'],axis=1,inplace=True)

df.head()

#total cases of all nationality
df['Total cases'] = df['Total Confirmed cases (Indian National)'] + df['Total Confirmed cases ( Foreign National )']
df.head()

total_cases_overall = df['Total cases'].sum()
print('The total number of cases till now in India is',total_cases_overall)

df['Active cases'] = df['Total cases'] - (df['Death'] + df['Cured'])
df

df.style.background_gradient(cmap = 'Reds')
#shows intensity of cases

Total_Active_Cases = df.groupby('Name of State / UT')['Total cases'].sum().sort_values(ascending = False).to_frame()

Total_Active_Cases

Total_Active_Cases.style.background_gradient(cmap='Reds')

##Graphical Representation

#using pandas
df.plot(kind = 'bar', x = 'Name of State / UT', y = 'Total cases')
plt.show()

df.plot(kind = 'bar', x = 'Name of State / UT', y = 'Death')
plt.show()

#plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
df.iplot(kind = 'bar', x = 'Name of State / UT', y = 'Total cases', xTitle='Total cases', yTitle='States', title = 'Total cases in India')

#pandas
df.plot(kind = 'scatter', x = 'Name of State / UT', y = 'Total cases')

#matplotlib
plt.scatter(df['Name of State / UT'], df['Total cases'])

configure_plotly_browser_state()
enable_plotly_in_cell()
df.iplot(kind='scatter', x = 'Name of State / UT', y = 'Death', mode = 'markers+lines', yTitle='Total Deaths', xTitle='States', title = 'Total Deaths in India', colors='red')
df.iplot(kind='scatter', x = 'Name of State / UT', y = 'Active cases', mode = 'markers+lines', yTitle='Active cases', xTitle='States', title = 'Active cases in India')

ind_co = pd.read_excel('Indian Coordinates.xlsx')
ind_co.head()

ind_co.shape

df_full = pd.merge(ind_co, df, on= 'Name of State / UT')
df_full.head()

map=folium.Map(location=[20,70],zoom_start=4,tiles='Stamenterrain')       #tiles: type of map

for lat,long,value, name in zip(df_full['Latitude'],df_full['Longitude'],df_full['Total cases'],df_full['Name of State / UT']):
    folium.CircleMarker([lat,long],radius=value*0.8,popup=('<strong>State</strong>: '+str(name).capitalize()+'<br>''<strong>Total Cases</strong>: ' + str(value)+ '<br>'),color='red',fill_color='red',fill_opacity=0.3).add_to(map)

map

"""
# How corona virus is rising Globaly"""

data_ind = pd.read_excel("per_day_cases.xlsx", parse_dates=True, sheet_name='India')
data_itl = pd.read_excel("per_day_cases.xlsx", parse_dates=True, sheet_name='Italy')
data_kor = pd.read_excel("per_day_cases.xlsx", parse_dates=True, sheet_name='Korea')
data_wuh = pd.read_excel("per_day_cases.xlsx", parse_dates=True, sheet_name='Wuhan')

data_ind.head()

#plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
data_ind.iplot(kind = 'bar', x = 'Date', y = 'Total Cases', yTitle='Total cases in India', xTitle='Dates', title = 'States')

#using pyplot
fig=plt.figure(figsize=(10,5),dpi=200)
fig=px.bar(data_ind,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(data_ind["Date"],data_ind["Total Cases"],color='green')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()



#plotly Express
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.bar(data_ind,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(data_itl["Date"],data_itl["Total Cases"],color='blue')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Italy")
plt.show()



#plotly Express
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.bar(data_itl,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Italy')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(data_kor["Date"],data_kor["Total Cases"],color='orange')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Korea")
plt.show()



#plotly Express
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.bar(data_kor,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Korea')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.bar(data_wuh["Date"],data_wuh["Total Cases"],color='red')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Wuhan")
plt.show()



#plotly Express
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.bar(data_wuh,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Wuhan')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(data_ind["Date"],data_ind["Total Cases"],color='green')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in India")
plt.show()


#Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
data_ind.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers', xTitle= 'Date', yTitle= 'Total Cases')


#Express Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.scatter(data_ind,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in India')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(data_itl["Date"],data_itl["Total Cases"],color='blue')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Italy")
plt.show()



#Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
data_itl.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers', xTitle= 'Date', yTitle= 'Total Cases')


#Express Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.scatter(data_itl,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Italy')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(data_kor["Date"],data_kor["Total Cases"],color='orange', marker='x')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Korea")
plt.show()



#Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
data_kor.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers', xTitle= 'Date', yTitle= 'Total Cases')



#Express Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.scatter(data_kor,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Korea')
fig.show()

#since pyplot not working....
#Matplotlib
fig=plt.figure(figsize=(10,5),dpi=200)
axes=fig.add_axes([0.1,0.1,0.8,0.8])
axes.scatter(data_wuh["Date"],data_wuh["Total Cases"],color='red')
axes.set_xlabel("Date")
axes.set_ylabel("Total Cases")
axes.set_title("Confirmed cases in Wuhan")
plt.show()


#Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
data_wuh.iplot(kind='scatter',x='Date',y='Total Cases',mode='lines+markers', xTitle= 'Date', yTitle= 'Total Cases')



#Express Plotly
configure_plotly_browser_state()
enable_plotly_in_cell()
fig=px.scatter(data_wuh,x="Date",y="Total Cases",color='Total Cases',title='Confirmed cases in Wuhan')
fig.show()

from plotly.subplots import make_subplots

configure_plotly_browser_state()
enable_plotly_in_cell()
fig=make_subplots(
    rows=2,cols=2,
    specs=[[{"secondary_y":True},{"secondary_y":True}],[{"secondary_y":True},{"secondary_y":True}]],
    subplot_titles=("S.Korea","Italy","India","Wuhan"))

fig.add_trace(go.Bar(x=data_ind['Date'],y=data_ind['Total Cases'],
                    marker=dict(color=data_ind['Total Cases'],coloraxis="coloraxis")),1,1)

fig.add_trace(go.Bar(x=data_itl['Date'],y=data_itl['Total Cases'],
                    marker=dict(color=data_itl['Total Cases'],coloraxis="coloraxis")),1,2)

fig.add_trace(go.Bar(x=data_kor['Date'],y=data_kor['Total Cases'],
                    marker=dict(color=data_kor['Total Cases'],coloraxis="coloraxis")),2,1)

fig.add_trace(go.Bar(x=data_wuh['Date'],y=data_wuh['Total Cases'],
                    marker=dict(color=data_wuh['Total Cases'],coloraxis="coloraxis")),2,2)



fig.update_layout(coloraxis=dict(colorscale='Bluered_r'),showlegend=False,title_text="Total Cases in 4 Countries")

fig.update_layout(plot_bgcolor='rgb(230,230,230)')

configure_plotly_browser_state()
enable_plotly_in_cell()
fig=make_subplots(
    rows=2,cols=2,
    specs=[[{"secondary_y":True},{"secondary_y":True}],[{"secondary_y":True},{"secondary_y":True}]],
    subplot_titles=("S.Korea","Italy","India","Wuhan"))

fig.add_trace(go.Scatter(x=data_ind['Date'],y=data_ind['Total Cases'],
                    marker=dict(color=data_ind['Total Cases'],coloraxis="coloraxis")),1,1)

fig.add_trace(go.Scatter(x=data_itl['Date'],y=data_itl['Total Cases'],
                    marker=dict(color=data_itl['Total Cases'],coloraxis="coloraxis")),1,2)

fig.add_trace(go.Scatter(x=data_kor['Date'],y=data_kor['Total Cases'],
                    marker=dict(color=data_kor['Total Cases'],coloraxis="coloraxis")),2,1)

fig.add_trace(go.Scatter(x=data_wuh['Date'],y=data_wuh['Total Cases'],
                    marker=dict(color=data_wuh['Total Cases'],coloraxis="coloraxis")),2,2)



fig.update_layout(coloraxis=dict(colorscale='Bluered_r'),showlegend=False,title_text="Total Cases in 4 Countries")

fig.update_layout(plot_bgcolor='rgb(230,230,230)')

"""##world Corona Virus"""

df = pd.read_csv('covid_19_data[1].csv', parse_dates=['Last Update'])

df.head()

df.rename(columns={'ObservationDate':'Date', 'Country/Region':'Country'}, inplace = True)
df.head()

df.query('Country == "UK"')

df.groupby('Date').sum()

confirmed=df.groupby('Date').sum()['Confirmed'].reset_index()
death=df.groupby('Date').sum()['Deaths'].reset_index()
rec=df.groupby('Date').sum()['Recovered'].reset_index()

configure_plotly_browser_state()
enable_plotly_in_cell()

fig=go.Figure()
fig.add_trace(go.Scatter(x=confirmed['Date'],y=confirmed['Confirmed'],mode='lines+markers',name='Confirmed',line=dict(color='blue',width=2)))

fig.add_trace(go.Scatter(x=death['Date'],y=death['Deaths'],mode='lines+markers',name='Deaths',line=dict(color='red',width=2)))
fig.add_trace(go.Scatter(x=rec['Date'],y=rec['Recovered'],mode='lines+markers',name='Recovered',line=dict(color='green',width=2)))

df_confirmed = pd.read_csv('time_series_covid_19_confirmed[1].csv')
df_confirmed.head()

df_confirmed.rename(columns={'Country/Region':'Country'},inplace=True)

df_latlong=pd.merge(df,df_confirmed,on=['Country','Province/State'])

df_latlong

configure_plotly_browser_state()
enable_plotly_in_cell()

fig=px.density_mapbox(df_latlong,lat="Lat",lon="Long",hover_name="Province/State",hover_data=["Confirmed","Deaths","Recovered"],animation_frame="Date",color_continuous_scale="Portland",radius=7,zoom=0,height=700)
fig.update_layout(title='Worldwide Corona Virus Cases')
fig.update_layout(mapbox_style="open-street-map",mapbox_center_lon=0)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

