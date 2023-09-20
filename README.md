# Ram Detector
Ram Detector project will recorde all ram states in intervals 

## Setup Environment
> virtualenv venv
 
> . venv/bin/activate
 
> pip install -r requirements.txt

> export PYTHONPATH=${pwd}:$PYTHONPATH


## Run backend 
> source ./init.sh

## Run Server
> source ./runserver.sh

## Run Tests
> export PYTHONPATH=${pwd}:$PYTHONPATH

> pytest

## API 

`http://127.0.0.1:8000/ram-data/{n}` n value is a integer >= 0 
returns the number of RAM states 

`http://127.0.0.1:8000/` returns hello and next link 
