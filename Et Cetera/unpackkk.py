def f(*args, **kwargs):
    print("Positional: ",args,  kwargs)


f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)