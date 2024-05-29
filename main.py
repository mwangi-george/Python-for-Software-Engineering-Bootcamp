from fastapi import FastAPI
from classes import Animal
app = FastAPI()


@app.get("/")
def home():
    dog = Animal(12, 30)
    return dog.print_height()
