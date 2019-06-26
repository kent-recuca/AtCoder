# -*- coding: utf-8 -*-
def main():
    N = int(input())
    d = [int(input())for i in range(N)]
    #print(d)
    out = set(d)
    print(len(out))

if __name__ == '__main__':
    main()