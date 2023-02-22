
def greet(fn):
    def mfx(*args, **kwargs):
        print('Good Morning')
        fn(*args, **kwargs)
        print('Thanks For Using This Func')
    return mfx


@greet
def hello():
    print('Hello World')

@greet
def add(x, y):
    print(x+y)


hello()
add(1,2)
