# using regular expressions
import re

global l

input_cipher = "hjgjkls"
l = len(input_cipher)

my_text = """" a 
aa
aaa
suhas
b
bb
bbb
xlgkx
c
cc
ccc


"""



patterns = re.compile(r'(.){5,}')
# matches = patterns.finditer(my_text)
lines = my_text.split('\n')

for line in lines:
    rxx = patterns.search(line)
    if rxx:
        print(line)



