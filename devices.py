from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Tuple


app = FastAPI(title="Devices API Docs",
              description="Made with ❤️ by George Mwangi")


class Device(BaseModel):
    title: str
    year_made: int
    company: str


class MultipleDeviceResponse(BaseModel):
    device: list[Device]
    total: int


all_devices = {
    0: {
        "title": "Laptop",
        "year_made": 2023,
        "company": "HP"
    }
}


# TODO: Asynchronous functions

async def get_device_details(device_id: int = 0) -> Device:

    # Currently reading from a dictionary
    # Later read from DB
    device = all_devices[device_id]

    # in the case of reading from DB, we can wait which can only happen inside an asynchronous function
    # await get_device_from_db(device_id)

    return Device(**device)


def new_device(device_profile: Device):
    new_device_id = len(all_devices)

    all_devices[new_device_id] = {
        "title": device_profile.title,
        "year_made": device_profile.year_made,
        "company": device_profile.company
    }


@app.get("/device/{device_id}", response_model=Device)
async def get_device_by_id(device_id: int = 0) -> Device:
    # since we are calling an asychronously defined function we use the await keyword
    device_details = await get_device_details(device_id=device_id)
    return device_details


@app.post("/devices")
async def create_device(device_profile: Device):
    new_device(device_profile)


@app.get("/devices", response_model=MultipleDeviceResponse)
async def get_muiltiple_devices() -> MultipleDeviceResponse:
    pass
