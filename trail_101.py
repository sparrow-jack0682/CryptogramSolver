# to create a function

from itertools import combinations_with_replacement
import enchant

d = enchant.Dict("en_US")



my_cipher = 'lloopsehwi'
letter_lst = [x for x in my_cipher]
print(letter_lst)

op = set()



for n in range(2,len(my_cipher)):

    for y in list(combinations_with_replacement(letter_lst,n)):
        z = "".join(y)
        if d.check(z):
            op.add(z)
print(op)
print(len(op))
