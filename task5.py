from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести кругову діаграму: яке вміння, скільки користувачів мають.

data = dict()
for student in list(dataset.keys()):
    for company, company_list in (dataset[student]).items():
        if company in data:
            data[company] += len(company_list)
        else:
            data[company] = len(company_list)
print(data)

diagram = go.Pie(labels=list(data.keys()), values=list(data.values()))
fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='Pie.html')
