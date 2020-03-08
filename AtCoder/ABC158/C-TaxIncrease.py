# -*- coding: utf-8 -*-
def main():
    A,B = map(int,input().split())
    for i in range(1,1010):
        if int(0.08*i)==A and int(0.1*i)==B:
            print(i)
            return
    print('-1')
if __name__ == '__main__':
    main()