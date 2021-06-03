# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.
# Leave in code under testing, comment out code if needed for later
# reference, or delete code that is no longer wanted.
# 6. COMPARE ORIGINAL ARRAY AND ORDERED ARRAY AND BUILD A DICTIONARY TO REMEMBER ORIGINAL ORDERING (SPK).

import  numpy as np
cipher_acceptor = "g fytc y bmg "

#create list of word that are their in the cipher_acceptor.
cipher_lst = cipher_acceptor.split()


# create an array from the above list.
cipher_ary = np.array(cipher_lst)


# create a length array from the cipher_array.
cipher_len_lst = [] #create an empty list
for i in cipher_lst:
    word_len = len(i)
    cipher_len_lst.append(word_len)

#order the cipher_len_lst by its length.
ord_cipher_len_lst = np.sort(cipher_len_lst)

#changing the cipher_len_lst in to an array.
cipher_len_array = np.array(cipher_len_lst)


# order the elements of cipher_len_ary.
ord_cipher_len_ary = np.sort(cipher_len_array)


#ordering cipher_ary by its length.
ord_cipher_lst= sorted(cipher_lst,key=len)
ord_cipher_ary = np.array(ord_cipher_lst)


#we have the cipher array, ordered cipher array, length of the cipher array and the length of the ordered cipher array.
print(cipher_ary)
print(ord_cipher_ary)
print(cipher_len_array)
print(ord_cipher_len_ary)

# to make dictionary.
my_dict = dict(zip(cipher_ary,ord_cipher_ary))
print(my_dict)

# but this dictionary is not so helpfull to solve the problem. Hence we use the length array.
for s in range(len(cipher_len_lst)):
    for t in range(len(ord_cipher_len_ary)):
        print(cipher_len_lst[s]==ord_cipher_len_lst[t])

