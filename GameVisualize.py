import pandas as pd
import csv
import plotly.graph_objects as gu

dataFrame = pd.read_csv("GameValue.csv")
#print(dataFrame)

values = dataFrame.groupby("level")['attempt'].mean()
print(values)

studentsDataFrame = dataFrame.loc[dataFrame["student_id"] == "TRL_xsl"]
studentValues = studentsDataFrame.groupby("level")['attempt'].mean()
figure = gu.Figure(gu.Bar(x = studentValues, y = ["level 1", "level2", "level 3", "level 4"], orientation = "h"))
figure.show()