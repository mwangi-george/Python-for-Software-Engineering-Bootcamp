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


if __name__ == "__main__":
    # Initialize the class
    animal_1 = Animal(height=120, weight=20)
    animal_2 = Animal(height=20, weight=40)

    print(animal_1.print_height())
