#fizz buzz program (prints numbers 1- 100 and "fizz" for those with factor of 3, "buzz" for those with factor of 5, and "fizzbuzz" for those with factors of both)

for i in range(1,100,1) :
    if (i % 5 == 0) and(i % 3 == 0) :

        print("Fizz Buzz")
    else: 
        
        if i % 3 == 0 :
            print("Fizz")
        
        else:
            if i % 5 == 0 :
                print("Buzz")
            else: 
                print(i)