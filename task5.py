from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: яке вміння, скільки користувачів мають.

data = ?

diagram = go.Pie(lables=dataset.keys(),values=dataset.value())

fig = go.Figure(data=[diagram])

plotly.offline.plot(fig,filename="pie.html")