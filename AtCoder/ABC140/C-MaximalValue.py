# -*- coding: utf-8 -*-
def main():
    N = int(input())
    B = list(map(int,input().split()))
    ans = B[0]
    for i in range(1,N-1):
        ans += min(B[i-1],B[i])
    ans += B[N-2]
    print(ans)
if __name__ == '__main__':
    main()