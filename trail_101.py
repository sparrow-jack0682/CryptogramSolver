# to create a function

from itertools import combinations_with_replacement
import enchant
from PyDictionary import PyDictionary as pyd

d = enchant.Dict("en_US")



my_cipher = 'abcdefghij'
letter_lst = [x for x in my_cipher]
print(letter_lst)

op = []



for n in range(5,len(my_cipher)):

    for y in list(combinations_with_replacement(letter_lst,n)):
        z = "".join(y)
        if d.check(z):
            op.append(z)

print(op)

