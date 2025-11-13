# d={'a':10,'b':20,'c':30,'d':40}
# d.setdefault('f',50)
# d.update(d=100)
# print(d.pop("a"))
# print(d)

# print(d.pop('f',50))

d = {'a':10,'b':20,'c':30,'d':40,'e':50}
print(d)

a = d.get('a')
print(a)

d.items()
for str1,num in d.items():
    print(str1,":", num)

s = 'Welcome to python'
s.split()
print(s)