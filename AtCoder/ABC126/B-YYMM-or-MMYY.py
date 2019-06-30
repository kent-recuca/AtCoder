# -*- coding: utf-8 -*-
def main():
    flg = 0
    answer = ['NA','AMBIGUOUS','YYMM','MMYY']
    data = list(input())
    front = data[0] + data[1]
    back = data[2] + data[3]
    front = int(front)
    back = int(back)
    if 1<=front<=12 and 1<=back<=12:
        flg = 1
    elif 0<=front<=99 and 1<=back<=12:
        flg = 2
    elif 1<=front<=12 and 0<=back<=99:
        flg = 3
    print(answer[flg])
if __name__ == '__main__':
    main()