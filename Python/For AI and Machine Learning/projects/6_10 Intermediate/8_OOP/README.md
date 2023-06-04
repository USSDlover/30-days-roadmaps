Object-oriented programming (OOP) is a programming paradigm that organizes code around objects, which are instances of classes. OOP allows for the creation of modular, reusable, and structured code by encapsulating data (attributes) and behavior (methods) into objects.

In Python, classes are used to define the structure and behavior of objects, and objects are instances of those classes. Here's an example that demonstrates the concept of classes, objects, and inheritance in Python:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement speak() method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create objects of Dog and Cat classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak() method on the objects
print(dog.name + ": " + dog.speak())  # Output: Buddy: Woof!
print(cat.name + ": " + cat.speak())  # Output: Whiskers: Meow!
```

In the example above, we define an `Animal` class as the base class, which has an `__init__` method to initialize the `name` attribute and a `speak` method that is intended to be implemented by subclasses. We then create two subclasses, `Dog` and `Cat`, which inherit from the `Animal` class and provide their own implementation of the `speak` method.

We create objects (`dog` and `cat`) of the `Dog` and `Cat` classes, respectively, and call the `speak` method on these objects. The `speak` method of each subclass is invoked, returning the appropriate sound.

Challenge: Your challenge is to create a new subclass called `Bird` that inherits from the `Animal` class. Implement the `speak` method in the `Bird` class to make it return "Tweet!". Create an object of the `Bird` class and call the `speak` method on it. Print the result to verify that it outputs "Tweet!".

```python
class Bird(Animal):
    def speak(self):
        return "Tweet!"

# Create an object of the Bird class
bird = Bird("Chirpy")

# Call the speak() method on the bird object
print(bird.name + ": " + bird.speak())  # Output: Chirpy: Tweet!
```

By completing this challenge, you'll gain hands-on experience with classes, objects, and inheritance in Python, and you'll understand how to create and use subclasses to extend the functionality of base classes.