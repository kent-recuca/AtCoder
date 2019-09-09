# -*- coding: utf-8 -*-
def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        n = 0
        while i < K:i*=2;n+=1
        ans += ((1/N)*(1/2)**n)
    print(ans)
if __name__ == '__main__':
    main()