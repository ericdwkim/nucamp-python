def func_retval():
	some_int = 10
	return some_int

def test_func_retval(input_value):
	assert func_retval() == input_value
