# def average(a=2, b=2):
#     print('Average Is', (a+b)/2)


# average(b=9)


# def greet(fname, lname):
#     print('Hello', fname, lname)


# greet('Muhammad', 'Uzair')

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum/len(numbers)


avg = average(5, 5)
print(avg)
