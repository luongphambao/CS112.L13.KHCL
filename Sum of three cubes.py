k = int(input())
check = k
t = int
if check% 9 == 4 or check % 9 == 5 or abs(k) >= 3*pow(10000,2):
    print(0, 0, 0)
elif k == 1:
    print(1, -1, 1)
elif k == 3:
    print(1, 1, 1)
elif k == -1:
    print(1, -1, -1)
elif k == -3:
    print(-1, -1, -1)
else:
    posK = 1
    if k < 0:
        k = k*(-1)
        posK = 0
    keyX = 0
    if k > 1000:
        keyX = -int(pow(k,1/3))
    else:
        keyX = -k//3
    des = -keyX
    flagout = 0
    while keyX <= des:
        temp = int((k - keyX)//2)
        posY = 1
        desY = 0
        if temp < 0:
            posY = 0
            temp =-temp
        if temp>=1500:
            keyY = int(pow(temp,1/3))
        else:
            keyY = temp//2
        if posY == 0:
            keyY == -keyY
        else:
            desY = -keyY
        desY, keyY = keyY , desY
        while keyY <=desY :
                keyT = k-(keyY**3) - (keyX**3)
                posT = 1
                if keyT <0:
                    posT = 0
                    keyT = -keyT
                keyZ = pow(keyT, 1/3)
                if keyZ - int(keyZ) == 0:
                    if posT ==0:
                       keyZ = -keyZ
                    if keyZ !=0 and keyX!=0 and keyY != 0:
                        if posK == 1:
                            print(int(keyX), int(keyY), int(keyZ))
                        else:
                            print(-int(keyX), -int(keyY), -int(keyZ))
                        flagout = 1 
                        break
                keyY +=1
        if flagout ==1: 
            break
        keyX +=1
    if flagout == 0:
        print(0, 0, 0)