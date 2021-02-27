#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Utility functions for tests."""


import json


def generate_json_and_cfg_contents(json_filename: str):
    """Populate dummy cookiecutter.json using inputs from actual file."""
    with open(json_filename, "r") as f:
        json_data = json.load(f)
    return json_data
