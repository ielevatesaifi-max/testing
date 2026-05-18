n=76
sum=0
for i in range(len(str(n))):
    r=n%10
    sum=sum+r
    n=n//10
print(sum)