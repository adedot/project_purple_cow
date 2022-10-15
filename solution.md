## Initial Run
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`

## Normal Run
1. `source env/bin/activate`
2. `python -m uvicorn src.main:app --reload`


Using Docker
1. docker build -t  project_purple_cow:latest .
2. docker run -it -p 3000:3000  project_purple_cow:latest