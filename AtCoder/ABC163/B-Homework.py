# -*- coding: utf-8 -*-
def main():
    N,M = map(int,input().split())
    A = [int(i) for i in input().split()]
    for i in A:
        N -= i
    if N < 0:
        print('-1')
    else:
        print(N)
if __name__ == '__main__':
    main()