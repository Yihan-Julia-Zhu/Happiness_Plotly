# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:09:12 2020

@author: zhuyi
"""

import pandas as pd
import os
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import numpy as np


os.chdir("C:\\Users\\zhuyi\\Documents\\ANLY503\\Module6\\plotly")
df = pd.read_csv("WorldHappiness_Final.csv")
print(df.head())

#-----------------------------------------------------------------
#def dummy(value):
#        if value >= 6:
#            return "Happy"
#        elif value<4:
#            return "Unhappy"
#        else:
#            return "Normal"


#df['Happy Category'] = df['Happiness Score'].apply(dummy)
#print(df['Happy Category'])
#df.to_csv("WorldHappiness_Final.csv")
#-----------------------------------------------------------------

user = "JuliaZhu"
key = "oyvNw3XLJFosChM6eGIs"
chart_studio.tools.set_credentials_file(username=user, api_key=key)


#stack bar plot
fig1 = px.bar(df, x="Year", y="Happiness Score", color="Happy Category",
              title="World Happiness Scores 2005-2018")
fig1.show()
pio.write_html(fig1, file='stackbar.html', auto_open=True)
#-------------------------------------------------

#3D
fig2 = px.scatter_3d(df, x="Log GDP per capita", y="Life expectancy",z="Freedom",
                                         opacity=0.5,
                                         color="Happy Category",
                                         title="Impact of GDP, Life Expectancy and Freedom on Happiness")
                        
                   
fig2.show()
pio.write_html(fig2, file='ThreeD.html', auto_open=True)
#--------------------------------------------------   

#facets
fig3 = px.scatter(df, x="Generosity", y="Perceptions of corruption",
                  color="Region", facet_col="Happy Category",
                  size="Happiness Score",
                  hover_name="Happy Category",
                  title="Impact of Generosity and Perceptions of corruption on Happiness")
fig3.show()
pio.write_html(fig3, file='facet.html', auto_open=True)
#--------------------------------------------------

#pie
#Count the frequency
df.groupby("Happy Category").count()
#Create a Donut Chart
labels = ['Happy(Score>=6)','Normal(4<=Score<6)','Unhappy(Score<4)']
values = [527,1001,170]
# Use `hole` to create a donut-like pie chart
fig4 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4)])
fig4.update_layout(title="Happiness Categories")
fig4.show()
pio.write_html(fig4, file='pie.html', auto_open=True)
#--------------------------------------------------

#box
fig5 = px.box(df,x='Region', y='Happiness Score', points="all",
              color="Happy Category",
             notched=True, # used notched shape
             title="Happiness Scores by Regions")
fig5.show()
pio.write_html(fig5, file='box.html', auto_open=True)
#--------------------------------------------------


#slider
df2 =  pd.read_csv("WorldHappiness_small.csv")
print(df2.head())
print(df.dtypes)

TS1=px.scatter(df2, x="Log GDP per capita", y="Life expectancy", 
               animation_frame="Year", 
               animation_group="Country name",
               size="Happiness Score", color="Happy Category", hover_name="Country name",
               size_max=55, range_y=[32,77], range_x=[6,12],
               title="Correlation between GDP and Life expectancy over Time")

pio.write_html(TS1, file='slder.html', auto_open=True)
#--------------------------------------------------

#map_bubble
fig7 = px.scatter_geo(df2, locations="Country name",locationmode='country names', 
                      color="Happy Category",animation_frame="Year",
                     hover_name="Country name", size="Happiness Score",
                     projection="natural earth",
                     title="Evolution of World Happiness")
pio.write_html(fig7, file='map_bubble.html', auto_open=True)
#--------------------------------------------------

#map_polygon
df3=df.query("Year==2018")
data=dict(type='choropleth',
          locations=df3["Country name"],
          locationmode='country names',
          z=df3["Happiness Score"],
          text=df3['Country name'],
          colorscale="Viridis",
          autocolorscale=False,
          colorbar={"title":"Happiness Scores"})
layout=dict(title="Global Happiness Scores in 2018",
            geo=dict(showframe=False,
                     projection={'type':'equirectangular'}))
fig8=go.Figure(data=data,layout=layout)
pio.write_html(fig8, file='map_polygon.html', auto_open=True)
#--------------------------------------------------

#density
fig9 = go.Figure(go.Histogram2dContour(
        x = df['Generosity'],
        y = df['Social support'],
        colorscale = 'Blues'))
fig9.update_layout(title="Relationship between Generosity And Social Support",
                   xaxis_title="Generosity",
                   yaxis_title="Social support",
                   legend_title="Density")
pio.write_html(fig9, file='density.html', auto_open=True)


#sunburst
fig10 = px.sunburst(df3, path=['Region','Happy Category'], values='Happiness Score',
                  color='Happy Category')
fig10.update_layout(title="Distribution of World Happiness")
pio.write_html(fig10, file='sunburst.html', auto_open=True)


#corr matrix
df4=pd.read_csv("WorldHappiness_corr.csv")
corrMatrix = df4.corr()
print (corrMatrix)
df_corr=pd.DataFrame(corrMatrix)

fig11 = px.imshow(df_corr,
                x=['Happiness Score',	'Log GDP per capita',	'Social support',	'Life expectancy',	'Freedom',	'Generosity',	'Perceptions of corruption'],
                y=['Happiness Score',	'Log GDP per capita',	'Social support',	'Life expectancy',	'Freedom',	'Generosity',	'Perceptions of corruption'])
fig11.update_layout(title="Correlation Matrix")
pio.write_html(fig11, file='matrix.html', auto_open=True)








