#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json

import pytest

import testing_utils.ccfebd_test_utilities as cu


@pytest.fixture
def custom_template(tmpdir):
    """Generate a template with cookiecutter, in order to run tests."""
    template = tmpdir.ensure("cookiecutter-template", dir=True)
    json_data = cu.generate_json_and_cfg_contents("cookiecutter.json")

    # ========= Populate cookiecutter.json =========
    template.join("cookiecutter.json").write(json.dumps(json_data))

    # ========= Create project folder =========
    repo_dir = template.ensure("{{cookiecutter.project_name}}", dir=True)

    # ========= Prepare individual files in project root dir =========
    repo_dir.join("README.md").write("{{cookiecutter.bokehserver_app_name}}")
    # Ensure files exist, without adding contents
    blank_files = [
        "Makefile",
        "README.md",
        "run.sh",
    ]
    for blank_file in blank_files:
        repo_dir.join(blank_file).ensure(file=True)
    # ========= Prepare files in bokehserver app dir =========
    bokehserver_app_dir = repo_dir.join(
        "{{cookiecutter.bokehserver_app_name}}", dir=True
    )
    bokehserver_app_files_list = [
        "Procfile",
        "theme.yaml",
        "requirements.txt",
    ]
    for bokehserver_app_file in bokehserver_app_files_list:
        bokehserver_app_dir.join(bokehserver_app_file).ensure(file=True)
    bokehserver_app_dir.join("runtime.txt").write(
        "python-{{cookiecutter.python_version}}"
    )
    procfile_text = (
        'web: bokeh serve --address="0.0.0.0" --port=${PORT} bkapps/*.py '
        "--allow-websocket-origin={{cookiecutter.flask_app_name}}."
        "herokuapp.com"
    )
    bokehserver_app_dir.join("Procfile").write(procfile_text)
    bkapps_dir = bokehserver_app_dir.join("bkapps", dir=True)
    for py_file in ["bk_server_bar.py", "bk_server_map.py"]:
        bkapps_dir.join(py_file).ensure(file=True)
    # ========= Prepare files in flask app dir =========
    flask_app_dir = repo_dir.join("{{cookiecutter.flask_app_name}}", dir=True)
    flask_app_files_list = [
        "flask_app_config.yaml",
        "main.py",
        "requirements.txt",
    ]
    for flask_app_file in flask_app_files_list:
        flask_app_dir.join(flask_app_file).ensure(file=True)
    flask_app_dir.join("runtime.txt").write(
        "python-{{cookiecutter.python_version}}"
    )
    templates_dir = flask_app_dir.join("templates", dir=True)
    templates_dir.join("embed.html").ensure(file=True)
    return template


@pytest.fixture
def bake_custom_project(cookies, custom_template):
    """Generate custom cookiecutter project template."""
    result = cookies.bake(template=str(custom_template))
    return result
