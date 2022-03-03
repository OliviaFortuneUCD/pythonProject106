from bokeh.plotting import figure, output_file, show
fig = figure(plot_width = 200, plot_height = 400)
fig.vbar(x = [1,2,3], width = 0.5, bottom = 0, top = [2,4,6], color = "Cyan")
output_file('bar.html')
show(fig)