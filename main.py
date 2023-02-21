a = input('Enter A Number:')
print(f"Multiplication Of {a} is:")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i}={int(a) * i}")
except ValueError:
    print('Invalid Input')
except IndexError:
    print('Index Error')
