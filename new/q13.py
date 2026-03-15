import numpy as np

# Create two 3×3 matrices with random integers between 1 and 10
A = np.random.randint(1, 11, (3,3))
B = np.random.randint(1, 11, (3,3))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
addition = A + B
print("\nA + B:")
print(addition)

# Element-wise Multiplication
elementwise = A * B
print("\nElement-wise Multiplication (A * B):")
print(elementwise)

# Dot Product
dot_product = np.dot(A, B)
print("\nDot Product of A and B:")
print(dot_product)

# Determinant of Matrix A
det_A = np.linalg.det(A)
print("\nDeterminant of A:")
print(det_A)