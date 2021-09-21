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
