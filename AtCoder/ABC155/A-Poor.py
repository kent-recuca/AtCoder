# -*- coding: utf-8 -*-
def main():
    N = list(map(int,input().split()))
    if len(set(N)) == 2:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()