from data import dataset
from task1 import *

import plotly
import plotly.graph_objs as go


#Вивести стовпчикову діаграму: хто скільки вмінь має.

data = dict()
for student in list(dataset.keys()):
    for company, company_list in (dataset[student]).items():
        if student in data:
            data[student] += len(company_list)
        else:
            data[student] = len(company_list)

print(data)

diagram = go.Bar(x=list(data.keys()),y=list(data.values()))

fig = go.Figure(data=[diagram])
plotly.offline.plot(fig, filename='Bar.html')
