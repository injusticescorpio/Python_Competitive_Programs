def update(list):
    return list[1:]+[list[0]]
n=int(input(""))
bride=[i for i in input("").split(" ")]
groom=[i for i in input("").split(" ")]
k=0
if(len(bride)==n and len(groom)==n):
    for j in range(n+2):
        if(bride[k]==groom[k]):
            bride.pop(0)
            groom.pop(0)
        else:
            groom=update(groom)
    print(len(bride))
