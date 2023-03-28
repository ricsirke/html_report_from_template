# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 06:22:26 2023

@author: Bene Ricsi
"""

# TODO: insert js library
# TODO: multiple pages
# TODO: line chart
# TODO: pie chart
# TODO: stack +/- column chart
# TODO: legend on charts
# TODO: tooltip on data points
# TODO: date to filename (input??, output)


import os
import plotly.graph_objs as plotly_go
from jinja2 import Template


TEMPLATES_FOLDERPATH = 'templates'


def read_file_contents(filepath):
    with open(filepath, 'r') as f:
        return f.read()
        
def load_template(template_filename):
    return read_file_contents(os.path.join(TEMPLATES_FOLDERPATH, template_filename))


# Generate data for the bar chart
x_data = ['Apples', 'Oranges', 'Bananas']
y_data = [5, 3, 7]

# Create a Plotly figure and add the trace to it
fig = plotly_go.Figure(data=[plotly_go.Bar(x=x_data, y=y_data)])

# Convert the Plotly figure to an HTML string
plotly_html = fig.to_html(full_html=False)

# Render the template with the Plotly chart embedded in it
index_template = Template(load_template("index_template.html"))

data = {
    'title': 'My Report',
    'heading': 'My Chart',
    'plotly_chart': plotly_html
}

index_html = index_template.render(data)



with open('output/report.html', 'w') as f:
    f.write(index_html)