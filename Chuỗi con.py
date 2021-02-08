def isPalidrome(s):
    n=len(s)
    if n==0:
        return False 
    for i in range(0,n//2):
        if s[i]!=s[n-i-1]:
            return  False
    return True
def solve(s,left,right,size):
    if left>=size+(right-size):
        print(s)
        return
    for i in range(left,right+1):
        if(isPalidrome(s[left:i])):
            str1=s[:i]+" "+s[i:]
            solve(str1,i+1,right+1,size)

s=str(input())
(solve(s,0,len(s),len(s)))