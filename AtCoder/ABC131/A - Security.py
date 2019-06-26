# -*- coding: utf-8 -*-
def main():
    S = list(str(input()))
    #print(S)
    for i in range(len(S)):
        if i == 0:
            t = int(S[0])
            continue
        else:
            t = int(S[i-1])
            #print(t)
            if t == int(S[i]):
                print('Bad')
                return
    print('Good')


if __name__ == '__main__':
    main()
