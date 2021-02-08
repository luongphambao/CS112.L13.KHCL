import heapq
n, start = input().split()
n = int(n)
graph = dict()
visited = set()
point = set()
for i in range(n):
    frm, to, w = input().split()
    point.add(frm)
    point.add(to)
    w = int(w)
    if frm in graph:
        heapq.heappush(graph[frm], (w, to))
    else:
        graph[frm] = [(w, to)]

solution_len = len(point)
visited.add(start)
path = ['' for i in range(solution_len + 1)]
path[0] = start
solutions = []


def shipper(graph, solutions, path, visited, pos, frm, end, cost, solution_len):
    if pos == solution_len:
        for t in graph[frm]:
            w, to = t
            total_cost = w + cost
            if to == end:
                path[pos] = end
                heapq.heappush(solutions, (total_cost, path[:]))
                path[pos] = ''
                return
        return

    for t in graph[frm]:
        w, to = t
        if to not in visited:
            visited.add(to)
            path[pos] = to
            shipper(graph, solutions, path, visited,
                    pos + 1, to, end, cost + w, solution_len)
            visited.remove(to)
            path[pos] = ''


shipper(graph, solutions, path, visited, 1, start, start, 0, solution_len)
if len(solutions) > 0:
    w, solution = heapq.heappop(solutions)
    print(*solution)