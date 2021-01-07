import random
import time
def merge_sort(b,low,high):

    x=[]
    if(low<high):
        mid=(low+high)//2
        merge_sort(b,low,mid)
        merge_sort(b,mid+1,high)
        x=merge(b,low,mid,high)
    return x


def merge(c,low,mid,high):
    b=[]
    h=i=low
    j=mid+1

    while((h<=mid)and(j<=high)):
        if(c[h]<=c[j]):
            b.append(c[h])
            h=h+1
        else:
            b.append(c[j])
            j=j+1
        i=i+1

    if(h<=mid):
        for k in range(h,mid+1):
            b.append(c[k])
            i=i+1

    else:
        for k in range(j,high+1):
            b.append(c[k])
            i=i+1

    # print(b)
    c[low:high+1]=b
    return c


def run(b):
    s = time.time()
    # print(b)
    b=merge_sort(b.copy(),0,len(b)-1)
    # print('by mergesort',b)
    e = time.time()
    print('merge',e - s)

# if __name__ == '__main__':
#
#     a=[]
#     l = 10
#     for i in range(0,l):
#         a.append(random.randint(0,10))
#     run(a.copy())
#
#
#     print('mergesort is completed')
