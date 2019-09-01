# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    if B == 1:
        print(0)
        return
    tap = A
    ans = 1
    while True:
        if tap >= B:
            print(ans)
            return
        tap+=A-1
        ans+=1
if __name__ == '__main__':
    main()