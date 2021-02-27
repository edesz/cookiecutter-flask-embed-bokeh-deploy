# Bokeh app embedded in Flask web app, run using Gunicorn, deployed to cloud

## [Table of Contents](#table-of-contents)
-   [About](#about)

-   [Notes](#notes)

-   [Usage](#usage)
    -   [Run apps locally](#run-apps-locally)
    -   [Update existing app](#update-existing-app)
    -   [Delete existing app](#delete-existing-app)

## [About](#about)
This project offres automated deployment of a Flask web application with multiple Bokeh server apps embedded in a single HTML document.

## [Usage](#usage)
### [Run apps locally](#run-apps-locally)
1.  Run Bokeh server locally
    ```bash
    cd {{cookiecutter.project_name}}/{{cookiecutter.bokehserver_app_name}}
    bokeh serve --address="localhost" --port=5006 --allow-websocket-origin=localhost:8000 bkapps/*.py
    ```

    and (in a separate shell) run the Flask web application
    ```bash
    cd {{cookiecutter.project_name}}/{{cookiecutter.flask_app_name}}
    gunicorn -w 1 --bind localhost:8000 main:app
    ```

    The resulting HTML webpage at `localhost:8000` will match the deployed version on the cloud (currently running on Heroku) found at `{{cookiecutter.flask_app_name}}.herokuapp.com`.

### [Update existing app](#update-existing-app)
1.  Make changes to Flask and/or Bokeh server app(s)

2.  Commit changes to `git`
    ```bash
    git add .
    git commit -m "updated apps"
    ```

3.  Deploy changes to pre-existing app running in the cloud (Heroku)
    ```bash
    ./run.sh "update"
    ```

### [Delete existing app](#delete-existing-app)
1.  Export name of an existing app, to be deleted, as environment variable `HD_APP_NAME`
    ```bash
    export HD_APP_NAME={{cookiecutter.bokehserver_app_name}}
    ```

2.  Delete an existing app (Bokeh server app or Flask web application)
    ```bash
    ./run.sh "delete"
    ```
## [Notes](#notes)
1.  Currently, the only cloud provider supported for deployment is Heroku.

2.  In `{{cookiecutter.flask_app_name}}/flask_app_config.yaml`, the names under `standalone_bokeh_apps` will match the standalone bokeh server (Python) script names from `flask-embed-bokeh-deploy/{{cookiecutter.bokehserver_app_name}}/bkapps/*.py`.
