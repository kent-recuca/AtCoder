    # -*- coding: utf-8 -*-
def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    cnt = 0
    for i in H:
        if i >= K:
            cnt +=1
    print(cnt)
if __name__ == '__main__':
    main()
