print("Math fns")

# abs fn --> turns sints ints to uints
abs_int = abs(-1)
print("this is the abs fn", abs_int)

# float fn --> turns ints to floats
int_to_float = float(100)
print("this is the float fn", int_to_float)

# int fn --> converts floats into ints
float_to_int = int(1.23)
print("this is the int fn", float_to_int)

"""
print(int(1.23)) --> same as above 

"""
# max fn returns greatest num
print(max(1, 2, -5, 10, 0))
# min fn returns smallest num
print(min(1, 2, -5, 10, 0))
# pow fn returns x**y
print(pow(2, 3))
# round fn returns rounded-up value
print(round(51.6))

"""
Converting User Input
//Python terminal

year  = 2021
print("The year is " + year)
>>> Traceback (most recent cal llast): File "<stdin>", line 1, in <module> 
TypeError: can only concatenate str (not "int") to str

--> this is due to Python not being able to concatenate a string ("The year is ") to an integer (2021)

How to Fix: simply make `year` from an integer to a string 

            year = "2021"
            print("The year is " + year)
        >>> The year is 2021

"""
##################################

"""
Lambda functions

lambda arg1, arg2: expression to return

NOTE: only (1) expression per line allowed in fn body (unlike JS's arrow fn which
allows for multiline fn bodies; however, only 1 expression can be returned)

"""
lambda num: num ** 2
# ^__________________^ same as square(), but anonymous and short-hand

# def square(num):
    # return num ** 2