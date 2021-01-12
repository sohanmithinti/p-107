import pandas as pd 
import plotly.express as px

dataFrame2 = pd.read_csv("data.csv")
bargraph = px.bar(dataFrame2, x = "Country", y = "InternetUsers", color = "Country", title = "Internet Users")
bargraph.show()