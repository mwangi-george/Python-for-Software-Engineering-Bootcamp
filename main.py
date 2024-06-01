from fastapi import FastAPI
from classes import Animal, Person, Office, HappyHour
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


@app.get("/happyhour")
def happy_hour():
    may_hh = HappyHour(1600, 1800, 20)
    return {"Food Eaten in KG": may_hh.amt_food_eaten_kg(20), "Drinks in Litres": may_hh.amt_drinks_litres(200)}
