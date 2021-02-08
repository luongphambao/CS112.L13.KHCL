all=[]
def checkgiamngat(a,max1):
    n=len(a)
    if n==0:
        return 0
    for i in range(0,n):
        if a[i]!=max1-i:
            return i-n
    return 0
def checkTang(a):
    n=len(a)
    if n==0:
        return 1
    if n==1:
        return 0
    for i in range(1,n):
        s=a[i]-a[i-1]
        if s<0:
            return (i-1-n)

    return 0
def trongso(arr,max1):
    a1 = arr[0]
    a2 = arr[1]
    a3 = arr[2]
    index1=checkTang(a1)
    index2=checkTang(a2)
    index=checkgiamngat(a3,max1)
    return index1+index2+index
import copy


def atob(state,value):
        if value[0]==0 and len(state[0])>=2:
            value[0]=0
        else:
            value[0]+=1
        a = state[0].pop()
        n=len(state[1])
        if (n>=1 and value[1] == 0 and state[1][n - 1] < a):
            value[1] = 0
        else:
            if value[1] == 1:
                value[1] = 0
            else:
                value[1] -= 1
        state[1].append(a)



def atoc(state,value):
        if value[0]==0 and len(state[0])>=2:
            value[0] = 0
        else:
            value[0] += 1
        a = state[0].pop()
        n = len(state[2])
        if  (n>=1 and value[2] == 0 and state[2][n - 1] == a+1):
            value[2] = 0
        else:
            value[2] -= 1
        state[2].append(a)


def btoa(state,value):
    if value[1] == 0 and len(state[1]) >= 2:
        value[1] = 0
    else:
        value[1] += 1
    a = state[1].pop()
    n = len(state[0])
    if  (n>=1 and value[0] == 0 and state[0][n - 1] < a):
        value[0] = 0
    else:
        if value[0] == 1:
            value[0]=0
        else:
            value[0] -= 1
    state[0].append(a)
def btoc(state,value):
    if value[1] == 0 and len(state[1]) >= 2:
        value[1] = 0
    else:
        value[1] += 1
    a = state[1].pop()
    n = len(state[2])
    if (n>=1 and value[2] == 0 and state[2][n - 1] == a + 1):
        value[2] = 0
    else:
        value[2] -= 1
    state[2].append(a)


def ctoa(state,value):
    if value[2] == 0 :
        value[2] = 0
    else:
        value[2] += 1
    a = state[2].pop()

    n = len(state[0])
    if ( n>=1 and value[0] == 0 and state[0][n - 1] < a):
        value[0] = 0
    else:
        if value[0] == 1:
            value[0] = 0
        else:
            value[0] -= 1
    state[0].append(a)


def ctob(state,value):
    if value[2] == 0:
        value[2] = 0
    else:
        value[2] += 1
    a = state[2].pop()

    n = len(state[1])
    if (n>=1 and value[1] == 0 and state[1][n - 1] < a):
        value[1] = 0
    else:
        if value[1] == 1:
            value[1] = 0
        else:
            value[1] -= 1
    state[1].append(a)


def nextstates(state,value1):
    state1 = copy.deepcopy(state)
    state2 = copy.deepcopy(state)
    state3 = copy.deepcopy(state)
    state4 = copy.deepcopy(state)
    state5 = copy.deepcopy(state)
    state6 = copy.deepcopy(state)
    trongso1=copy.deepcopy(value1)
    trongso2 = copy.deepcopy(value1)
    trongso3 = copy.deepcopy(value1)
    trongso4 = copy.deepcopy(value1)
    trongso5 = copy.deepcopy(value1)
    trongso6 = copy.deepcopy(value1)
    arr1=[]
    a1=[]
    if len(state[0])>0:
        atob(state1,trongso1)
        atoc(state2,trongso2)
        arr1.append(state1)
        arr1.append(state2)
        a1.append(trongso1)
        a1.append(trongso2)

    if len(state[1])>0:
        btoa(state3,trongso3)
        btoc(state4,trongso4)
        arr1.append(state3)
        arr1.append(state4)
        a1.append(trongso3)
        a1.append(trongso4)
    if len(state[2])>0:
        ctoa(state5,trongso5)
        ctob(state6,trongso6)
        arr1.append(state5)
        arr1.append(state6)
        a1.append(trongso5)
        a1.append(trongso6)
    return [arr1,a1]


def solve(solution,  state, goalstate, depth,value,max1,value1):

    if depth >max1-2 and value<0:
        return
    if str(state[2]) == str(goalstate):
        if len(all)==0:
            all.append(list(solution))
        else:
            if len(solution)<len(all[0]):
                all.pop()
                all.append(list(solution))
        return
    nstate = nextstates(state,value1)
    nstates=nstate[0]
    giatri=nstate[1]
    max2=value
    a3=[]
    for i in range(len(giatri)):
        result=giatri[i][0]+giatri[i][1]+giatri[i][2]
        a3.append(result)
        max2=max(max2,result)
    if max2>value:
        depth=1
    for i in range(0,len(a3)):
        s=a3[i]
        if nstates[i] not in solution :
           if s==max2:
                solution.append(nstates[i])
                solve(solution, nstates[i], goalstate, depth+1,max2,max1,giatri[i])
                solution.pop()

    return

array = []
goalstate = []
for i in range(3):
    ip = [int(i) for i in input().split()]
    array.append(ip)
    goalstate.extend(ip)
goalstate.sort(reverse=True)

depth = 0
solution = [array]

max1=len(array[0])+len(array[1])+len(array[2])-1
a=checkTang(array[0])
b=checkTang(array[1])
c=checkgiamngat(array[2],max1)
value=a+b+c
value1=[a,b,c]
solve(solution,  array, goalstate, depth,value,max1,value1)
max2=0
index=0
bao=all[index]
for state in bao:
    print(*state[0])
    print(*state[1])
    print(*state[2])
    print('#')