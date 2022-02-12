# Dijkstra short path with heap
# greedy, 최단거리가 처리되면(heap에서 꺼내서) 그것이 최단거리.

import heapq
import sys
INF = int(1e9) # 10억

n,m = map(int, sys.stdin.readline().split())
# n = 노드의 수, m = 간선의 수
start = int(input())
graph =  [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  a,b,c = map(int, sys.stdin.readline().split())
  graph[a].append((b,c))

def dijkstra(start):
  heap = []
  heapq.heappush(heap, (0,start)) # (거리, 지점)
  distance[start] = 0
  while heap:
    dist, now = heapq.heappop(heap)
    # 가장 최단거리가 짧은 노드 꺼내기
    if distance[now] < dist:
      # 현재 노드가 이미 처리된 적 있는 경우 무시
      continue
    for i in graph[now]:
      cost  = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(heap, (cost,i[0]))

dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("도달할 수 없음.")
  else:
    print(distance[i])

