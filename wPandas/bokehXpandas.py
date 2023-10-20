from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas as pd

df = pd.read_csv("sports.csv")
x = df["Year"]
y = df["Handball"]

output_file("sportsResult.html")

f = figure()
f.line(x,y)
show(f)
