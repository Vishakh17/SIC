from collections import defaultdict

word = 'asjebfehuwheire'
counter = defaultdict(int)
for letter in word:
    counter[letter] += 1
print(counter)