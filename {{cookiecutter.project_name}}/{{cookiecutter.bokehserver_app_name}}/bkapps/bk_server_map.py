#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Standalone Bokeh server with choropleth map."""


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
# (SINGLE) web: bokeh serve --address="0.0.0.0" --port=${PORT} bkapps/bk_server_map.py --allow-websocket-origin=$FLASK_APP_NAME.herokuapp.com
# (MULTIPLE) web: bokeh serve --address="0.0.0.0" --port=${PORT} --allow-websocket-origin=$FLASK_APP_NAME.herokuapp.com bkapps/*.py


import bokeh.sampledata

bokeh.sampledata.download()

from bokeh.layouts import column
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import curdoc, figure
from bokeh.sampledata.unemployment import data as unemployment
from bokeh.sampledata.us_counties import data as counties
from bokeh.themes import Theme

palette = tuple(reversed(palette))

counties = {
    code: county for code, county in counties.items() if county["state"] == "tx"
}

county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

county_names = [county["name"] for county in counties.values()]
county_rates = [unemployment[county_id] for county_id in counties]
color_mapper = LogColorMapper(palette=palette)

data = dict(
    x=county_xs,
    y=county_ys,
    name=county_names,
    rate=county_rates,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="Texas Unemployment, 2009",
    tools=TOOLS,
    x_axis_location=None,
    y_axis_location=None,
    tooltips=[
        ("Name", "@name"),
        ("Unemployment rate", "@rate%"),
        ("(Long, Lat)", "($x, $y)"),
    ],
)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches(
    "x",
    "y",
    source=data,
    fill_color={"field": "rate", "transform": color_mapper},
    fill_alpha=0.7,
    line_color="white",
    line_width=0.5,
)

curdoc().add_root(column(p))
curdoc().theme = Theme(filename="theme.yaml")
