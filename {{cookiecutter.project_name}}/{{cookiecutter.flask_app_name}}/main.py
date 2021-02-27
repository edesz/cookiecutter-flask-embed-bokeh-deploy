#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Flask main script."""


# Run locally
# export HOST=0.0.0.0  # 0.0.0.0 or localhost
# export PORT=8000
# gunicorn -w 1 --bind $HOST:$PORT main:app

# Heroku App name = myflaskapp  # export FLASK_APP_NAME=myflaskapp

# Heroku Procfile
# web: gunicorn -w 1 --bind $HOST:$PORT main:app


import os

import yaml
from bokeh.embed import server_document
from flask import Flask, render_template

PROJ_ROOT_DIR = os.getcwd()
app_config_filepath = os.path.join(PROJ_ROOT_DIR, "flask_app_config.yaml")

with open(app_config_filepath) as f:
    params = yaml.safe_load(os.path.expandvars(f.read()))

deploy = params["deploy"]
deployed_bokeh_server_app_name = params["deployed_bokeh_server_app_name"]
standalone_bokeh_apps = params["standalone_bokeh_apps"]

if deploy:
    # Heroku
    BOKEH_URLS = {
        sname: f"https://{deployed_bokeh_server_app_name}.com/{bokeh_app}"
        for sname, bokeh_app in standalone_bokeh_apps.items()
    }
else:
    BOKEH_URLS = {
        sname: f"http://localhost:5006/{bokeh_app}"
        for sname, bokeh_app in standalone_bokeh_apps.items()
    }

app = Flask(__name__)


@app.route("/", methods=["GET"])
def bkapp_page():
    script = {
        sname: server_document(BOKEH_URL)
        for sname, BOKEH_URL in BOKEH_URLS.items()
    }
    return render_template("embed.html", script=script)
