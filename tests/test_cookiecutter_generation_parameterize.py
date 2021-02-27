#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tests using pytest."""


import pytest

root_dir_files_list = ["Makefile", "README.md", "run.sh"]
bokehserver_app_files_list = [
    "Procfile",
    "theme.yaml",
    "requirements.txt",
]
flask_app_files_list = [
    "flask_app_config.yaml",
    "main.py",
    "requirements.txt",
    "runtime.txt",
]


@pytest.mark.parametrize("project_name", ["myproject"])
@pytest.mark.parametrize("root_dir_files", [root_dir_files_list])
def test_project_generation(bake_custom_project, project_name, root_dir_files):
    """Test generation and rendering of cookiecutter project template."""
    result = bake_custom_project
    assert result.exit_code == 0
    assert result.exception is None
    proj_dir = result.project
    assert proj_dir.basename == project_name
    assert proj_dir.isdir()
    for file in root_dir_files:
        file = proj_dir.join(file)
        assert file.isfile()


@pytest.mark.parametrize("flask_app_files", [flask_app_files_list])
def test_flask_apps_folder_generation(bake_custom_project, flask_app_files):
    """Test generation and rendering of cookiecutter project template."""
    result = bake_custom_project
    proj_dir = result.project
    flask_app_dir = proj_dir.join("myflaskkappe")
    assert flask_app_dir.isdir()
    runtime_txt = flask_app_dir.join("runtime.txt")
    runtime_txt_file_lines = runtime_txt.readlines(cr=False)
    assert "python-3.9.2" in runtime_txt_file_lines[0]
    for file in flask_app_files:
        file = flask_app_dir.join(file)
        assert file.isfile()
    templates_dir = flask_app_dir.join("templates")
    assert templates_dir.isdir()
    assert templates_dir.join("embed.html").isfile()


@pytest.mark.parametrize("bokehserver_app_files", [bokehserver_app_files_list])
def test_bokehserver_apps_folder_generation(
    bake_custom_project, bokehserver_app_files
):
    """Test generation and rendering of cookiecutter project template."""
    result = bake_custom_project
    proj_dir = result.project
    bokehserver_app_dir = proj_dir.join("mybokehserverapp")
    assert bokehserver_app_dir.isdir()
    runtime_txt = bokehserver_app_dir.join("runtime.txt")
    runtime_txt_file_lines = runtime_txt.readlines(cr=False)
    assert "python-3.9.2" in runtime_txt_file_lines[0]
    for file in bokehserver_app_files:
        file = bokehserver_app_dir.join(file)
        assert file.isfile()
    procfile = bokehserver_app_dir.join("Procfile")
    assert procfile.isfile()
    procfile_file_lines = procfile.readlines(cr=False)
    assert "web: bokeh serve" in procfile_file_lines[0]
    bkapps_dir = bokehserver_app_dir.join("bkapps")
    assert bkapps_dir.isdir()
    assert bkapps_dir.join("bk_server_bar.py").isfile()
    assert bkapps_dir.join("bk_server_map.py").isfile()
