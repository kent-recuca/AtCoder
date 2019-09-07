# -*- coding: utf-8 -*-
def main():
    N,M = map(int,input().split())
    A = [int(input()) for i in range(M)]
    MOD = 1000000007
    ans = [0,1]
    for i in range(1,N):
        if i in A:
            ans.append(0)
        else:
            

if __name__ == '__main__':
    main()