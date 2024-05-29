from fastapi import FastAPI
from classes import Animal, Person
app = FastAPI()


@app.get("/")
def home():
    dog = Animal(12, 30)
    return dog.print_height()


@app.get("/user")
def user_info():
    user = Person("George", "English", "Kenya", "Software Engineer")
    lang, *_, work = user.person_language(), user.person_nationality(), user.person_profession()
    return lang, work
