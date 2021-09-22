def rFib(n):
    # base conditions/cases to stop the recusion (prevents infinite loops)
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)


"""
what happens when rFib(4)?

n = 4, so skips if and elif conditions
--> return rFib(4-1) + rFib(4-2)

# starting w/ the left-hand operand of above return statement ("rFib(4-1)"):
rFib(4-1) = rFib(3), where n = 3 --> recursion occurs
n = 3, so skips if and elif conditions
--> return rFib(3-1) + rFib(3-2)
rFib(3-1) = rFib(2) --> meets elif condition, so rFib(2) returns 1 
rFib(3-2) = rFib(1) --> meets elif condition, so rFib(1) returns 1
SO, rFib(3) = rFib(2) + rFib(1) = 1 + 1 = 2, so rFib(3) = 2


# finishing w/ the right-hand operand of above return statement ("rFib(4-2)"):
rFib(4-2) = rFib(2), where n = 2 --> recursion occurs
n= 2 meets elif condition, so rFib(2) returns 1
SO, rFib(2) = 1

# conclusion of when rFib(4):
return rFib(3) + rFib(2) = 2 + 1 = 3 
SO, rFib(4) = 3 


NOTE: python has a maximum recursion depth of 1000, so n >= 1000 will return a RecursionError 
"""