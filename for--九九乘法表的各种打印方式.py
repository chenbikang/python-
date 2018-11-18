print("="*62)
for i in range (1,10):#输入正常9*9表
    for j in range(1,i+1):
        print("{}*{}={:<2}".format(j,i,i*j),end=" ")
    print(" ")
print("="*62)

for a in range(9,0,-1):#输入正常9*9表的水平镜像
    for b in range(1,a+1):
        print("{}*{}={:<2}".format(b,a,a*b),end=" ")
    print(" ")
print("="*62)

for x in range (1,10):#输入正常9*9表的垂直镜像
    for k in range(1, 10 - x):
        print(end="       ")
    for y in range(x,0,-1):
        print("{}*{}={:<2}".format(y,x,x*y),end=" ")
    print(" ")
print("="*62)

for m in range (9,0,-1):#输入正常9*9表的垂直镜像的水平镜像
    for k in range(1, 10 - m):
        print(end="       ")
    for n in range(m,0,-1):
        print("{}*{}={:<2}".format(n,m,m*n),end=" ")
    print(" ")
print("="*62)

