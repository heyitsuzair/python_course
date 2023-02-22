x = 4
print(x)


def welcome():
    global x # uses global x variable, without it x that will be used will be the x within function
    x = 5
    print(f"Local x is {x}")


welcome()
print(f"Global x is {x}")
