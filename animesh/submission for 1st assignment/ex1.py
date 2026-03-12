
for num in range(1,101) :

    if num % 3 and num % 5 :
        print( f"{num} FizzBuzz \n" )

    elif num % 3 :
        print( "Fizz \n" )

    else :
        print( f"{num} Buzz \n" )
