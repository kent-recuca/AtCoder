# -*- coding: utf-8 -*-
def main():
    N = int(input())
    if N % 2 == 0:
        ans = (N/2)/N
    elif N % 2 == 1:
        ans = ((N+1)/2)/N
    print(ans)
if __name__ == '__main__':
    main()
