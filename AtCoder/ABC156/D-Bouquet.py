# -*- coding: utf-8 -*-
import math 
MOD = 10**9+7
def comb(n,k):
    nCk = 1
    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1,k+1):
        nCk *= pow(i,MOD-2,MOD)
        nCk %= MOD
    return nCk

def main():
    N,A,B = map(int,input().split())
    print((pow(2,N,MOD)-1-comb(N,A)-comb(N,B))%MOD)

if __name__ == '__main__':
    main()