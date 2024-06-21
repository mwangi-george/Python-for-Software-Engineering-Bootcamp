from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel
from typing import Tuple

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
