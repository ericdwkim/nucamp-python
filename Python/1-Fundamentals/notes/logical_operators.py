x = 100
y = 200
z = 100

"""
`and` -- connects (2) boolean expressions into (1) expression; BOTH sub-expressions _MUST_
be `True` for the compound or result expression to be `True`
"""
print(x < y and y > z)  # true

"""
`or` -- connects (2) boolean expressions into (1) expression; EITHER sub-expressions _MUST_
be `True` for the compound or result expression to be `True`
"""
print(x > y or y > z)  # true

"""
`not` takes a boolean expression as its operand and reverses its logical value;
if the expression is `True`, the `not` operator returns `False` and vice-versa
"""
print(not(x > y or y > z))  # false

"""
`not` keyword simply reverses the evaluated boolean value
since x > y is false, but y > z is true, w/o the `not` keyword
this would evaluate to `true`, but `not` reverses the result, thus outputting `false`
"""
