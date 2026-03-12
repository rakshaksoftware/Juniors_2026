import math as mp


num1 = int(input("Enter start number : "))
num2 = int(input("Enter end number : "))

for num in range( num1 , num2 + 1 ) :
    
    prime = True 

    for divisor in range( 2 , int(mp.sqrt(num)) + 1 ):

        if num % divisor == 0 :
            prime = False 
            break

    if prime == False :
        print( f"{num} Not Prime" )
    
    else :
        print( f"{num} Prime" )
    


