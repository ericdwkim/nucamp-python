x = 10
y = 10

if x == y:
    print("wear a jacket")
    print("put on mittens")

# conditionals using if/elif/else statements
"""
if x < 2 is true, then print "small",
if not, but x < 10, print "medium",
if neither conditions above are true, print "large"
"""
if x < 2:
    print("small")
elif x < 10:
    print("medium")
else:
    print("Large")

# while loops
"""
while some condition(s) is/are met, run then loop through a certain task(s) until condition(s) is/are not met
"""

n = 5
# loops through while fn until n = 0, since 0 is not > 0, it exits while loop
# then prints next line of code "Blastoff"
# then prints the next line of code "0"
# rearranging lines 34 & 35 results in an output of 5, 4, 3,2,1, 0, Blastoff!
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)  # <-- n = 0

# break statement terminates current loop and resumes code execution of following statement
m = 5
while m > 1:
    print(m)
    m = m - 1
    if m == 2:
        break
print(m)  # <-- m = 2

"""
if line 44 had an indentation to remain w/in the same code block
the while loop will stop at `m = 3`, thus outputting: 5,4,3,3 
"""

# continue statement

h = 5
while h > 1:
    h = h - 1
    if h == 2:
        continue
    print(h)
