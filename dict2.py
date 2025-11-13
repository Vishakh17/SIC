str1=['a','b','c','b','a','b','c']
dic={}
for ch in str1:
    if ch not in dic.keys():
        dic[ch]=0
    dic[ch] +=1
    print(dic)
print("alphabet counting: ",dic)
