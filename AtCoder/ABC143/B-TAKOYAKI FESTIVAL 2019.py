# -*- coding: utf-8 -*-
def main():
    N = int(input())
    D = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans += (D[i]*D[j])
    print(ans)
if __name__ == '__main__':
    main()