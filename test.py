def add(x , y ):
    return x  + y


def curry(f):
    def g(x):
        def h(y):
            return f(x , y)
        return h
    return g

