import string

import numpy as np

# I want to build a dictionary based on two arrays.
# One array consists of english alphabets, the other array consists of its index value.

alphabet_string = string.ascii_lowercase
# print(alphabet_string)

alphabet_lst = list(alphabet_string)
# print(alphabet_lst)

alphabet_ary = np.array(alphabet_lst)
# print(alphabet_ary)

ary = []
for i in range(len(alphabet_lst)):
    index = i+1
    ary.append(index)
print(alphabet_ary)
print(ary)