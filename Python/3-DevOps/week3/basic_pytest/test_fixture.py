import pytest

@pytest.fixture
def data_set():
	return (-111, -33.3, -5, 0, 0.67, 12, 100, 'abc')

def add_all_pos_nums(numbers):
	total = 0
	for n in numbers:
		if type(n) == str:
			continue
		if n > 0:
			total += n
	return total

def test_add_pos_ints(data_set):
	assert add_all_pos_nums(data_set) == 112.67
