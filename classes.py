class Animal:

    # What to call when the class is initialized
    # the self keyword allows us to reference the properties of the class itself
    def __init__(self, height: int, weight: int):
        # height and weight are attributes of the class
        self.height = height
        self.weight = weight

    def print_height(self):
        return f"This animals height is {self.height}"


if __name__ == "__main__":
    # Initialize the class
    animal_1 = Animal(height=120, weight=20)
    animal_2 = Animal(height=20, weight=40)

    print(animal_1.print_height())
