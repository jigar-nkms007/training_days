n=int(input('enter number'))
for i in range(1,n):
    m = n- i
    for j in range(1,m):
        print(' ',end='')
    for k in range(1,i+1):
        print('* ',end='')
    print('')

y=n-1
for i in range(1,y):
    z=m+i
    for j in range(1,z):
        print(' ',end='')
    print((y- i) * '* ')
print('')


