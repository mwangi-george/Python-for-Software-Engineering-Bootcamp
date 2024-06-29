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
    first_name: str
    middle_name: Optional[str] = None
    last_name: str

    # Attributes Configurations
    class Config:
        str_max_length = 30
        str_min_length = 2


# Using a list of dictionaries for easier subsetting
# defining it globally for later use
all_names = {
    0: {
        "first_name": "George",
        "last_name": "Mwangi"
    }
}


def get_name(user_id: int = "default") -> User:
    user = all_names[user_id]
    return User(**user)


@app.get("/user/{user_id}", response_model=User)
def get_name_by_id(user_id: int = 0) -> dict:
    return get_name(user_id)


# TODO: Request Bodies (Sending Data to our server)


# a simple model to store the returned id
class CreateUserResponse(BaseModel):
    user_id: int

# function to add a user (probably to a database)


def create_user(user_profile: User) -> int:
    # Get the data using User
    # since the keys start from 0, length will be 1
    new_user_id = len(all_names)

    # add new user to dictionary using keys
    all_names[new_user_id] = {
        "first_name": user_profile.first_name,
        "middle_name": user_profile.middle_name,
        "last_name":  user_profile.last_name
    }

    return new_user_id


@app.post("/users", response_model=CreateUserResponse)
def add_user(new_user_info: User):
    user_id = create_user(new_user_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user
