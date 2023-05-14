from os import system

system('gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind localhost:8080')