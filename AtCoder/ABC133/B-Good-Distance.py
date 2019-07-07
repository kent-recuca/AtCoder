# -*- coding: utf-8 -*-
def main():
    N,D = map(int,input().split())
    X=[list(map(int,input().split())) for i in range(N)]
    count = 0
    for i in range(N):
        for k in range(N-1-i):
            K = 0
            KK = 0
            for j in range(D):
                K += ((X[i][j])-(X[N-1-k][j]))**2
            KK = K**0.5
            if isinstance(KK,int) or KK.is_integer():
                count += 1
    print(count)
if __name__ == '__main__':
    main()