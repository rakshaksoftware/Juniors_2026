import numpy as np 

np.random.seed( 42 )

arr = np.random.normal( loc = 50 , scale = 5 , size = 1000 ) 

print(arr)

mean = np.mean( arr ) 

print( mean ) 

median = np.median( arr ) 

print( median ) 

std_dvn = np.std( arr ) 

print( std_dvn ) 

variance = np.var( arr ) 

print( variance ) 

p25 = np.percentile( arr , 25 ) 
p75 = np.percentile( arr , 75 ) 

print( f"25th percentile is : {p25} " )
print( f"75th percentile is : {p75} " )


