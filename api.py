from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Tuple, Optional

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
def home():
    return "Welcome to our fastapi application"


@app.get("/test", response_class=JSONResponse)
def test_endpoint():
    return {
        "1": "some value",
        "2": "another value",
        3: {"some internal key": "some internal value"}
    }


# some general function to get user info


def get_user_info() -> Tuple[str, str]:
    username = "test user"
    short_description = "my bio is here"
    return username, short_description


class User(BaseModel):
    usernamme: str
    short_description: str


@app.get("/user/me", response_model=User)
def user_info() -> dict:
    username, short_description = get_user_info()

    user = User(usernamme=username, short_description=short_description)
    return user


class Books(BaseModel):
    book_id: int
    book_name: str
    # optional parameter, none by default
    book_authors: Optional[list[str]] = None


def get_book_info() -> Books:
    content = {
        "book_id": 1,
        "book_name": "George the Great",
        "book_authors": ["George", "Moses", "Mwangi"]
    }

    # return the initialized class unpacking the content dict
    return Books(**content)


@app.get("/books/book_id", response_model=Books)
def book_info() -> dict:
    return get_book_info()


# Example 3
class Cars(BaseModel):
    car_id: int
    car_name: str
    car_mileage: float
    car_manufacturer: Optional[str] = None


def get_car_info() -> Cars:
    details = {
        "car_id": 2,
        "car_name": "BMW",
        "car_mileage": 20003.4,
        # "car_manufacturer": "I have no idea"
    }

    return Cars(**details)


@app.get("/cars/id", response_model=Cars)
def car_info() -> dict:
    return get_car_info()


# Example 4
class Breakfast(BaseModel):
    drink: str
    snacks: dict
    dissert: Optional[list] = None


def get_breakfast() -> Breakfast:
    content = {
        "drink": "Mixed Tea",
        "snacks": {1: "Mandazi", 2: "Fried Eggs", 3: "Veges"},
        "dissert": ["Water Melon", "Pineapples", "Cake"]
    }

    return Breakfast(**content)


@app.get("/breakfast", response_model=Breakfast)
def breakfast() -> dict:
    return get_breakfast()


# Nesting schemas

class ProfileInfo(BaseModel):
    short_bio: str
    long_bio: str
    occupation: Optional[str]


class Worker(BaseModel):
    id: int
    username: str
    profile_info: ProfileInfo  # Referencing another pydantic class


def get_worker_info() -> Worker:
    profile_contents = {
        "short_bio": "This is our short bio",
        "long_bio": "This is our very long bio",
        "occupation": "Software Engineer"
    }
    profile_info = ProfileInfo(**profile_contents)

    worker_contents = {
        "id": 1234,
        "username": "user_1",
        "profile_info": profile_info
    }

    return Worker(**worker_contents)


@app.get("/worker", response_model=Worker)
def worker() -> list:
    return get_worker_info()


# TODO: Response Models
# Adding more information to schemas using the Field class from pydantic

class House(BaseModel):
    length: float = Field(
        alias="length",
        title="House Length in Meters",
        description="This is the lenght of the house"
    )
    width: float
    height: float
    make: str = Field(
        title="Material Used",
        description="This is the main material used to make the house",
        examples=["Wood", "Stone", "Clay"],
        default=None
    )
    location: str = Field(
        title="Location of the house",
        description="This is the county where the house is located"
    )

    # we can define configurations to apply to all attributes as follows
    class Config:
        str_max_length = 50
        str_min_length = 1


def get_house_info() -> House:
    details = {
        "length": 20,
        "width": 15,
        "height": 10,
        "make": "Stone",
        "location": "Kiambu"
    }

    return House(**details)


@app.get("/house", response_model=House)
def house() -> dict:
    return get_house_info()
