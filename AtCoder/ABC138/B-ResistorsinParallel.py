# -*- coding: utf-8 -*-
def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans += 1/A[i]
    print(1/ans)
if __name__ == '__main__':
    main()