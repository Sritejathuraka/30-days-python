import numpy as np


numpyArray = np.array([2, 4, 8, 10])
#print("Multiply array", numpyArray * 2 )

numpyArray1 = np.array([[[4, 8, 10, 11],
                       [ 5, 7, 10, 12],
                       [ 15, 37, 1, 8]],
                       [[4, 8, 10, 11],
                       [ 5, 7, 10, 12],
                       [ 15, 37, 1, 8]]])


#print("numpyArray1 - shape", numpyArray1.shape)
#print("numpyArray1 - Dimen", numpyArray1.ndim)
#print("numpyArray1 - Datatype", numpyArray1.dtype)
#print("numpyArray1 - Size", numpyArray1.size)

a = np.array([[4, 8, 10],
              [6, 9, 1]])
b = np.array([[5, 9, 15],
              [2, 6, 16]])

#print("addition", a + b)
#print("Multiplication", a * b)
#print("Square of a", a ** 2)
#print("Square of b", b ** 2)

c = np.array([[[14, 6, 12],
              [16, 4, 8]]])

#print("DImension", c.ndim)
#print("Accessing elements in three dimensional array", c[0][0][1])

#print("Slicing three dimensional array", c[0][1][0:2] )

#print("Create Rows and colums with Zeros", np.zeros((2, 2)))
#print("Create Rows and colums with one's",np.ones((2, 3)))
#print("Arrange numbers",np.arange(0, 10, 2))
#print("Arrange line space",np.linspace(0, 1, 5))


c = np.array([[1, 2, 3], 
              [4, 5, 6]])
#print("Reshape of array",  c.reshape(3, 2))
#print("Flatten rows and coloms", c.flatten())
#print("Transpose",c.T)

arr = np.array([1, 2, 3, 4, 5, 7])
#print("Mean:", np.mean(arr))
#print("Median:", np.median(arr))
#print("Standard Deviation:", np.std(arr))


mat1 = np.array([[1, 2, 3], 
                 [0, 1, 4], 
                 [5, 6, 0]])
mat2 = np.array([[7, 8, 9], 
                 [2, 3, 4], 
                 [1, 0, 2]])

#print("Dot product:\n", np.dot(mat1, mat2))



