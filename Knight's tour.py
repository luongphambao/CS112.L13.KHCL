si=[[2,1], [1,2], [2,-1], [-1,2], [1,-2], [-1,-2], [-2, 1], [-2, -1]]

def inside(x,max):
    return x>=0 and x<max
def backtracking(path,m,n):
    if len(path)==m*n:
        for i in path:
            print(i,end=" ")
        return True

    cur=path[-1]
    x=ord(cur[0])-ord('a')
    y=int(cur[1])-1
    co_duong=False
    for i in si:
        newx=x+i[0]
        newy=y+i[1]
        if inside(newx,m) and inside(newy,n):
            new=chr(ord('a')+newx)+str(newy+1)
            if new in path: continue
            path.append(new)
            co_duong=backtracking(path,m,n)
            path.pop()
            if co_duong:break

    return co_duong

n,m=map(int,input().split())
str1=str(input())

path=[str1]
backtracking(path,m,n)