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


def get_device_details(device_id: int = 0) -> Device:
    device = all_devices[device_id]
    return Device(**device)


def new_device(device_profile: Device):
    new_device_id = len(all_devices)

    all_devices[new_device_id] = {
        "title": device_profile.title,
        "year_made": device_profile.year_made,
        "company": device_profile.company
    }


def multiple_devices(start: int = 0, limit: int = 20) -> Tuple[Device, int]:


@app.get("/device/{device_id}", response_model=Device)
def get_device_by_id(device_id: int = 0) -> Device:
    return get_device_details(device_id=device_id)


@app.post("/devices")
def create_device(device_profile: Device):
    new_device(device_profile)


@app.get("/devices", response_model=MultipleDeviceResponse)
def get_muiltiple_devices() -> MultipleDeviceResponse:
    pass
