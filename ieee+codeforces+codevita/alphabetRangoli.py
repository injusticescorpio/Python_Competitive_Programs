import string
alpha = string.ascii_lowercase
print(alpha)
n = int(input())
list=[]
for i in range(n):
    s='-'.join(alpha[i:n])
    print(s)
    list.append((s[::-1]+s[1:]).center(4*n-3,"-"))
print(list)
list5=list[::-1]+list[1:]
s='\n'.join(list5)
print(s)

