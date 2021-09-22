# higher-order fn w/ a callback fn as a param
def a_fn(callback):
    print(callback(3))


# invoking the higher-order fn w/ a lambda fn arg
a_fn(lambda num: num ** 2)
