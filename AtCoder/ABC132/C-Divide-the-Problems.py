# -*- coding: utf-8 -*-
def main():
    N = int(input())
    D =[int(i) for i in input().split()]
    D.sort()
    D.reverse()
    print(D[int((N/2))-1]-D[int(N/2)])
if __name__ == '__main__':
    main()