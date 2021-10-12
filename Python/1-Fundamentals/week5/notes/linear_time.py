import timeit

print(timeit.timeit("[x for x in range(1_000_000)]", number=1))
print(timeit.timeit("[x for x in range(10_000_000)]", number=1))
print(timeit.timeit("[x for x in range(100_000_000)]", number=1))
