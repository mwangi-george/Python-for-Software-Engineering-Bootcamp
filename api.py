from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel
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
