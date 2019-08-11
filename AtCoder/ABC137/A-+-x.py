# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    ans = []
    ans.append(A+B)
    ans.append(A-B)
    ans.append(A*B)
    print(max(ans))

if __name__ == '__main__':
    main()