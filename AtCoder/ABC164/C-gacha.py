# -*- coding: utf-8 -*-
def main():
    N = int(input())
    S = [str(input()) for i in range(N)]
    d = {}
    for i in S:
        if not(i in d):
            d[i] = 0
    print(len(d))
if __name__ == '__main__':
    main()