<div align="center">
<h1>Bokeh apps embedded in Flask, via Gunicorn, and deployed to cloud</h1>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-brightgreen.svg"></a>
  <a href="https://github.com/edesz/cookiecutter-flask-embed-bokeh-deploy/pulls"><img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square"></a>
  <a href="https://github.com/edesz/pipenv-tox/actions">
    <img src="https://github.com/edesz/cookiecutter-flask-embed-bokeh-deploy/workflows/CI/badge.svg"/>
  </a>
  <a href="https://github.com/edesz/cookiecutter-flask-embed-bokeh-deploy/actions">
    <img src="https://github.com/edesz/cookiecutter-flask-embed-bokeh-deploy/workflows/CodeQL/badge.svg"/>
  </a>
  <a href="https://en.wikipedia.org/wiki/Open-source_software"><img alt="Open Source?: Yes" src="https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github"></a>
</div>

<div align="center">
<a href="https://www.python.org/">
  <img alt="Made With: Python" src="https://forthebadge.com/images/badges/made-with-python.svg"/>
</a>
</div>

## [Table of Contents](#table-of-contents)
-   [About](#about)

-   [Features](#features)

-   [Notes](#notes)

-   [Usage](#usage)

-   [Tests](#tests)

-   [Links](#links)

-   [Enhancements](#enhancements)

## [About](#about)
This `cookiecutter` is a scripted approach to deploying a single or multiple [Bokeh server](https://docs.bokeh.org/en/latest/docs/user_guide/server.html) app(s), embedded inside a [Flask](https://flask.palletsprojects.com/en/1.1.x/) web application (which is run via the [`gunicorn`](https://gunicorn.org/) [WSGI](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) server), to a cloud-based app-hosting service.

## [Features](#features)
Included

-   click-free app deployment to the cloud

-   allows one or more Bokeh apps to be embedded inside an HTML document via a Flask application

-   code for starter apps to support immediate deployment to the cloud on execution

Not included

-   customized HTML document

-   advanced Bokeh or Flask features, such as interactive charts (Bokeh)

## [Notes](#notes)
1.  Currently, the only cloud provider whose app-hosting service is supported by this project is [Heroku](https://www.heroku.com/what#a-focus-on-apps).

## [Usage](#usage)
1.  Change into the desired local path
    ```bash
    cd ${HOME}/Downloads
    ```

2.  Generate a templated project and deploy it to the cloud as an app (currently, only deployment to Heroku is supported)
    ```bash
    cookiecutter https://github.com/edesz/cookiecutter-flask-embed-bokeh-deploy
    ```

    This will

    -   create a single cloud-based app (currently, on Heroku) where two Bokeh apps, under `{{cookiecutter.bokehserver_app_name}}/bkapps/*.py`, [are run on a single Bokeh server](https://discourse.bokeh.org/t/bokeh-multiple-bokeh-apps-using-one-server/1228)

    -   create a Flask web application (currently, on Heroku) and embed the two deployed Bokeh apps [in the same HTML document](https://discourse.bokeh.org/t/multiple-bokeh-apps-embedded-on-same-webpage-using-flask-with-gunicorn/7253)

    The newly created project will have the following directory structure
    ```
    ├── <project-name>
    │   ├── <bokeh-server-app-name-in-cloud>
    │   │   ├── bkapps
    │   │   │   ├── <first-bokeh-server-app-to-embed-in-flask-web-app>.py
    │   │   │   └── <second-bokeh-server-app-to-embed-in-flask-web-app>.py
    │   │   ├── Procfile
    │   │   ├── requirements.txt
    │   │   ├── runtime.txt
    │   │   └── theme.yaml
    │   ├── <flask-web-app-name-in-cloud>
    │   │   ├── flask_app_config.yaml
    │   │   ├── main.py
    │   │   ├── Procfile
    │   │   ├── requirements.txt
    │   │   ├── runtime.txt
    │   │   └── templates
    │   │       └── embed.html
    │   ├── Makefile
    │   └── README.md
    ```

## [Tests](#tests)
1. Tests can be run from the root of the project using
   ```bash
   make test
   ```

   Note that tests will only confirm that the project is rendered from this template. Tests will **not**

   -   deploy an app to the cloud

   -   test the content of rendered files, but will only test the existence of these files

## [Links](#links)
This project is based on

1.  Bokeh discourse questions

    -   deploying single bokeh server app embedded in gunicorn flask to the cloud
        -   [1](https://discourse.bokeh.org/t/bokeh-server-embedded-in-gunicorn-flask-hosted-to-cloud/6199/19)
        -   [2](https://discourse.bokeh.org/t/bokeh-server-embedded-in-gunicorn-flask-hosted-to-cloud/6199/15)

    -   [deploying multiple Bokeh apps using one server](https://discourse.bokeh.org/t/bokeh-multiple-bokeh-apps-using-one-server/1228)

    -   [adapting Bokeh docs example of embedding Bokeh server inside Flask with `gunicorn`](https://github.com/bokeh/bokeh/blob/main/examples/howto/server_embed/flask_gunicorn_embed.py)

2.  Bokeh docs

    -   [map](https://docs.bokeh.org/en/latest/docs/gallery/texas.html)
    
    -   [bar chart](https://docs.bokeh.org/en/latest/docs/user_guide/categorical.html#basic)

## [Enhancements](#enhancements)
Below is a preliminary list of improvements planned

1.  Support deployment to other cloud providers, such as Azure ([App Service](https://azure.microsoft.com/en-ca/services/app-service/)), DigitalOcean ([App Platform](https://www.digitalocean.com/docs/app-platform/)), [AWS](https://aws.amazon.com/application-hosting/) (eg. [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)), etc.
