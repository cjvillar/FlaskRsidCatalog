![Pytest CI](https://github.com/cjvillar/flask_template/actions/workflows/ci_tests.yml/badge.svg)
![Manual Lint](https://github.com/cjvillar/flask_template/actions/workflows/main.yml/badge.svg)
![Pylint](https://github.com/cjvillar/flask_template/actions/workflows/pylint.yml/badge.svg)

# Flask Rsid Catalog 
A Flask-based web application focused on retrieving and storing rsID information. (CRUD App)

This app is a WIP currently used for testing. 

## To get started:
1. Clone Repo.
2. Create a Virtual Env:
```bash
   python3 -m venv venv
```
3. Activate:
```bash   
. venv/bin/activate
```
4. Install requirements and run flask:
```bash   
pip install Flask
pip install -r requirements
export FLASK_APP=hello.py
export 'PYTHONPATH="${PYTHONPATH}:/Users/chris/flask_project'
flask Run
```

## When running you should see this:
![alt text](https://github.com/cjvillar/flask_template/blob/master/images/log_in.png "Log In Page")

## After logging in or creating a new user navigate to "LitVar rsID lookup":
![alt text](https://github.com/cjvillar/flask_template/blob/master/images/RSID_PAGE.png "rsID page")


## Run Cypress Test:
1. Complete the steps above. 
2. Run init_db.py *WARNING: this clears the Users db* 
4. In new terminal window, npm run cypress:run



## *Notes*:
If set up, start-up with:
```bash
flask_template: ./start.sh
```

Pip install requirements.txt

## Set up DB:
```python
from hello import db, User, variant
db.create_all()
exit()
```

## Open sqlite3 in terminal:
```bash
sqlite3
.open db.sqlite3
 DROP table user;
 .tables
PRAGMA table_info(table_name);
```
```bash
.schema variant

# need to make table look like this:
CREATE TABLE variant (
        rs_id VARCHAR(20), 
        gene VARCHAR(20), 
        diseases VARCHAR(20), 
        PRIMARY KEY (rs_id)     
);


.quit; to exit sqlite
```
