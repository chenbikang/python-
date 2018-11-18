i = 1
while i<=9:
    j = 1
    while j<=i:
        print ("{}*{}={}".format(j,i,i*j),end=" ")
        j+=1
    i+=1
    print("")
print ("="*62)

i = 9
while i>=1:
    j = 1
    while j<=i:
        print ("{}*{}={}".format(j,i,i*j),end=" ")
        j+=1
    i-=1
    print("")
print ("="*62)

i = 1
while i<=9:
    j = i
    print("       "*(9-i),end=" ")
    while j>=1:
        print ("{}*{}={:<2}".format(j,i,i*j),end=" ")
        j-=1
    i+=1
    print("")
print ("="*62)

i = 9
while i>=1:
    j = i
    print("       " * (9 - i), end=" ")
    while j>=1:
        print ("{}*{}={:<2}".format(j,i,i*j),end=" ")
        j-=1
    i-=1
    print("")
print ("="*62)