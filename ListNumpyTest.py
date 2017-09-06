import numpy as np
a=np.arange(1,10).reshape(3,3)
b=[[1,2,3],[4,5,6],[7,8,9]]
print a
c=np.array(range (1,10))
number=input("input a number:")
letter="X"
for x in range (0,3):
    for y in range (0,3):
        if a[x,y]==number:
            b[x][y]=letter
            break




print b[0][0] ,"|", b[0][1] ,"|", b[0][2]
print("---------")
print b[1][0],"|",b[1][1],"|",b[1][2]
print("---------")
print b[2][0],"|",b[2][1],"|",b[2][2]
