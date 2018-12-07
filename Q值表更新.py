a = [[0,-1,0,0,-1,-1],
     [-1,0,-1,0,0,-1],
     [20,-1,0,-1,-1,0],
     [0,0,-1,0,-1,30],
     [-1,0,-1,-1,0,30],
     [-1,-1,0,0,0,30]]
q = [[0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]
c = [0,0,0,0,0,0]
def biggest(i):
    m = q[i - 1][0]
    for j in range(6):
        if q[i-1][j]>=m:
            m = q[i-1][j]
    return m

for b in range(1):
    for i in range(6):
        c[i] = biggest(i+1)
    for i in range(6):
        for j in range(6):
            q[i][j]=a[i][j]+0.7*c[j]
for i in range(6):
    for j in range(6):
        print("{:.2f}".format(q[i][j]),end=" ")
    print("")

