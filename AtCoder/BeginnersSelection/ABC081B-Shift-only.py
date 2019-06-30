# -*- coding: utf-8 -*-
def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    flg = 0
    while flg == 0:
        for i in range(len(A)):
            if A[i]%2 != 0:
                flg += 1
                break
            A[i] = A[i]/2
            if i == N-1:
                count += 1
    print(count)
if __name__ == '__main__':
    main()