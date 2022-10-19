## Initial Run
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`
5. `source env/bin/activate`
6. `python -m uvicorn src.main:app --reload`

## Normal Run
1. `source env/bin/activate`
2. `python -m uvicorn src.main:app --reload`


## Using Docker
1. docker build -t  project_purple_cow:latest .
2. docker run -it -p 3000:3000  project_purple_cow:latest

# End points

/docs is swagger documentation

GET /items

ex: 
curl -X 'GET' \
  'http://127.0.0.1:8000/items' \
  -H 'accept: application/json'

PUT /items/{item_id}
ex:
curl -X 'PUT' \
  'http://127.0.0.1:8000/items/2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "example"
}'


DELETE /items/{item_id}
ex:
curl -X 'DELETE' \
  'http://127.0.0.1:8000/items/2' \
  -H 'accept: application/json'



## TODO 
1. Add Database
2. Validation