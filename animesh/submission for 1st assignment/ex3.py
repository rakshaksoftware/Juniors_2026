import numpy as np

np.random.seed( 42 ) 

a = np.random.randint( 1 , 11 , ( 3 , 3 ) ) 
b = np.random.randint( 1 , 11 , ( 3 , 3 ) )

print( a )

print( "\n----" ) 

print( b )

print( "\n-----" )

s = a + b

# prints the sum 
print( s )
print( "\n----" ) 

p = a * b

#prints the prodcut 
print( p ) 
print( "\n----" ) 

d = np.dot( a , b ) 

#prints dot product 
print( d ) 
print( "\n----" ) 

det_A = np.linalg.det( a ) 

#prints the determinant of matrix A 
print( det_A ) 