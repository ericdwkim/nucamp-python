import pytest

class Person:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		return self.name == other.name


def test_classes_compare():
	p1 = Person("Mindy")
	p2 = Person("Mindy")
	assert p1 == p2

