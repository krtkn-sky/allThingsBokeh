from bokeh.plotting import figure
from bokeh.io import output_file, show

# Code to generate triangle-based plot

x = [2,8,4,3,7,1,9]
y = [1,6,3,8,2,5,6]

output_file("triangle-plots.html")

f0 = figure()
f0.triangle(x,y)
show(f0)

# Code to generate circle-based plot

x = [1,9,4,5,6]
y = [2,5,3,7,8]

output_file("circle-plots.html")

f1 = figure()
f1.circle(x,y)
show(f1)
