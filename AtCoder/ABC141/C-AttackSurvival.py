# -*- coding: utf-8 -*-
def main():
    N,K,Q = map(int,input().split())
    A=[int(input()) for i in range(Q)]
    Ns=[0 for i in range(N)]
    for i in A:
        Ns[i-1] += 1
    SUM = sum(Ns)
    for j in range(N):
        if K<=SUM-Ns[j]:
            print('No')
        else:
            print('Yes')
if __name__ == '__main__':
    main()