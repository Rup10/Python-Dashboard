import pandas as pd
import plotly.express as px

long_df = px.data.medals_long()
nations = list(map(str, long_df["nation"].unique()))
# print(data)
class Barclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def method1(self):
        print(f"Hello {self.name}")
        fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
        return fig #fig.show()
