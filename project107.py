import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/whitehatjr/Data-Analysis-by-visualisation/master/data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()

#size means more the attempt bigger will be the circle
#color also will be set by the average of attempts
fig = px.scatter(mean, x="student_id", y="level", color="attempt", size="attempt")
fig.show()
