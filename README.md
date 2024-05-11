# Quickstart

### Run Website
- Needs Docker desktop running
- ```docker compose up --build```
- ```localhost:8000```

### DB
- ```docker ps``` -> have a look at the db docker container id
- ```docker exec -ti <container-id> psql -U postgres``` -> to take a look at what's in the db (there is a defaut db set up called default_db)
- This FastAPI app is configured to use the docker db (connection string is of the docker container) so cannot run using ```uvicorn...```

### Dev
- For development you may need a venv -> ```python3 -m venv .venv```
- Activate venv -> ```source .venv/bin/activate```
- Install required packages -> ```pip install -r requirements.txt```
- Update requirements -> ```pip freeze > requirements.txt```
- N.B. above commands are for MAC 
