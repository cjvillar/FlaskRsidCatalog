#!/bin/bash
echo "starting venv and running app.py"
source ./venv/bin/activate
export FLASK_APP=app.py
#add path below :/path/to/FlaskRsidCatalog
export 'PYTHONPATH="${PYTHONPATH}:/Users/chris/flask_project'
flask run