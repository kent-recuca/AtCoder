    # -*- coding: utf-8 -*-
def main():
    import numpy
    N = int(input())
    P =[int(i) for i in input().split()]
    count = 0
    for i in range(1,N-1):
        tmp = [P[i-1],P[i],P[i+1]]
        PP=numpy.array(tmp)
        PPI = PP.argsort()
        if PPI[1] == 1:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
