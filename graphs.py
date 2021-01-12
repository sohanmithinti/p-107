import pandas as pd 
import plotly.express as px

dataFrame2 = pd.read_csv("line_chart.csv")
linegraph = px.line(dataFrame2, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
linegraph.show()
data = [1,2,3,4,5]
dataFrame1 = pd.DataFrame(data)
print(dataFrame1)