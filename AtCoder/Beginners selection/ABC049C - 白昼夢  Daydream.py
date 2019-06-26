# -*- coding: utf-8 -*-
def main():
    S = str(input())
    SS = ['eraser','erase','dreamer','dream']
    for i in SS:
        S = S.replace(i,'')
    if len(S) == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()