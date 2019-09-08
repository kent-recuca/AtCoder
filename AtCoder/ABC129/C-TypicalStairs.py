# -*- coding: utf-8 -*-
def main():
    N,M = map(int,input().split())
    A = set([int(input()) for _ in range(M)])
    MOD = 1000000007
    ans = [1]
    ans.append(0) if 1 in A else ans.append(1)
    for i in range(2,N+1):
        ans.append(0)
        if i in A:
            continue
        ans[i] += (ans[i-1] + ans[i-2])
    print(ans[N] % MOD)
if __name__ == '__main__':
    main()