from time import sleep
n=4
i=0
while(i<=n+3):
    if (i<=0):
        for j in range(0, n):
            print((j)*' ','*',end='')
            print((2*(n-j))*' ','*',end='')
            print('')
            sleep(0.1)

        i=i+1

    if(i==1):
        print((n + 1) * ' ','*')
        sleep(0.1)
        i=i+1

    if(i>1):
        for j in range(0, n):
            print((n - j - 1) * ' ', '*', end='')
            print(((2 * j + 1) + 1) * ' ','*', end='')
            print('')
            sleep(0.1)
        i=0