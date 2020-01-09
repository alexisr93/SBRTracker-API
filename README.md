#RESTful API

> Uses Python3, Flask, SQLAlchemy, Marshmallow

``` bash
# Create Virtual Environment
$ python3.7 -m venv venv

# Start venv
$ . venv/bin/activate

# End venv
$ deactivate

# Create Database
$ python3.7
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python3.7 app.py
```

## Endpoints

* GET     /incident
* GET     /incident/:id
* POST    /incident
* PUT     /incident/:id
* DELETE  /incident/:id
