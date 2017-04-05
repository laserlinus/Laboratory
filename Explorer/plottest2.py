import numpy as np
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file

x = []
y = []
y2 = []
y3 = []

for i in range(250):
    if i>=120:
        y2.append(-i+120)
        y.append(i-100)
        x.append(i)
        y4 = y[i]+y2[i]
        y3.append(y4)
    elif i>=100:
        y2.append(0)
        y.append(i - 100)
        x.append(i)
        y4 = y[i] + y2[i]
        y3.append(y4)
    else:
        y2.append(0)
        y.append(0)
        x.append(i)
        y4 = y[i] + y2[i]
        y3.append(y4)


#TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

p1 = figure(title="Option value")

p1.circle(x,   y, legend="Buy option (SEK)",color="darkgreen",line_width=1)
p1.circle(x, y2, legend="Sell option (SEK)", color="darkred",line_width=1)
p1.line(x, y3, legend="Total (SEK)", color="cornflowerblue",line_width=5)

output_file("legend.html", title="legend.py example")

p1.ygrid.minor_grid_line_color = 'navy'
p1.ygrid.minor_grid_line_alpha = 0.1
p1.xgrid.minor_grid_line_color = 'navy'
p1.xgrid.minor_grid_line_alpha = 0.1

p1.xaxis.axis_label = "Stock Value"
p1.yaxis.axis_label = "Payoff"

show(gridplot(p1,ncols=1, plot_width=800, plot_height=600))  # open a browser