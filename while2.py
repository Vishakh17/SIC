n=int(input("enter a number to sum up to:"))
s=0
i=1
while i<=n:
    s=s+i
    i+=1
print("sum of 1 to {} is {}".format(n,s))