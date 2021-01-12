import pandas as pd 
import plotly.express as px

dataFrame2 = pd.read_csv("coffe.csv")
scattergraph = px.scatter(dataFrame2, x = "Coffee in ml", y = "sleep in hours")
scattergraph.show()