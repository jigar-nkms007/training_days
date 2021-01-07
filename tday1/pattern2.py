n=7

m=n*2+1
for i in range(0,m):
    print('*',end='')
print('')

for i in range(0,n):
    print((n - i) * '*', end='')
    print((i+1)*' ',end='')
    print(i*' ',end='')
    print((n-i)*'*',end='')
    print('')

for j in range(0,n-1):
    print((j+2)*'*',end='')
    print(((n-1)-j)*' ',end='')
    print(((n-2)-j)*' ',end='')
    print((j+2)*'*',end='')
    print('')

for i in range(0,m):
    print('*',end='')


