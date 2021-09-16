x = 100
y = 200
z = 100

print(x < y and y > z)  # true
print(x > y or y > z)  # true

"""
`not` keyword simply reverses the evaluated boolean value
since x > y is false, but y > z is true, w/o the `not` keyword
this would evaluate to `true`, but `not` reverses the result, thus outputting `false`
"""
print(not(x > y or y > z))  # false
