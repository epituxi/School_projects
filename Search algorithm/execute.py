from search import linearSearch
from search import binarySearch
import random
input()

table = [-9, -1, 0,	0, 1, 4, 7, 10, 11, 11, 26, 36,	44,	44,	98]
x = 0
#random.shuffle(table)
print(table)

a = linearSearch(table, x)
print(a)

b = binarySearch(table, x)
print(b)
