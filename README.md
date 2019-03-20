# Installation

* run following commands:
bash
```
virtualenv ENV
source ENV/bin/activate
```

# Dependencies
```
pip install -r requirements.txt
pip install -r requirements-dev.txt 
```

# Create database, tables and import data 
```
make database
```

Rename `.env.default to .env `

Run the project
```
make run
```


Some info about the project.

Created with Flask. It has 3 API endpoints.

`api/apartment`
it will return all the properties from the database

`api/apartment/<int:id>``
it will return a specific apartment

`api//location/<float:latitude>/<float:longitude>/<float:km>`

It will return a selection of properties for the selected area, with the average price/sqm and average living area/sqm. API expects longitude + latitude parameters and km's to calculate the area (bounding-box)
