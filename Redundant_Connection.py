class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n =  len(edges)
        res = []
        #무방향 그래프, 사이클 없음 
        def find(parent, x) :
            if parent[x] != x :
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y) :
            x = find(parent, x)
            y = find(parent, y)
            if x < y :
                parent[y] = x
            else :
                parent[x] = y

        parent = [0] * (1 + n)
        for i in range(1, n+1) :
            parent[i] = i

        cycle = False

        for i in range(n) :
            x, y = edges[i][0], edges[i][1]
            if find(parent, x) == find(parent, y) :
                cycle = True
                res.append(x)
                res.append(y)
                break
            else :
                union(parent, x, y)
        return res
