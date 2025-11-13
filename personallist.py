p1=["david doe",20,1,180.0,100.0]
p2=["John Smith",25,1,170.0,70.0]
p3=["Jane Cracker",22,0,169.0,60.0]
p4=["Peter Kelly",40,1,150.0,50.0]
p_list=p1+p2+p3+p4
print(p_list)
n_persons=int(len(p_list)/5)
age_sum=0.0
for age in p_list[1::5]:
    age_sum+=age
average_age=float(age_sum)/n_persons
print("the average age is", str(average_age))