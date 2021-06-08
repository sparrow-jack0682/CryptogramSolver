#  this file will be used to experiment about pydictionary.

from PyDictionary import PyDictionary as pyd

# print(pyd.meaning("physics"))
# print(pyd.meaning("jkjf"))
#
# lst = ['physics','know','gst']
#
# r = range(len(lst))
# # print(r)
# for i in r:
#     if (pyd.meaning(lst[i])) != None :
#         print('word exists')
#     else : print('word does not exists')

# alphabets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
# alphabets_lst = alphabets.split()
# print(alphabets_lst[0],range(len(alphabets_lst)))

word = ['gq']

word_str = ''.join(word)
print(word_str,type(word_str))

letter_lst = [x for x in word_str]
print(letter_lst)

asp_lst = []

for i in range(len(alphabets_lst)):
    rep_lst1 = [x.replace('g', alphabets_lst[i]) for x in letter_lst]
    for j in range(len(alphabets_lst)):
        rep_lst2 = [y.replace('q',alphabets_lst[j]) for y in letter_lst]

        word_lst = [rep_lst1[0],rep_lst2[1]]

        # print(word_lst)

        word_str1 = ''.join(word_lst)
        # print(word_str1)

        asp_lst.append(word_str1)

print(asp_lst)


for i in range(len(asp_lst)):
    if (pyd.meaning(asp_lst[i])) != None :
        print('word exists')
    else : print('word does not exists')






