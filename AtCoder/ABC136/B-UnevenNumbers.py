# -*- coding: utf-8 -*-
def main():
    N = int(input())
    count = 0
    for i in range(N):
        L = []
        L = [int(i+1) for c in str(i+1)]
        if len(L)%2 != 0:
            count += 1
    print(count)
if __name__ == '__main__':
    main()