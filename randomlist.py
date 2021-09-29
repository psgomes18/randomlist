import random
randomlist = []
d = 500000
for i in range(d):
    randomlist.append(random.randint(0,d))

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
print(bubbleSort(randomlist))