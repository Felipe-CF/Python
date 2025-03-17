import random


a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

comb = [(x, y) for x in a for y in b if x + y == 5]

comb = [x**3 for x in range(10)]

comb = [x for x in range(20) if x % 3 == 0]

frutas = ['maça', 'banana', 'pera', 'uva', 'tomate']

comb = [fruta for fruta in frutas if len(fruta) < 4]

print(comb)

