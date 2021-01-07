
import sys
import time

def partition(c,pivot,high):
    i = pivot + 1
    j = high

    while (i<=j):
        if (c[i]>=c[pivot]):
            while(i<=j):
                if (c[j]<c[pivot]):
                    c[i], c[j] = c[j], c[i]
                    break
                else:
                    j=j-1
        else:
            i=i+1

    c[pivot],c[j]=c[j],c[pivot]
    # print(c)
    return i

def quiksort(b,pivot,high):



    if(high>pivot):

        pi=partition(b,pivot,high)

        quiksort(b,pivot,pi-1)

        quiksort(b,pi,high)

        return  b


def run(b):
    s = time.time()
    sys.setrecursionlimit(100000)
    # print(b)
    b=quiksort(b.copy(), 0,len(b)-1)
    # print('by quicksort',b)
    e=time.time()
    print('quick', e-s)


# if __name__ == '__main__':
#
#
    # import sys
    # sys.setrecursionlimit(100000)
#     a=[]
#     l = 10
#     for i in range(0,l):
#         a.append(random.randint(0,l))
#     run(a.copy())



