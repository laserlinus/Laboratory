from bokeh.plotting import figure, output_file, show

# prepare some data
x = [100, 110, 120, 130, 140, 150, 160]
y = [0, 10, 20, 30, 40, 50, 60]
y2 = [0, 0, 0, -10, -20, -30, -40]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example")

# add a line renderer with legend and line thickness
p.multi_line(x, y, y2)

# show the results
show(p)