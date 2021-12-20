     

def func_retval():
    some_int = 50
    return some_int

def test_func_retval(input_value):
    assert func_retval() == input_value

def test_simple_pass(input_value):
    assert True


