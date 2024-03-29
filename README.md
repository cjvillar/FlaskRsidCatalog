![Pytest CI](https://github.com/cjvillar/flask_template/actions/workflows/ci_tests.yml/badge.svg)
![Manual Lint](https://github.com/cjvillar/flask_template/actions/workflows/main.yml/badge.svg)
![Pylint](https://github.com/cjvillar/flask_template/actions/workflows/pylint.yml/badge.svg)

# Flask Rsid Catalog 
A Flask-based web application focused on retrieving and storing rsID information. (CRUD App)
This app is a WIP. 

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
pip install -r requirements.txt
export FLASK_APP=app.py
export 'PYTHONPATH="${PYTHONPATH}:/path/to/FlaskRsidCatalog'
flask Run
```

## When running you should see this:
![alt text](https://github.com/cjvillar/flask_template/blob/master/images/log_in.png "Log In Page")

## After logging in or creating a new user navigate to "LitVar rsID lookup":
![alt text](https://github.com/cjvillar/flask_template/blob/master/images/RSID_PAGE.png "rsID page")


## TODO:
- Code:
1. Break up app.py. Example, separate Models from app code.
2. Use secure key.

- Functionality:
1. Add File input for bulk searches.
2. Add Delete feature.
3. Upgrade to Postgres


### Run Cypress Test:
1. Complete the steps above. 
2. Run init_db.py *WARNING: this clears the Users db* 
4. In new terminal window, npm run cypress:run


### *Notes*:
If set up, start-up with:
```bash
./start.sh
```

Pip install requirements.txt

### Set up DB:
```python
from app import db, User, Variant
db.create_all()
exit()
```

### Open sqlite3 in terminal:
```bash
sqlite3
.open db.sqlite3
 DROP table user;
 .tables
PRAGMA table_info(table_name);
```
```bash
.schema variant

# need to make tables look like this:
CREATE TABLE variant (
        rs_id VARCHAR(20), 
        gene VARCHAR(20), 
        diseases VARCHAR(20), 
        PRIMARY KEY (rs_id)     
);

.quit; to exit sqlite
```
