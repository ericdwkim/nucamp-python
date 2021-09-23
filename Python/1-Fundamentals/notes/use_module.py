# importing a specific function and string var from a module
from my_module import greet, flavor

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)


# importing the entire module
"""
import my_module

my_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", my_module.flavor)

--> performs the same importing functionality, but must be notated with a period

"""

# importing a specific function from a module
"""

from my_module import greet

greet("Albert Einstein")

--> saves memory but not importing unnecessary vars, fns from same module 


"""
