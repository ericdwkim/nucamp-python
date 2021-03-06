"""
the (4) primitive data types: string, integer, float, boolean
"""

name = "Eric"
age = 27
cash = 420.69
sexy = True


# print("The data type for variable 'name' is:", type(name)) # >> string
# print("The data type for variable 'age' is:", type(age)) # >> integer
# print("The data type for variable 'cash' is:", type(cash)) # >> float
# print("The data type for variable 'sexy' is:", type(sexy)) # >> Boolean


"""
the (4) composite data types: list, dictionary, tuple, set
"""

# Data composed as a `List`; ordered sequence of multiple values
nucamp_locations = ["Seattled", "Tacoma", "Bellevue"]

# Data composed as a `Dictionary`; ORDERED collection of key-value pairs; equivalent to an array
# indexed by their unique keys, not automatically zero-indexed

"""
empty_dict = {}
"""
Eric_Info = {"name": "Eric", "age": 27, "cash": 420.69, "sexy": True}


# Data composed as a `Tuple`; similiar to a list, but IMMUTABLE
# parentheses are optional*; commas are a _MUST_
# * - parentheses are a _MUST_ if it is an empty tuple
# if a tuple only has 1 item, parenthesis are optional, BUT a trailing comma is a _MUST_
# tuples can contain values of *any* data type, including composite data types!
# tuples can contain duplicate values
"""
my_empty_tuple = ()

one_item_tuple = ("lion",)
"""
my_cool_tuple = ("apple", "bannana", "cherry")

# Data composed as a `Set`; unordered collection of values, immutable, no duplicate values

"""
sets are unordered and therefore are not indexed, and therefore contents within a set cannot be
accessed by bracket notation (eg: someSet[0])
contents can be accessed using `for in` loops 

items within a set cannot be mutable data types (lists, dicts, sets)

set_A = {"someString", 1234, (True, False)} --> this is a set

set_B = {"someString", 1234, [True, False]} --> this is NOT a set as it contains a list 

set_C = {"someString", 1234, 1234} --> this is a set that only contains (2) values as no duplicates are allowed in a set

empty_set = set() 
"""
my_cool_set = {"cats", "dogs", "bridges"}

print("The data type for variable 'nucamp_locations' is:",
      type(nucamp_locations))  # >> list
print("The data type for variable 'Eric_Info' is:",
      type(Eric_Info))  # >> dictionary
print("The data type for variable 'my_cool_tuple' is:",
      type(my_cool_tuple))  # >> tuple
print("The data type for variable 'my_cool_set' is:", type(my_cool_set))  # >> set
