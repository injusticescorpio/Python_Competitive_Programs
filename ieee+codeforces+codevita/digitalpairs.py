def bits(digit):
    a=[int(i) for i in str(digit)]
    maxi=max(a)
    mini=min(a)
    res=maxi*11+mini*7
    # a=str(res)
    if(len(str(res))>=3):
        return res%100
    else:
        return res


n=int(input("enter limit"))
list=[]
print("enter elements")
for i in range(0,n):
    x=int(input(""));
    if(len(str(x))==3):
        list.append(x)
list1=[bits(i) for i in list]
list2=[str(i) for i in list1]
count=0;
count1=0
for i in list2:
    count1=count1+1
    for j in list2[count1:]:
        print(f'i={i}   j={j}')

        if(i[0]==j[0] and (((list2.index(i)%2==0) and (list2.index(j)%2==0)) or ((list2.index(i)%2!=0) and (list2.index(j)%2!=0)) )):
            count=count+1
            break


print(f"count={count}")