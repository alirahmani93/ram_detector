from fastapi import FastAPI
from src.db.database import connection

app = FastAPI()


@app.get("/")
def read_main():
    return {"msg": "Hello World", 'link': 'http://127.0.0.1:8000/ram-data/1/'}


# API2: Retrieve the last n RAM data as JSON
@app.get("/ram-data/{n}")
async def get_ram_data(n: int):
    with connection as conn:
        data = conn.get_all(raw='SELECT * FROM ram_usage ORDER BY timestamp DESC LIMIT (?)', parameters=(n,))
        result = []
        for row in data:
            result.append({
                "total": row[1],
                "free": row[2],
                "used": row[3],
                "timestamp": row[4]
            })
    return result
