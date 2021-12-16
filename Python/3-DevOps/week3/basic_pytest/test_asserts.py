def func_retval():
	some_int = 10
	return some_int

# def test_func_retval():
#	assert func_retval() == 4


def test_sets_compare():
	set1 = set("abcd")
	set2 = set("aced")
	assert set1 == set2


