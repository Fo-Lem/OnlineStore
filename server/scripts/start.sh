#!/bin/bash

source //home/nginxadmin/OnlineStore/server/onlst/bin/activate
/home/nginxadmin/OnlineStore/server/onlst/bin/gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind localhost:8080