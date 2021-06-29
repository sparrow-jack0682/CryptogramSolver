# using regular expressions
import re

cipher = "asd"
print(len(cipher))

fileObject = open("words_alpha.txt", "r")
data = fileObject.read()
# print(data)


# patterns = re.compile(r'(.){3,}')
# matches = patterns.finditer(data)
# lines = data.split('\n')
#
# for line in lines:
#     rxx = patterns.search(line)
#     if rxx:
#         print(line)

words = data.split()
# print(words)

for wordi in range(len(words)):
    if len(words[wordi])==len(cipher):
        print(words[wordi])


