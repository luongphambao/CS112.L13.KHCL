def parity(n):
    if n % 2 == 1:
        return -1
    return 1


def partitions(n):
    p = [1] + [0] * n

    for i in range(1, n+1):
        j = 1
        k = 1
        s = 0
        while j > 0:
            kk = k*k
            j = i-((3*kk+k)//2)
            t = parity(k)
            if j >= 0:
                s = s-t*p[j]
            j = i-((3*kk-k)//2)
            if j >= 0:
                s = s-t*p[j]
            k = k+1
            p[i] = s

    return p[n]


n = int(input())
print(partitions(n) % (10**17+3))