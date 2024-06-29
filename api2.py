from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Tuple, Optional

app = FastAPI()

# TODO: Path Parameters


class Roads(BaseModel):
    road_id: int = Field(default=1)
    road_name: str = Field(
        title="Road name",
        description="This is the name of the road"
    )
    lanes: int = Field(
        title="Lanes on the Road",
        description="This is the number of lanes on the road"
    )
    origin: str = Field(
        title="Road start location",
        description="This is the name of the location where the road starts"
    )
    destination: str = Field(
        title="Road end location",
        description="This is the name of the location where the road ends"
    )

    class Config:
        str_max_length = 30
        str_min_length = 2


def get_road_info(road_id) -> Roads:
    all_roads = {
        1: {
            "road_id": 1,
            "road_name": "Thika Super Highway",
            "lanes": 10,
            "origin": "Nairobi City",
            "destination": "Thika Town"
        },
        2: {
            "road_id": 2,
            "road_name": "Nairobi-Nakuru Highway",
            "lanes": 4,
            "origin": "Nairobi City",
            "destination": "Nakuru Town"
        },
        3: {
            "road_id": 3,
            "road_name": "Mombasa Road",
            "lanes": 6,
            "origin": "Nairobi City",
            "destination": "Mombasa Town"
        },
        4: {
            "road_id": 4,
            "road_name": "Ngong Road",
            "lanes": 2,
            "origin": "Nairobi City",
            "destination": "Ngong Town"
        },
        5: {
            "road_id": 5,
            "road_name": "Mundoro - Kiganjo - Kimbo",
            "lanes": 2,
            "origin": "Mundoro Town",
            "destination": "Kimbo"
        }
    }

    # Subset dictionary to get details for a specified road
    road_details = all_roads[road_id]
    return Roads(**road_details)


@app.get("/roads/{road_id}", response_model=Roads)
def get_road_by_id(road_id: int) -> dict:
    return get_road_info(road_id)


# More than one path parameters

class User(BaseModel):
    id: int
    first_name: str
    middle_name: Optional[str] = None
    last_name: str

    # Attributes Configurations
    class Config:
        str_max_length = 30
        str_min_length = 2


def get_name(name_id: str = "default") -> User:
    # Using a list of dictionaries for easier subsetting using the index
    all_names = {
        "default": {
            "id": 0,
            "first_name": "George",
            "last_name": "Mwangi"
        },
        "user_1": {
            "id": 1,
            "first_name": "Alex",
            "middle_name": "Ross",
            "last_name": "McRuger"
        },
        "user_2": {
            "id": 2,
            "first_name": "James",
            "last_name": "Bond"
        },
        "user_3": {
            "id": 3,
            "first_name": "Michael",
            "middle_name": "McGovern",
            "last_name": "John II"
        }
    }

    user = all_names[name_id]
    return User(**user)


@app.get("/user/{name_id}/{origin}/{age}", response_model=User)
def get_name_by_id(name_id: str, origin: str, age: int) -> dict:
    return get_name(name_id)


# TODO: Request Bodies (Sending Data to our server)

@app.post("/users")
def add_user():
    pass
