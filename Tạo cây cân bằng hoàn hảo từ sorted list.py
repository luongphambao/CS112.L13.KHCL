def Print(left,right,a):
    if left>right:
        return
    mid=(left+right)//2
    Print(left,mid-1,a)
    Print(mid+1,right,a)
    print(a[mid])
a=[]
while True:
    try:
        a.append(input())
    except:
        break
Print(0,len(a)-1,a)