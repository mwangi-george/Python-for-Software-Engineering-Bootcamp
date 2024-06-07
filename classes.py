class Animal:

    # What to call when the class is initialized
    # the self keyword allows us to reference the properties of the class itself
    def __init__(self, height: int, weight: int):
        # height and weight are attributes of the class
        self.height = height
        self.weight = weight

    def print_height(self):
        return f"This animals height is {self.height}"


class Person:

    def __init__(self, name, language, nationality, profession) -> None:
        self.name = name
        self.language = language
        self.nationality = nationality
        self.profession = profession

    def person_language(self):
        return f"{self.name} speaks {self.language}"

    def person_nationality(self):
        return f"{self.name} comes from {self.nationality}"

    def person_profession(self):
        return f"{self.name}'s profession is {self.profession}"

    def show_profession_again(self):
        """Reference other methods of the same class """
        return f"{self.person_language()} and {self.person_nationality()}"


class Office:

    # shared variables (not part of the initialization)
    door_color = "blue"  # strings are immutable objects inside the class
    desk_holders = ["Robert", "Dan"]   # lists are mutable objects

    def __init__(self, name, size_sqft, location) -> None:
        self.name = name
        self.size_sqft = size_sqft
        self.location = location
        # private variables (start with underscore)
        self._private_owner = "Mwangi George"

    def get_door_color(self):
        return self.door_color

    def get_desk_holders(self):
        return self.desk_holders

    # updating initialization values
    def set_name(self, new_name):
        self.name = new_name


class HappyHour:
    """Characteristics of Happy hour at IHL"""

    def __init__(self, start_time, end_time, people_available) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.people_available = people_available
        self._favorite_drink = "white cap"

    def amt_food_eaten_kg(self, plate_size):
        amt = self.people_available * plate_size
        return amt

    def amt_drinks_litres(self, pack_size):
        amt = self.people_available * pack_size
        return amt, self.amt_food_eaten_kg(20)


# TODO:
""" Class inheritance """

# Parent Class


class Car:
    def __init__(self, color: str, capacity: int, wheels: int) -> None:
        self.color = color
        self.capacity = capacity
        self.wheels = wheels

    def get_normal_capacity(self):
        return self.capacity

    def get_vehicle_color(self):
        return self.color


# Child Class that inherits Car class
class Matatu(Car):
    def __init__(self, color, capacity, wheels) -> None:
        super().__init__(color, capacity, wheels)

    def get_extra_capacity(self, car_age_years: int):
        if car_age_years > 5:
            extra_capacity = 0
        else:
            extra_capacity = 3
        return extra_capacity

    def get_wheels(self):
        return self.wheels

    # we can chnage behaviour of methods in the base Class by overwriting them
    def get_normal_capacity(self):
        return 30

    # if we need to define methods that dont need access to the class itself we do as follows

    @staticmethod
    def greeting(user_name):
        """ This method does not need access to the class methods or attributes

        Does not need the self key
        We can also add other parameters
        """
        print(f"Hello {user_name}")

    # class methods - allows us to call a class method or attribute with having to initialize the class first
    @classmethod
    def car_loved_or_hated(self, love=True):
        if love:
            return "This car is really loved"


class Config:
    """ We do not have to initialize this class to access its attributes or methods"""
    DEVELOPMENT = "https://localhost/8000"
    PRODUCTION = "https://superserver.com"

    def __init__(self) -> None:
        pass

    @classmethod
    def server_endpoints(self):
        return {"dev": self.DEVELOPMENT, "prod": self.PRODUCTION}


class NtdModelingWorkshop:
    def __init__(self, countries: list, partners: list, donors: list) -> None:
        self.countries = countries
        self.partners = partners
        self.donors = donors

    def workshop_participants(self):
        return {
            "Countries": self.countries,
            "Partners": self.partners,
            "Donors": self.donors
        }


if __name__ == "__main__":
    # Initialize the class
    may = HappyHour(1600, 1800)
