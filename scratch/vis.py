import numpy as np
import pandas as pd
import fakedata
from bokeh.plotting import *
from bokeh.objects import HoverTool
from bokeh.sampledata.unemployment1948 import data
from collections import OrderedDict

# Read in the data with pandas. Convert the year column to string
columns = [str(x) for x in range(1,13)]
rows = [str(x) for x in range(1,9)]

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

texts = []
for key, value in fakedata.corpus.items():
    texts.append(key)
c_texts = list(chunks(texts,12))

# this is the colormap from the original plot
colors = [
    "#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce",
    "#ddb7b1", "#cc7878", "#933b41", "#550b1d"
]

# Set up the data for plotting. We will need to have values for every
# pair of year/month names. Map the rate to a color.
month = []
year = []
color = []
ids = []
for y in columns:
    for m in rows:
        month.append(m)
        year.append(y)
        color.append(colors[0])
        ids.append(c_texts[int(m) - 1][int(y)- 1])

# EXERCISE: create a `ColumnDataSource` with columns: month, year, color, rate
source = ColumnDataSource(
    data=dict(
        month=month,
        year=year,
        color=color,
        id=ids,
    )
)

output_file('unemployment.html')
figure()

rect('year',
     'month',
     0.99,
     0.99,
     source=source,
     x_axis_location="above",
     x_range=columns,
     y_range=rows,
     color='color',
     line_color=None,
     tools="hover",
     title="Text test",
     plot_width=300,
     plot_height=300)

grid().grid_line_color = None
axis().axis_line_color = None
axis().major_tick_line_color = None
axis().major_label_text_font_size = "5pt"
axis().major_label_standoff = 0
xaxis().major_label_orientation = np.pi/3

# EXERCISE: configure the  hover tool to display the month, year and rate
hover = curplot().select(dict(type=HoverTool))
hover.tooltips = OrderedDict([
    ('id', '@id'),
])

show()      # show the plot
