from typing import Union

from fastapi import FastAPI

##crear la aplocacion 'FastApi()'
app = FastAPI()

##paginas @app.get("/")
@app.get("/")
def read_root():
    return {"": "World"}
##paginas @app.get("/") entonces http://127.0.0.1:8000/Erick
@app.get("/Erick")
def read_root():
    return {"Hello1": "World1"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}