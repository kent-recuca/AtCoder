# -*- coding: utf-8 -*-
def main():
    N,Y = map(int,input().split())
    for i in range(N+1):
        for j in range(N-i+1):
            z = 10000*i + 5000*j + 1000*(N-i-j)
            if z == Y:
                print(i,j,N-i-j)
                return
    print('-1','-1','-1')
if __name__ == '__main__':
    main()