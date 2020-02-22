# -*- coding: utf-8 -*-
def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = []
    for i in range(100):
        tmp = 0
        for j in range(N):
            tmp += (X[j]-i)**2
        ans.append(tmp)
    print(min(ans))
if __name__ == '__main__':
    main()
