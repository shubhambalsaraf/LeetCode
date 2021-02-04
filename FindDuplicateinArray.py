## Given a read only array of n + 1 integers between 1 and n,
# find one number that repeats in linear time using less than O(n) space
# and traversing the stream sequentially O(1) times.


# Sample Input: [4,1,3,1,3,3] = Output = 3

A = [4,1,3,1,3, 3]
d = {}
new = []
for i in A:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
print(max(d, key=d.get))