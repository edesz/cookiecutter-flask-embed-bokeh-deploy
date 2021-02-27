#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Standalone Bokeh server with bar chart."""


# Run locally
# export HOST=0.0.0.0  # 0.0.0.0 or localhost
# export PORT=8000
# bokeh serve \
#     --address="0.0.0.0" \
#     --port=5006 \
#     --allow-websocket-origin=$HOST:$PORT \
#     *.py

# (SINGLE) Heroku App name = {{cookiecutter.bokehserver_app_name}}  # export BOKEH_SERVER_APP_NAME={{cookiecutter.bokehserver_app_name}}

# Heroku Procfile
# (SINGLE) web: bokeh serve --address="0.0.0.0" --port=${PORT} bkapps/bk_server_bar.py --allow-websocket-origin=${FLASK_APP_NAME}.herokuapp.com
# (MULTIPLE) web: bokeh serve --address="0.0.0.0" --port=${PORT} --allow-websocket-origin=${FLASK_APP_NAME}.herokuapp.com bkapps/*.py


from bokeh.layouts import column
from bokeh.plotting import curdoc, figure
from bokeh.themes import Theme

fruits = ["Apples", "Pears", "Nectarines", "Plums", "Grapes", "Strawberries"]
counts = [5, 3, 4, 2, 4, 6]

p = figure(
    x_range=fruits,
    plot_height=350,
    title="Fruit Counts",
    toolbar_location=None,
    tools="",
)
p.vbar(x=fruits, top=counts, width=0.9)
p.xgrid.grid_line_color = None
p.y_range.start = 0

curdoc().add_root(column(p))
curdoc().theme = Theme(filename="theme.yaml")
