# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    C = (A+B)/2
    if C.is_integer():
        print(int(C))
        return
    print('IMPOSSIBLE')
if __name__ == '__main__':
    main()
