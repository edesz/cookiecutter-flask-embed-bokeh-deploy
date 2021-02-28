#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Execute post- project-generation deployment."""


import shlex
import subprocess


def run_cmd(cmd: str) -> None:
    print(cmd)
    process = subprocess.Popen(
        shlex.split(cmd), shell=False, stdout=subprocess.PIPE
    )
    while True:
        output = process.stdout.readline()
        if process.poll() is not None:
            break
        if output:
            print(str(output.strip(), "utf-8"))
    _ = process.poll()


if __name__ == "__main__":
    initial_commit_msg = "configured apps for initial creation on heroku"
    cmds = [
        "git init",
        "git add .",
        f"git commit -m {initial_commit_msg}",
        "make heroku-create",
    ]
    for cmd in cmds:
        run_cmd(cmd)
