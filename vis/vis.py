import numpy as np

from bokeh.plotting import *
from bokeh.objects import HoverTool
from collections import OrderedDict

import fakedata as fd

#-------------------------------------------------------------------------------
# globals
corpus = fd.corpus
color  = '#96fa00'
tools  ="hover"
texts  = [key for key,value in corpus.items()]
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# functions for corpus analysis

#-- get_count_for_texts_within
# gets cumulative count of colocations between two classes within a range of [1,within]
# lot     : list of texts to check
# within  : range in [1..50]
# focal   : focal class to check
# compare : comparison class to check against
def get_count_for_texts_within(lot,focal,compare,within):
    text_vals          = [value for key,value in corpus.items() if key in lot]
    unpacked_vals      = [values['focals'][focal][compare].items() for values in text_vals]
    counts             = [value for key,value in unpacked_vals if key == within]
    s = sum(counts)
    return s

#-- get_count_across_corpus
# gets total count for a focal class across a corpus
# focal : the class to get a total occurence count from
def get_count_across_corpus(focal):
    counts = [text['focals'][focal]['num_occurences'] for text in corpus.items()]
    count = sum(counts)
    return count

#-- get_count_for_focal_genre
# returns total count for a class across a full genre set
# focal : class to check
# genre : genre to check
def get_count_for_focal_genre(focal,genre):
    lot  = [text for text in corpus.items() if text['genre'] == genre]
    vals = [counts for counts in text['focals'][focal]['num_occurences']]
    s = sum(vals)
    return s

#-- in_text
# returns whether a focal appears within a text
def in_text(focal,textname):
    count = count_focal_in_text(focal,textname)
    if count > 0:
        return True
    else:
        return False
#-- count_focal_in_text
# returns a count for a class in a particular text
def count_focal_in_text(focal,textname):
    count = corpus[textname]['focals'][focal]['num_occurences']
    return count

#-- normalized_count
# returns count(focal) / length_of_text
def normalized_count(focal,textname):
    count  = count_focal_in_text(focal,textname)
    length = corpus[textname]['length']
    normal = float(count) / float(length)
    return normal

#-- get_colocation_strength_for_text
def get_colocation_strength_for(focal,compare,text):
    txt_compares = corpus[text]['focals'][focal]['compares'][compare]
    counts = [c for c in sorted(txt_compares.items()) if c[0] != 'sentence']
    diffs = []
    for i in range(1,len(counts)):
        diff = counts[i][1] - counts[i-1][1]
        t = (i,diff)
        diffs.append(t)
    strengths = [float(d[1]) / float(d[0]) for d in diffs]
    count_strength = sum(strengths)
    sentence_strenth = float(txt_compares['sentence']['count']) / float(corpus[text]['length'])
    total_strength = count_strength + sentence_strenth
    return total_strength

#-- 

#-------------------------------------------------------------------------------
# file to output to
output_file("vis.html")

# turn on plot ho ld
hold()

# new figure
figure()
#-------------------------------------------------------------------------------
# grid values
x_r = map(str, range(1,13))
y_r = map(str, range(1,9))
x = map(str, sorted(range(1,13)*8))
y = map(str, range(1,9)*12)
w = [0.90]*96
h = [0.90]*96
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
source = ColumnDataSource(
    data=dict(
        x=x,
        y=y,
        id=texts,
    )
)
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# rectangle texts plot options
rect(   'x','y',w,h,
        source=source,
        tools=tools,
        title=None,
        x_range=x_r,
        y_range=y_r,
        line_color=None,
        outline_line_color="white",
        plot_width=200,
        plot_height=200)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# graph options
grid().grid_line_color = None
axis().axis_line_color = None
axis().major_tick_line_color = None
axis().major_label_text_font_size = "0pt"
axis().major_label_standoff = 0
xaxis().major_label_orientation = np.pi/3

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
hover = curplot().select(dict(type=HoverTool))
hover.tooltips = OrderedDict([('id', '@id'),])
#-------------------------------------------------------------------------------

# new figure
figure()

# sample the distribution
mu, sigma = 0, 0.5
measured = np.random.normal(mu, sigma, 1000)
hist = np.histogram(measured, density=True, bins=50)
quad(   top=hist,
        bottom=0,
        left=hist[:-1],
        right=hist[1:],
        fill_color="#036564",
        line_color="#033649",

        # NOTE: these are only needed on the first renderer
        background_fill="#E8DDCB",
        title="Dist",
        tools=""
)
#-------------------------------------------------------------------------------
show()
