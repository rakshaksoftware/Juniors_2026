print("Solution for Question 1.1")
for i in range(1,100):
 if i%3==0 and i%5==0:
  print("Fizzbuzz")
 elif i%3==0:
  print("Fizz")
 elif i%5==0:
  print("Buzz")
 else :
  print(i)
  

print("\nSolution for Question 1.2")
a=int(input("first number:"))
b=int(input("second number:"))

for i in range(a,b+1):
 for j in range(2,i):
      if i%j==0:
        break
      else:
       print(i)


print("\nSolution for Question 2.1")
import numpy as np
A=np.random.randint(1,10,9).reshape(3,3)
B=np.random.randint(1,10,9).reshape(3,3)
print("A:\n",A)
print("B:\n",B)
add=A+B
element_product=A*B
dot_product=np.dot(A,B)
det_A=np.linalg.det(A)
print("Addition:\n",add)
print("Element Product:\n",element_product)
print("Dot Product:\n",dot_product)
print("Determinant of A:\n",det_A)


print("\nSolution for Question 2.2")
import numpy as np
arr1=np.random.normal(50,5,1000)
print(arr1)
print("Mean:",arr1.mean())
print("Median:",np.median(arr1)) 
print("Standard deviation:",arr1.std()) 
print("Variance:",arr1.var())
print("25 percentile:",np.percentile(arr1,25))
print("75 percentile:",np.percentile(arr1,75))


print("\nSolution for Question 3")
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10)
y=x**2
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Line plot")
plt.plot(x,y)
plt.grid()
plt.show()


m=np.random.uniform(0,1,100)
n=np.random.normal(0.5,1,100)
plt.scatter(m,n)
plt.title("Scatter plot")
plt.show()

p=np.random.exponential(0.5,500)
plt.hist(p)
plt.title("Histogram")
plt.show()


print("\nSolution for Question 4")
import numpy as np
import pandas as pd
data={'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan'],
        'Age': [28, 34, 25, 42, 30],
        'Salary': [70000, 80000,50000, 110000,75000]}
a=pd.DataFrame(data)
print(a)
a['Tax']=0.2*a['Salary']
print("\nWith Tax:\n",a)
a1=a[a['Age']>=30]
print(a1)
print("\nThe average salary is=",a[a['Age']<30]['Salary'].mean())
a2=a.sort_values('Salary',ascending=False)
print("\nSorted data:\n",a2)


print("Solution for Question 5")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates=pd.date_range(start='2025-01-01',end='2025-01-31')
days=np.arange(len(dates))
temperature= 15 + 10 * np.sin(2 * np.pi * days / 31)
df = pd.DataFrame({
    'Date': dates,
    'Temperature': temperature
})
print(df)
plt.plot(df['Date'],df['Temperature'],label='Temperature')
plt.xticks(rotation=45)
plt.title("Temperature")
plt.show()
df["rolling_avg"]=df["Temperature"].rolling(window=7).mean()
plt.plot(df['Date'],df['Temperature'],label='Temperature')
plt.plot(df['Date'],df['rolling_avg'],label="Rolling average")
plt.xticks(rotation=45)
plt.title("Temperature and 7 day avg of rolling temperature")
plt.legend()
plt.show()

d1=df[df['Temperature']>20]
print("Days when the temperature was above 20:\n",d1['Date'])
