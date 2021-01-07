from threading import *
from quicksort import run
import random
import time

s=time.time()
a = []
for i in range(0, 10000):
    a.append(random.randint(0, 10000))

t1 = Thread(target=run, args=(a,))

t1.start()



from merge_sort import run

t2 = Thread(target=run, args=(a,))
t2.start()



t1.join()
t2.join()

e=time.time()

print(e-s)