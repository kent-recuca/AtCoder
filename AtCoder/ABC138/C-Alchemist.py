# -*- coding: utf-8 -*-
def main():
    N = int(input())
    v = list(map(int,input().split()))
    while len(v)>1:
        v.sort()
        v1 = v.pop(0)
        v2 = v.pop(0)
        v.append((v1+v2)/2)
    print(v[0])

if __name__ == '__main__':
    main()