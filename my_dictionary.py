import string

import numpy as np

# I want to build a dictionary based on two arrays.
# # One array consists of english alphabets, the other array consists of its index value.
#
# alphabet_string = string.ascii_lowercase
# # print(alphabet_string)
#
# alphabet_lst = list(alphabet_string)
# # print(alphabet_lst)
#
# alphabet_ary = np.array(alphabet_lst)
# # print(alphabet_ary)
#
# ary = []
# for i in range(len(alphabet_lst)):
#     index = i+1
#     ary.append(index)
# print(alphabet_ary)
# print(ary)

original_list = ['g', 'fytc','ghjdg', 'y', 'bmg']
length_sorted_list = []
dictionary_memory = {}


def sort_list_by_length():
    temp_list = []
    global original_list
    for i in range(0, len(original_list)):
        temp_list.insert(i, sorted(original_list, key=len)[i])
    return temp_list


def dictionary_builder(original, compare):
    for original_element in original:
        for compare_element in compare:
            if  original.index(original_element)==compare.index(compare_element
                                                                ):
                dictionary_memory[original_element] = compare_element
                compare.remove(compare_element)
                break


if __name__ == '__main__':
    print(original_list)
    length_sorted_list = sort_list_by_length().copy()
    print(length_sorted_list)
    dictionary_builder(original_list, length_sorted_list)
    # print(original_list)
    # print(length_sorted_list)
    print(str(dictionary_memory))