# Sandbox area to test out code snippets before inclusion in cryptogram_solver.py.
# Leave in code under testing, comment out code if needed for later
# reference, or delete code that is no longer wanted.
# 6. COMPARE ORIGINAL ARRAY AND ORDERED ARRAY AND BUILD A DICTIONARY TO REMEMBER ORIGINAL ORDERING (SPK).


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
            if  (original_element)==(compare_element):
                dictionary_memory[original.index(original_element)] =  compare.index(compare_element)




if __name__ == '__main__':
    print(original_list)
    length_sorted_list = sort_list_by_length().copy()
    print(length_sorted_list)
    dictionary_builder(original_list, length_sorted_list)
    # print(original_list)
    # print(length_sorted_list)
    print(str(dictionary_memory))

