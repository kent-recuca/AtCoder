# -*- coding: utf-8 -*-
def main():
    A,B,C = map(int,input().split())
    D = C-(A-B)
    if D < 0:
        print(0)
        return
    print(D)
if __name__ == '__main__':
    main()
