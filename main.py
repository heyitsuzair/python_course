# with open('test.txt', 'r') as f:
#     print(type(f))

#     f.seek(6)

#     print(f.tell())
#     data = f.read(1)

#     print(data)

with open('hello.txt', 'w') as f:
    f.write('Hello World')
    f.truncate(5)
