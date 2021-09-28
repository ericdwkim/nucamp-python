import random

"""
randint(min, max)
returns a random intger b/w provided min, max values

"""
rng = random.randint(1, 10)
print(rng)

"""
sequence data types (list, tuple)

choice(someSequenceDataType)

"""
# list
pets = ["cat", "dog", "bird", "dinosaur"]
random_pet = random.choice(pets)
print(random_pet)

# tuple
fruits = ["apple", "bannana", "cherry"]
random_fruit = random.choice(fruits)
print(random_fruit)

"""

"""

animals = ["zebra", "lion", "tiger", "bear"]
random.shuffle(animals)

