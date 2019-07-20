# -*- coding: utf-8 -*-
import copy
def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    Am = max(A)
    if A.count(Am)>1:
        for j in range(N):
            print(Am)
        return
    Ap = copy.copy(A)
    set(Ap)
    Ap.sort(reverse=True)
    for i in range(N):
        if  A[i] != Am:
            print(Am)
        else:
            print(Ap[1])
if __name__ == '__main__':
    main()