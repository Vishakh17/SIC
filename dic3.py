str1=['a','b','c','b','a','b','c']
dic={}
for ch in str1:
    dic.setdefault(ch,0)
    dic[ch] +=1
    print(list(dic.items()))
print("alphabet counting: ",dic)