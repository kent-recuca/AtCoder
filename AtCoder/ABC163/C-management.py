# -*- coding: utf-8 -*-
def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    ans = []
    for _ in range(N):
        ans.append(0)
    for i in A:
        ans[i-1]+=1
    for j in ans:
        print(j)
if __name__ == '__main__':
    main()