# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    if 6<=A<=12:
        B = B/2
    elif A<6:
        B = 0
    print(int(B))
if __name__ == '__main__':
    main()
