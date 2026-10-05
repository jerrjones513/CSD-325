class Animal:
    def __init__(self, name, fur_color, behavior):
        self.name = name
        self.fur_color = fur_color
        self.behavior = behavior

    # Private method related to name
    def __get_name(self):
        return self.name

    # Private method related to fur color
    def __get_fur_color(self):
        return self.fur_color

    # Private method related to behavior
    def __get_behavior(self):
        return self.behavior

    # Public method that calls the private name method
    def display_name(self):
        print(f"Name: {self.__get_name()}")

    # Public method that calls the private fur-color method
    def display_fur_color(self):
        print(f"Fur color: {self.__get_fur_color()}")

    # Public method that calls the private behavior method
    def display_behavior(self):
        print(f"Behavior: {self.__get_behavior()}")

    # Public method showing general animal information
    def display_info(self):
        self.display_name()
        self.display_fur_color()
        self.display_behavior()


class Dog(Animal):
    def __init__(self, name, fur_color, behavior, breed):
        super().__init__(name, fur_color, behavior)
        self.breed = breed

    # Private method specific to Dog
    def __dog_behavior(self):
        return "The dog wags its tail and barks."

    # Public method that calls the Dog's private method
    def perform_behavior(self):
        print(self.__dog_behavior())

    # Demonstrates that the child cannot directly access
    # the parent's private method
    def test_parent_private_method(self):
        try:
            print(self.__get_fur_color())
        except AttributeError:
            print("Dog cannot directly access Animal's private method.")


class Cat(Animal):
    def __init__(self, name, fur_color, behavior, breed):
        super().__init__(name, fur_color, behavior)
        self.breed = breed

    # Private method specific to Cat
    def __cat_behavior(self):
        return "The cat purrs and curls up comfortably."

    # Public method that calls the Cat's private method
    def perform_behavior(self):
        print(self.__cat_behavior())

    # Demonstrates that the child cannot directly access
    # the parent's private method
    def test_parent_private_method(self):
        try:
            print(self._Animal__get_behavior())
        except AttributeError:
            print("Cat cannot directly access Animal's private method.")


# Create objects from the child classes
dog = Dog("Buddy", "Brown", "Friendly and energetic", "Golden Retriever")
cat = Cat("Luna", "Gray", "Independent and calm", "Russian Blue")

# Attempting to call the private __get_name() method
# From outside of the class
# animal = Animal("Buddy", "Brown", "Friendly")
# print(animal.__get.name())

# Program execution
print("----- DOG -----")
dog.display_info()
dog.perform_behavior()
dog.test_parent_private_method()

print("\n----- CAT -----")
cat.display_info()
cat.perform_behavior()
cat.test_parent_private_method()

## Attempting to override name mangling and
## Call a private method from outside the class
