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
all_users = {
    0: {
        "first_name": "George",
        "middle_name": "Ngugi",
        "last_name": "Mwangi"
    }
}


def get_user(user_id: int = 0) -> User:
    """
    Function to get a user's information by id 

    :param user_id: int - Unique monotonically increasing integer id
    :return: User object
    """

    # The docstring can be accessed by calling get_user().__doc__
    user = all_users[user_id]
    return User(**user)


@app.get("/user/{user_id}", response_model=User)
def get_user_by_id(user_id: int = 0) -> dict:
    user = get_user(user_id)
    print(f"The docstring of get_user function is {get_user.__doc__}")
    return user


# TODO: Request Bodies (Sending Data to our server)


# a simple model to store the returned id
class CreateUserResponse(BaseModel):
    user_id: int

# function to add a user (probably to a database)


def create_or_update_user(user_profile: User, new_user_id: Optional[int] = None) -> int:
    # Get the data using User
    # since the keys start from 0, length will be 1
    if new_user_id is None:
        new_user_id = len(all_users)

    print("Before")
    print(all_users)
    # add new user to dictionary using keys
    all_users[new_user_id] = {
        "first_name": user_profile.first_name,
        "middle_name": user_profile.middle_name,
        "last_name":  user_profile.last_name
    }

    print("After")
    print(all_users)

    return new_user_id


@app.post("/users", response_model=CreateUserResponse)
def add_user(new_user_info: User):
    user_id = create_or_update_user(new_user_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user


# TODO: Query Parameters

class MultipleUsersResponse(BaseModel):
    """Every element in the users list is going to be of class User"""
    users: list[User]
    total: int


# functions to get multiple users
def get_multiple_users_with_pagination(start: int, limit: int) -> Tuple[list[User], int]:
    """Get 2 users at a time"""

    list_of_users = []  # start with an empty list of users

    keys = list(all_users.keys())  # get all keys in the all_users dictionary
    total = len(keys)
    # loop over the keys
    for index in range(0, len(keys), 1):
        if index < start:
            continue

        current_key = keys[index]
        user = get_user(current_key)
        list_of_users.append(user)

        if len(list_of_users) >= limit:
            break

    return list_of_users, total


@app.get("/users", response_model=MultipleUsersResponse)
def get_multiple_users_paginated(start: int = 0, limit: int = 2):
    users, total = get_multiple_users_with_pagination(start, limit)
    formatted_users = MultipleUsersResponse(users=users, total=total)
    return formatted_users


# TODO: PUT Method
""" The put method allows us to create a new entity or update an existing one"""


@app.put("/user/{user_id}")
def update_user(user_id: int, user_profile: User) -> None:
    create_or_update_user(user_profile, user_id)
    return None


# TODO: Delete Method
""" Allows us to delete an entity """


# a function to perform deletion
def delete_user(user_id: int) -> None:
    # add error handling for key not found
    del all_users[user_id]  # just deleting the keys


@app.delete("/user/{user_id}")
def remove_user(user_id: int) -> None:
    delete_user(user_id)
    return None


# TODO: The Patch Method
"""
The PATCH method is used when you want to apply partial modifications to a resource. It is
similar to the PUT method in that you specify exactly the resource you want to update, but the
PUT method is used for either an insert or a replace, whereas the PATCH is a partial update.
"""

""" implement the PATCH method to update the user information. Specifically, the
PATCH method should allow updating the middle name, but no other properties.
"""


def update_middle_name(user_id: int, middle_name: str) -> None:
    all_users[user_id]["middle_name"] = middle_name
    return None


@app.patch("/user/{user_id}", response_model=User)
def update_user_middle_name(user_id: int, middle_name: str) -> User:
    """
    Endpoint for updating a user's middle name

    :param user_id: int - Unique monotonically increasing integer id

    :param middle_name: str - New user's middle name string

    :return: A dictionary with the updated User's information
    """
    update_middle_name(user_id, middle_name)
    return get_user(user_id=user_id)
