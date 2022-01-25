string1 = input()
string2 = input()
d1 = {}
for i in string1:
    if i not in d1:
        d1[i] = 1
    else :
        d1[i] = d1[i] + 1
anagram = True
for i in string2:
    if i not in d1 or string2.count(i) != d1[i]:
        anagram = False
        break
if anagram:
    print('Those strings are anagrams.')
else :
    print('Those strings are not anagrams.')
