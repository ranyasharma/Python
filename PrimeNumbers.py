#prints numbers 1- 100 and lists them as odd, even, or prime 
for i in range (1,100,1) :
    count = 0 
    for num in range (2,i-1,1):
        if (i % num == 0):
            count = count + 1
    if count == 0:
        print (i, "prime")
    else:
        if i % 2 == 0:
            print (i, "even")
        else:
            if i % 2 == 1:
                print (i, "odd")
            