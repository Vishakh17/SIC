l1=[1,2,3,4,5,6,7,8,9]
l2=[]
for i in l1:
    if i%2==1:
        l2.append(i)
        print(l2)
l1.pop()
print(l1)
l1.extend(l2)
print(l1)
l3=[2,5,3,45,67,54,32,1,23,69]
l3.sort()
print(l3)
l3.reverse()
print(l3)
l3.remove(3)
print(l3)
print(l3.index(2))
l4=list(range(1,10))
print(l4)
n_list=[11,22,33,44,55,66]
print(n_list)
print(len(n_list))