import csv 
import plotly.graph_objects as p
import numpy as np
import pandas as pd 

reader = pd.read_csv("data1.csv")

groups = reader.groupby("level")["attempt"].mean()
print(groups)

bargraph = p.Figure(p.Bar(
    x = groups, 
    y = ['level 1', 'level 2', 'level 3', 'level 4'],
    orientation = 'h',
))
bargraph.show()