try:
    l = [1, 4, 6, 7]
    i = int(input('Enter A Index:'))
    print(l[i])
except:
    print('Something went wrong')
finally:
    print('I am always executed')