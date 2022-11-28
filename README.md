# crafty_danes

During my bootcamp days I made a basic API with node/express of [common beers in Japanese convience stores](https://github.com/mp40/CC6-API-Solo-Project) as a learning exercise. I used that project as a basis for making a basic API for Danish craft beers using python/flask

It stores the following data:

* Name of beer, as string
* Name of brewery, as string
* ABV, as float
* Type of beer as string
* Volume in ml, as integer
* Type of container, as string

The API returns the following beer object.
```json
{
    "id": 4,
    "name": "Sweet Mary",
    "brewery":"Svaneke",
    "abv": 7.9,
    "type": "Dobbelbock",
    "receptacle_size": 500,
    "receptacle_type": "bottle"
}
```
## Install procedure
```
source env/bin/activate
pip install flask
pip install pytest
```
## Initialise and seed database
```
FLASK_APP=project/app.py python -m flask init-db
```
## Run development server
```
FLASK_APP=project/app.py python -m flask run
```
## Run tests
```
python3 -m pytest
```
## How to use
### GET /beers
Returns list of beers
### GET /beers/:id
Returns beer with stated id number
### POST /beers
Adds a beer to list
### PUT /beers/:id
Updates beer
### DELETE /beers/:id
Deletes beer
