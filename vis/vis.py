import numpy as np
import pandas as pd

from bokeh.plotting import *
from bokeh.objects import HoverTool
from bokeh.sampledata.unemployment1948 import data
from collections import OrderedDict

import fakedata as fd

#-------------------------------------------------------------------------------
corpus = fd.corpus
texts  = corpus.keys()
color  = '#96fa00'
tools  ="hover"
texts  = [key for key,value in fd.corpus.items()]
#-------------------------------------------------------------------------------

# file to output to
output_file("vis.html")
figure()
#-------------------------------------------------------------------------------
# grid values
x = map(float, sorted(range(1,13)*8))
y = map(float, range(1,9)*12)
w = [0.90]*96
h = [0.90]*96
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
source = ColumnDataSource(
    data=dict(
        id=texts,
    )
)
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
rect(   x,y,w,h,
        source=source,
        tools=tools,
        title=None,
        line_color=None,
        plot_width=200,
        plot_height=200)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# graph options
grid().grid_line_color = None
axis().axis_line_color = None
axis().major_label_text_font_size = "0pt"
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
hover = curplot().select(dict(type=HoverTool))
hover.tooltips = OrderedDict([('id', '@id'),])
#-------------------------------------------------------------------------------

show()
