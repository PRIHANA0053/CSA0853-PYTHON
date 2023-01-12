n=input("Enter the string:")
vow="AaEeIiOoUu"
vowels=0
con=0
v=[]
c=[]
for i in range(len(n)):
    if(n[i] in vow):
        vowels+=1
        v.append(n[i])
    elif(n[i]!=" " and n[i]not in vow):
        con+=1
        c.append(n[i])
print("no of vowels:",vowels,v)
print("no of cons:",con,c)



        
