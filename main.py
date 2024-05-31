from fastapi import FastAPI
from classes import Animal, Person, Office
app = FastAPI()

"""Home route"""


@app.get("/")
def home():
    dog = Animal(12, 30)
    return dog.print_height()


""" user info route """


@app.get("/user")
def user_info():
    user = Person("George", "English", "Kenya", "Software Engineer")
    return user.person_language(), user.person_nationality(),


@app.get("/office")
def office_info():
    office = Office("IHL", 200, "Westlands, Nairobi")
    door_color = office.get_door_color()

    # door_color = "green"
    desk_holders = office.get_desk_holders()
    desk_holders.append(["George", "Mike", "Ross"])

    office.set_name("TechActioneers")
    return {
        "door_color": door_color,
        "desk_holders": desk_holders,
        "office_name": office.name,
        "Owner": office._private_owner
    }
