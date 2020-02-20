# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    if 1 <= A < 10 and 1<= B < 10:
        print(A*B)
    else:
        print('-1')

if __name__ == '__main__':
    main()