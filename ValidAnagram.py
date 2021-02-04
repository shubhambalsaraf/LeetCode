# https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram


def anagram(s,t):
    s.replace(' ','').lower()
    t.replace(' ','').lower()
    d = {}
    for x in s:
        if x not in d:
            d[x] = 1
        else:
            d[x] +=1
    for x in t:
        if x not in d:
            d[x] = 1
        else:
            d[x] -=1
    for k,v in d.items():
        if v == 1:
            return False
    return True
anagram('caption', 'niotpac')