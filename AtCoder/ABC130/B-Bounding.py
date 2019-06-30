# -*- coding: utf-8 -*-
def main():
    N,X = map(int,input().split())
    L=[int(i) for i in input().split()]
    Ls = 0
    count = 1
    for i in range(N):
        Ls = Ls+L[i]
        if Ls<=X:
            count+=1
    print(count)
if __name__ == '__main__':
    main()