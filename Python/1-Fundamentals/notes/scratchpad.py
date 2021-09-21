stars = ""
for x in range(5):
    stars += "*" * x
    print(stars)

"""
when x = 0
>> "" + ('*' * 0) = "" + 0 = ""

when x = 1
>> "" + ('x' * 1) = "" + * = *

when x = 2
>> * + ('x' * 2) = * + ** = ***

etc...

"""
