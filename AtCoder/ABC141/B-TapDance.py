# -*- coding: utf-8 -*-
def main():
    S = list(input())
    for i in range(len(S)):
        if i % 2 == 0:
            if S[i] != 'R' and S[i] != 'U' and S[i] != 'D':
                print('No')
                return
        if i % 2 == 1:
            if S[i] != 'L' and S[i] != 'U' and S[i] != 'D':
                print('No')
                return
    print('Yes')
if __name__ == '__main__':
    main()
