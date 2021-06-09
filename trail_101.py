# to create a function

from itertools import combinations_with_replacement
import enchant

d = enchant.Dict("en_US")

alphs = ['a b c d e f g h i j k l m n o p q r s t u v w x y z ']
print(alphs,type(alphs))

my_cipher = 'extreme'
letter_lst = [x for x in my_cipher]
print(letter_lst)

op = set()



for n in range(4,len(my_cipher)):
    for y in list(combinations_with_replacement(letter_lst,n)):
        z = "".join(y)
        if d.check(z):
            op.add(z)
print(op)

