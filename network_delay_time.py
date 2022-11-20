import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        graph = [[] for _ in range(N + 1)]

        for i in times:
            a, b, c = map(int, i)
            graph[a].append((b, c))
            
        def dijkstra_pq(graph, start):
            N = len(graph)
            dist = [1000000] * N

            q = [(0, K)]
            #heapq.heappush(q, (0, start))
            dist[start] = 0

            while q:
                acc, cur = heapq.heappop(q)

                if dist[cur] < acc:
                    continue

                for adj, d in graph[cur]:
                    cost = acc + d
                    if cost < dist[adj]:
                        dist[adj] = cost
                        heapq.heappush(q, (cost, adj))

            return dist


        dist = dijkstra_pq(graph, K)
        m = 0
        
        for d in range(1, len(dist)):
            if 1000000 <= dist[d]:
                return -1
            m = max(m, dist[d])
        return m
