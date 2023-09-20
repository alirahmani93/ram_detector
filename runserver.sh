export PYTHONPATH=${pwd}:$PYTHONPATH
uvicorn src.server.api:app --reload

