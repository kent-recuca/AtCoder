# -*- coding: utf-8 -*-
def main():
    S = list(input())
    S.sort()
    SS = set(S)
    if len(SS)==2 and S[0]==S[1] and S[2]==S[3]:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()
