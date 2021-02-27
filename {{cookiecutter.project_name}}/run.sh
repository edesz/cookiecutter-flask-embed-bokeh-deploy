#!/bin/bash


ACTION=${1:-create}

if [[ "$ACTION" == 'create' ]]; then
    git init
    git add .
    git commit -m "initial commit"
    make heroku-create-bokehserver \
        heroku-create-flask \
        heroku-push-bokehserver \
        heroku-push-flask
elif [[ "$ACTION" == 'update' ]]; then
    make heroku-push-bokehserver heroku-push-flask
elif [[ "$ACTION" == 'delete' ]]; then
    make heroku-stop
fi
