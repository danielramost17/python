from collections import defaultdict
from heapq import *

def dijkstra_heap(edges, f, t):
    dic = defaultdict(list)
    for l,r,c in edges:
        dic[l].append((c,r))

    q, visited = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in visited:
            visited.add(v1)
            path = path+(v1,)
            if v1 == t:
                return (cost, path)

            for c, v2 in dic.get(v1, ()):
                if v2 not in visited:
                    heappush(q, (cost+c, v2, path))

    return float('inf')


if __name__ == "__main__":

    #The format of edges will be: [('paris', 'palaiseau', 2), ('palaiseau', 'orsay', 1)]
    edges = []
    with open('edges.txt', 'r') as file:
        for line in file.readlines():
            edges.append((line.split()[0], line.split()[1], int(line.split()[2])))
    file.close()

    s = input('Enter the source vertex: ')
    t = input('Enter the vertex you want to analyse: ')
    result = dijkstra_heap(edges, s, t)

    print('The minimal distance to go from ', s, ' to ', t, ' is ', str(result[0]))
    print('The path is: ', end='')
    list = list(result[1])
    print(list[0], end='')
    list.remove(list[0])
    for x in list:
        print(' -> ', x, end='')