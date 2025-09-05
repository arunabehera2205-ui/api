from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()


@app.get("/aruna/kumar/")
def add(a:int,b:int):
    return a+b

class subtractmodel(BaseModel):
    a: int
    b: int


def substract(a:int,b:int):
    return a-b

@app.post("/subtract")
def subtract_number(model:subtractmodel):
    return substract(model.a,model.b)


print(add(3,4))
print(substract(6,3))


