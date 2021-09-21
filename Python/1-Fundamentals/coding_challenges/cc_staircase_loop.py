# stars = ""
# for i in range(1, 5, 2):
#     for j in range(0, 2, 1):
#         stars += "i"
#         print(j)

"""

*
***
******
**********

"""

stars = ""
for i in range(0, 5, 1):
    for j in range(0, i, 1):
        stars += "*"
    print(stars)


"""
when i = 0, j range(0, 0)
>> ""

when i = 1, j range(0, 1)
>> "" + * --> *

when i = 2, j range(0, 2)
>> * + ** --> ***

when i = 3, j range(0, 3)
>> *** + *** -- > ******

when i = 4, j range(0, 4)
>> ****** + **** ---> **********

"""


"""
stars = ""
for x in range(5):
    stars += "*" * x
    print(stars)

when x = 0
>> "" + ('*' * 0) = "" + 0 = ""

when x = 1
>> "" + ('x' * 1) = "" + * = *

when x = 2
>> * + ('x' * 2) = * + ** = ***

etc...

"""
