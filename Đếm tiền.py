n=int(input())
can=n//500000
a1=500000
a2=200000
a3=100000
a4=50000
a5=20000
sum1=0
max1=10**10
for i in range(0,n//a1+1):
    s=n-a1*i
    for j in range(0,s//a2+1):
        s1=s-a2*j
        for k in range(0,s1//a3+1):
            s2=s1-a3*k
            for i1 in range(0,s2//a4+1):
                s3=s2-a4*i1
                if( s3%a5==0):
                    value=(i+j+k+s3//a5+i1)
                    sum1+=1
                    max1=min(max1,value)
print(sum1,end=" ")
if max1==10**10:
    print(0)
else:
    print(max1)