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


@app.get("/user/me")
def user_info() -> dict:
    return {"username": "some_username", "short_description": "My bio is here"}
