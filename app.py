from itertools import product

dataset = ['A', 'B', 'C']

printList = list(product(dataset, repeat = 3))
print(printList)