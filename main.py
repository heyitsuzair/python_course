def my_generate():
    for i in range(5):
        yield i


gen = my_generate()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
