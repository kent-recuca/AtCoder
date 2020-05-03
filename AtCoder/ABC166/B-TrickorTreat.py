# -*- coding: utf-8 -*-
def main():
    N,K = map(int,input().split())
    ans = []
    for i in range(K):
        tmp = []
        S = int(input())
        tmp = list(map(int, input().split()))
        ans.extend(tmp)
    print(N-(len(set(ans))))
if __name__ == '__main__':
    main()