def dtb(points, percents, current_point, current_rate, cols, pos, realpoint):
    
    if pos == len(percents):
        res = current_point
        res += 0.001
        if round(res, 1) == realpoint:
            for c in cols:
                if c - int(c) == 0:
                    print(int(c), end=" ")
                else:
                    print(c, end=" ")
            print()
        return

    for n in points:
        cols[pos] = n
        nextpoint = current_point + cols[pos] * percents[pos]
        nextrate = percents[pos] + current_rate
        res = nextpoint + 10 * (1 - nextrate)
        res2 = nextpoint + 0.25 * (1 - nextrate)
        if round(res + 0.001, 1) < realpoint or round(res2 + 0.001, 1) > realpoint:
            continue
        else:
            dtb(points, percents, nextpoint, nextrate, cols, pos+1, realpoint)


points = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75,
          5.0, 5.25, 5.5, 5.75, 6.0, 6.25, 6.5, 6.75, 7.0, 7.25, 7.5, 7.75, 8.0, 8.25, 8.5, 8.75, 9.0, 9.25, 9.5, 9.75, 10.0]
n = int(input())
rate = []
for i in range(n):
    percent = int(input()) / 100
    rate.append(percent)
realpoint = float(input())
cols = [0 for i in rate]
if n <= 10:
    dtb(points, rate, 0, 0, cols, 0, realpoint)