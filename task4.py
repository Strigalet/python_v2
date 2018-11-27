from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки вмінь має.

data = {}
for student in dataset:
    for keys,values in dataset.items():
        if student in data:
            data[student] =l
        else:
            data[student] = len(product_list)

diagram = go.Bar(x=dataset.keys(),y=dataset.values())
fig = go.Figure(data=[diagram])

plotly.offline.plot(fig,filename="bar.html")
