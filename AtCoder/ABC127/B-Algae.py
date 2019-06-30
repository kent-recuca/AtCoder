
    # -*- coding: utf-8 -*-
def main():
    r,D,x = map(int,input().split())
    xs = list()
    xs.append(x)
    for i in range(10):
        xst = r*xs[i]-D
        xs.append(xst)
        if i != 0:
            # print(xs[i])
    print(xs[10])
if __name__ == '__main__':
    main()