import plotly.figure_factory as ff 
import csv
import statistics as st 
import random 
import plotly.graph_objects as go 
import pandas as pd


df = pd.read_csv('StudentsPerformance.csv')
mathlist = df['math score'].tolist()

mean = st.mean(mathlist)
print('The mean --->', mean)

median = st.median(mathlist)
print('The median --->', median)

mode = st.mode(mathlist)
print('The mode --->', mode)

stDev = st.stdev(mathlist)
print('The standard deviation --->', stDev )

SD1start = mean - stDev
SD1end = mean + stDev
SD2start = mean - 2*stDev
SD2end = mean + 2*stDev
SD3start = mean - 3*stDev
SD3end = mean + 3*stDev

SD1 = []
SD2 = []
SD3 = []

for i in mathlist:
    if i < SD1end and i > SD1start:
        SD1.append(i)

for i in mathlist:
    if i < SD2end and i > SD2start:
        SD2.append(i)

for i in mathlist:
    if i < SD3end and i > SD3end:
        SD3.append(i)

SD1percentage = (len(SD1)/len(mathlist))*100
SD2percentage = (len(SD2)/len(mathlist))*100
SD3percentage = (len(SD3)/len(mathlist))*100

print('percentage for division 1 --->',SD1percentage)
print('percentage for division 2 --->',SD2percentage)
print('percentage for division 3 --->',SD3percentage)

fig = ff.create_distplot([mathlist], ['Math grades'], show_hist = False)
fig.add_trace(go.Scatter(x = [SD3start, SD3start,], y = [0,0.25], mode = 'lines'))
fig.add_trace(go.Scatter(x = [SD3end, SD3end], y = [0,0.25], mode = 'lines')) 
fig.add_trace(go.Scatter(x = [SD2start, SD2start], y = [0,0.25], mode = 'lines'))
fig.add_trace(go.Scatter(x = [SD2end, SD2end], y = [0,0.25], mode = 'lines'))
fig.add_trace(go.Scatter(x = [SD3start, SD3start], y = [0,0.25], mode= 'lines'))
fig.add_trace(go.Scatter(x = [SD3end, SD3end], y = [0,0.25], mode = 'lines'))
fig.show()

