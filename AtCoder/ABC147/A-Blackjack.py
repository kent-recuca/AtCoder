# -*- coding: utf-8 -*-
def main():
    A,B,C = map(int,input().split())
    if (A+B+C) >=22:
        print('bust')
    else:
        print('win')

if __name__ == '__main__':
    main()
