import numpy as np

from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file


x = [70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
y = [0, 0, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
y2 = [0, 0, 0, 0, 0, 0, -10, -20, -30, -40, -50, -60, -70]
y3 = []
print (len(x))
for i in range(len(x)):
    print (i)
    y4 = y[i]+y2[i]
    y3.append(y4)

#TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Payoff")

p1.circle(x,   y, legend="Buy option")
p1.circle(x, y2, legend="Sell option", color="orange")
p1.line(x, y3, legend="Total", color="green")

output_file("legend.html", title="legend.py example")

show(gridplot(p1,ncols=1, plot_width=800, plot_height=600))  # open a browser