from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse

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
