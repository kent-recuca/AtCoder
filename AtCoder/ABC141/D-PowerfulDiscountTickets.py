# -*- coding: utf-8 -*-
import heapq as hq
def main():
    N,M = map(int,input().split())
    A=[-int(j) for j in input().split()]
    hq.heapify(A)
    for _ in range(M):
        tmp = hq.heappop(A)
        hq.heappush(A,(-((-tmp)//2)))
    print(-sum(A))
if __name__ == '__main__':
    main()