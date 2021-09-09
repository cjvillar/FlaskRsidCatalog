#!/bin/bash
echo "starting venv and running hello.py"
. venv/bin/activate
export FLASK_APP=hello.py
export 'PYTHONPATH="${PYTHONPATH}:/Users/chris/flask_project'
flask run