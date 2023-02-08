a=0
b=0

n=int(input())
s=input()

for c in s:
    if c =="A":
        a+=1
    else:
        b+=1
        
if a>b:
    print('A')
elif b>a:
    print('B')
else:
    print("Tie")
