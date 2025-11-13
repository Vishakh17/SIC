from collections import defaultdict
k=("a","b","c","d")
x=dict.fromkeys(k,100)
y=defaultdict(int)
print(x)
print(y['z'])