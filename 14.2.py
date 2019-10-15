# import re
# p = r'[Jj]ava|JAVA'
# m1 = re.search(p,'I like Java and Python.')
# print(m1)
# m2 = re.search(p,'I like JAVA and Python.')
# print(m2)

# import re
# p = r'(121){2}'
# m = re.search(p, '121121abcabc')
# print(m)
# print(m.group())
# print(m.group(1))
# p = r'(\d{3,5})-(\d{7,8})'
# m = re.search(p, '010-87654321')
# print(m)
# print(m.group())
# print(m.group(2))
# print(m.groups)

# p=r'(\S{2})-(\S{6})'
# m = re.search(p, '010-87654321')
# print(m.group())
# print(m.group(2))


import re

p = r'[Jj]ava'
text = 'I like Java and java.'

match_list = re.findall(p, text)
print(match_list)
match_iter = re.finditer(p, text)

for m in match_iter:
    print(m.group())
