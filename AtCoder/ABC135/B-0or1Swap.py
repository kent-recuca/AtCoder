# -*- coding: utf-8 -*-
def main():
    N = int(input())
    A = list(map(int,input().split()))
    count = 0
    for i in range(N):
        if (i+1) != A[i]:
            count += 1
    if count==0 or count == 2:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    main()

