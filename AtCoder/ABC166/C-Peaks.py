# -*- coding: utf-8 -*-
def main():
    N,M = map(int, input().split())
    H = list(map(int, input().split()))
    ans = []
    for _ in range(N):
        ans.append(1)
    for i in range(M):
        A,B = map(int, input().split())
        if H[A-1] < H[B-1]:
            ans[A-1] = 0
        elif H[A-1] > H[B-1]:
            ans[B-1] = 0
        else:
            ans[B-1] = 0
            ans[A-1] = 0
    print(sum(ans))
if __name__ == '__main__':
    main()