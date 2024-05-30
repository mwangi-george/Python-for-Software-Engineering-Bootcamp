from fastapi import FastAPI
from classes import Animal, Person
app = FastAPI()

"""Home route"""


@app.get("/")
def home():
    dog = Animal(12, 30)
    return dog.print_height()


""" user info route """


@app.get("/user")
def user_info():
    user = Person("George", "English", "Kenya", "Software Engineer")
    return user.person_language(), user.person_nationality(), user.person_profession()
