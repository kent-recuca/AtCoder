# -*- coding: utf-8 -*-
def main():
    N,R = map(int,input().split())
    if N >= 10:
        print(R)
        return
    else:
        print(R+(100*(10-N)))
if __name__ == '__main__':
    main()
