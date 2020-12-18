# Question – :  Some prime numbers can be expressed as a sum of other consecutive prime numbers.

# For example
# 5 = 2 + 3,
# 17 = 2 + 3 + 5 + 7,
# 41 = 2 + 3 + 5 + 7 + 11 + 13.
# Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
# Write code to find out the number of prime numbers that satisfy the above-mentioned property in a given range.

# Input Format: First line contains a number N

# Output Format: Print the total number of all such prime numbers which are less than or equal to N.

# Constraints: 2<N<=12,000,000,000

# S.no	Input	Output	Comment
# 1	    20	        2	(Below 20 there are two such members; 5 and 17) 5=2+3 17=2+3+65+7
# 2	    15	        1	


def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
m= int(input('enter limit'))
input_list=[i for i in range(m+1)]
li=list(filter(is_prime,input_list))
s=5
c=0
for i in range(2,len(li)):
    if is_prime(s) and s<=m:
        c=c+1
    elif s>m:
        break
    else:
        pass
    s=s+li[i]
print(c)
