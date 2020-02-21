# -*- coding: utf-8 -*-
def main():
    N,M = map(int,input().split())
    L = []
    R = []
    for _ in range(M):
        l,r = map(int,input().split())
        L.append(l)
        R.append(r)
    L.sort(reverse=True)
    R.sort()
    lmax = L[0]
    rmin = R[0]
    print(max(0,rmin-lmax+1))



if __name__ == '__main__':
    main()