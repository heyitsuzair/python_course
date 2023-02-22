

from functools import reduce
l = [1, 2, 3, 4, 5]

newl = list(map(lambda x: x**3, l))
print(newl)

newnewl = list(filter(lambda a: a > 4, l))
print(newnewl)


n = [1, 2, 3, 4]

sum = reduce(lambda x, y: x + y, n)
print(sum)
