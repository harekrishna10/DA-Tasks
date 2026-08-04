# 1) Import the NumPy library and print its version.
import numpy as np
print(np.__version__)


# 2) Create a NumPy array containing numbers from 1 to 10.
print(np.array(range(1,11)))


# 3) Create an array of all ones with shape (3,3).
print(np.ones(shape=(3,3)))


# 4) Create an identity matrix of size 5×5.
mat_array = np.identity(5)
print(mat_array)

# 5) Create an array of even numbers from 2 to 50.
array_even = np.array(range(2,51,2))
print(array_even)


# 6) Generate numbers from 10 to 100 with step size 5.
arr = np.arange(10,101,5)
print(arr)


# 7) Create a NumPy array from a Python list.
list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
numpy_array = np.array(list1)
print(numpy_array)

# 8) Find the shape of an array.
array2 = np.array([[[1,2,3,4,5],
                    [6,7,8,9,10],
                    [11,12,13,14,15],
                    [16,17,18,19,20]]])
array_shape = np.shape(array2)
array_size = np.size(array2)
array_dimention = np.ndim(array2)
print("Shape of an array:",array_shape,"Size of an array:", array_size, "Dimetion of an array:", array_dimention)


# 9) Find the datatype of array elements.
array3 = np.array([1,2,5,6,7])
print(array3.dtype)


# 10) Create a random array of size 10.
array4 = np.random.randint(100, size = 10)
print(array4)


# 11) Generate 10 random integers between 1 and 100.
random_int = np.random.randint(1,101, size = 10)
print(random_int)

# 12) Reshape an array of size 12 into (3,4).
array5 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("Original array:\n", array5)
reshape_array = array5.reshape(3,4)
print("Reshaped array:\n", reshape_array)


# 13) Flatten a 3×3 matrix into a 1D array.
matrix_3by3 = np.array([[1,2,3],
                       [4,5,6],
                       [7,8,9]])
flatten_array = matrix_3by3.flatten()
print("Original matrix:\n", matrix_3by3)
print("Flattened array:\n", flatten_array)


# 14) Create a 4×4 matrix filled with value 7.
matrix_4by4 = np.full((4,4),7)
print("4by4 matrix with value 7:\n",matrix_4by4)

# 15) Find the size (number of elements) of an array.
array_size = np.array([1,2,4,5,6,8,9])
print(np.size(array_size))


# 16) Create a diagonal matrix with diagonal values [1,2,3,4].
matrix1 = np.array([1,2,3,4])
print("Diagonal matrix is:\n",np.diag(matrix1))


# 17) Convert a float array into an integer array.
float_array = np.array([1.5, 2.3, 3.7, 4.9])
int_array = float_array.astype(int)
print("Float array:", float_array)
print("Integer array:", int_array)


# 18) Create an array with values between 0 and 1 using linspace().
linspace_array = np.linspace(0, 1, 10)
print("Linspace array:\n", linspace_array)

# 19) Reverse an array.
array6 = np.array([1,2,3,5,6,7,8])
print("Original array:\n", array6)
reverse = array6[::-1]
print("Reversed array:\n",reverse)


# 20) Sort an array in ascending order.
array7 = np.array([1,30, 5,90, 100, 2, 6, 4])
ascending = np.sort(array7)
print(ascending)


# 21) Find the maximum and minimum values in an array.
max_min_val = np.array([100,20,30,4,2,1,500,103393])
max_value = np.max(max_min_val)
min_value = np.min(max_min_val)
print("Max value is:", max_value)
print("Min value is:", min_value)


# 22) Find the index of maximum value.
number = np.array([100,20,30,4,2,1,500,103393])
max_index = np.argmax(number)
print("The index of Max value is:",max_index)


# 23) Find the index of minimum value.
number = np.array([100,20,30,4,2,1,500,103393])
min_index = np.argmax(number)
print("The index of Min value is:",min_index)


# 24) Create a 2×3 matrix and print its transpose.
matrix2 = np.array([[1,2,3],
                    [4,5,6]])
print("Original matrix is :\n", matrix2)
transpose_matrix = np.transpose(matrix2)
print("The transpose matrix is:\n",transpose_matrix)


# 25) Concatenate two arrays.
arrays1 = np.array([1,2,3,4])
arrays2 = np.array([5,6,7,8])
concatenate_array = arrays1 + arrays2
print("Concatenate array is:",concatenate_array)

# 26) Split an array into 3 equal parts.
arrays3 = np.array([1,2,3,4,5,6,7,8,9])
split_array = np.split(arrays3, 3)
print("Split array is:\n", split_array)


# 27)Multiply two arrays element-wise.
mul_arr1 = np.array([1,2,3,4])
mul_arr2 = np.array([5,6,7,8])
print("Original arrays are:\n", mul_arr1, "\n", mul_arr2)
array_mul_result = mul_arr1 * mul_arr2
print("multiplication result is:", array_mul_result)


# 28) Calculate square root of array values.
array8 = np.array([1,4,9,16,25])
sqrt_array = np.sqrt(array8)
print("Square root of array:", sqrt_array)


# 29) Find exponential values of array elements.
arr = np.array([1,2,3,4])
exp_array = np.exp(arr)
print("Exponential values of array:", exp_array)


# 30) Find logarithm of array elements.
arr2 = np.array([1,2,3,4,5])
arr_log = np.log(arr2)
print("Array using log:", arr_log)


# 31) Compute sum of all elements in an array.
arr3 = np.array([1,2,3,4,5,6,7])
arr_sum = np.sum(arr3)
print("Sum of all element is:",arr_sum)


# 32) Compute median of array values.
arr4 = np.array([1,2,3,4,5,6,7])
arr_median = np.median(arr4)
print("Median of array is:", arr_median)

# 33) Compute standard deviation.
arr5 = np.array([1,4,7,9,12,14,15])
arr_sd = np.std(arr5)
print("Standard deviation is:", arr_sd)


# 34) Compute variance.
arr_var = np.var(arr5)
print("Variance is :", arr_var)


# 35) Find cumulative sum of elements.
arr6 = np.array([1,2,3,4,5,6,7,8,9])
cum_sum = np.cumulative_sum(arr6)
print("Cummulative sum is:", cum_sum)


# 36) Find cumulative product of elements.
cum_product = np.cumulative_prod(arr6)
print("Cummulative product is:", cum_product)


# 37) Round decimal values to 2 decimal places.
arr7 = np.array([1.2345, 2.3456, 3.4567, 4.5678])
arr_round = np.round(arr7,2)
print("Rounded decimal value with 2 is:", arr_round)


# 38) Find absolute values of negative numbers.
neg_number = -100
abosute_val = np.abs(neg_number)
print("Absolute value of negative number is:", abosute_val)


# 39) Replace all negative values with zero.
arr8 = np.array([1,2,3,-4,-100,5,8, -8])
rep_neg = np.where(arr8 < 0, 0, arr8)
print("Replace all negative number with zero:", rep_neg)


# 40) Extract last 5 elements from an array.
arr10 = np.array([1,2,3,4,5,6,7,8,9])
last_5_eleement = arr10[-5:]
print("Last five eleement of array is:", last_5_eleement)


# 41) Reverse an array using slicing.
arr11 = np.array([1,2,3,4,5,6,7,8,9,10])
arr_slice = arr11[2:6]
print("Array sliced:", arr_slice)
rev_slice_array = arr_slice[::-1]
print("Reversed slice arry is :", rev_slice_array)


# 42) Access a specific column in a matrix.
matrx12 = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print("Original Matrix:\n", matrx12)
access_colm = matrx12[:, 1:2]
print("Accessed column of matrisx is:\n", access_colm)


# 43) Extract a submatrix from a 5×5 matrix.
matrx13 = np.array([[1,4,5,6,7],
                    [2,4,5,3,6],
                    [6,7,8,4,6],
                    [5,7,7,3,7],
                    [5,3,5,7,2]])
print("Original Matrix is:\n", matrx13)
sub_matrix = matrx13[:, 2:4]
print("Sub Matrix is:\n", sub_matrix)


# 44) Replace the third element with value 100.
arr22 = np.array([10,2,34,466,500,190,5,3])
print("Original array is:", arr22)
arr22[2] = 100
print("Replace 3rd element with 100 is:\n",arr22)


# 45) Find indices of elements greater than 50.
arr23 = np.array([1,45,68,92,6,76,12,50])
indices_element = np.where(arr23 > 50)
print("Indices of element greater than 50 is:", indices_element)


# 46) Multiply two matrices element-wise.
matrix11 = np.array([[1,2,3,4],
                    [5,6,7,8]])
matrix22 = np.array([[4,3,2],
                     [6,5,4],
                     [9,8,7],
                     [12,56,23]])
matrx_mul = np.dot(matrix11,matrix22)
print("Matrix multiplication is:\n", matrx_mul)


# 47) Find inverse of a matrix.
matrx10 = np.array([[1,20,3],
                  [4,50,6],
                  [70,8,90]])
inv_mtrx = np.linalg.inv(matrx10)
print("inverse matrix is:\n", inv_mtrx)


# 48) Find eigenvalues of a matrix.
matrxs = np.array([[1,2,4],
                   [6,5,7],
                   [8,9,3]])
eigenv_matrx = np.linalg.eigvals(matrxs)
print("The eigenvalues of matrix is:", eigenv_matrx)


# 49) Find eigenvectors of a matrix.
eigenvects_matrx = np.linalg.eig(matrxs)
print("The eigenvectors of matrix is:\n", eigenvects_matrx)

# 50) Compute matrix rank.
matrx_rank = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9]])
rank = np.linalg.matrix_rank(matrx_rank)
print("The rank of matrix is:", rank)


# 51) Create a random 4×4 matrix and find row sums.
matrx_random = np.random.rand(4,4)
print("Random 4 by 4 matrix is:\n",matrx_random)
row_sum = np.sum(matrx_random, axis=1)
print("Sum of random 4 by 4 matrix row wise is :", row_sum)

rand_4by4 = np.random.rand(4,4)
print("Random 4 by 4 matrix is:\n",rand_4by4)
row_sum = np.sum(rand_4by4, axis=1)
print("Sum of random 4 by 4 matrix row wise:\n", row_sum)


# 52) Find row-wise maximum values.
matrix0 = np.array([[1,2,3],
                    [70,98,77],
                    [123,0,14]])
row_max_val = np.max(matrix0, axis=1)
print("Maximum value row wise:", row_max_val)


# 53) Generate a random array and normalize it between 0 and 1.
random_array = np.random.rand(10)
print("Random array is:\n", random_array)
normalized_array = (random_array - np.min(random_array)) / (np.max(random_array) - np.min(random_array))
print("Normalized array is:\n", normalized_array)

# 54) Find common elements between two arrays.
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
common_elements = np.intersect1d(arr1, arr2)
print("Common elements between two arrays is:", common_elements)


# 55) Convert a 1D array into a 3D array.
arr_1d = np.arange(1,25)
print("Random array iss:",arr_1d)
arr_3d = arr_1d.reshape(2,3,4)
print("Reshaped 3d array is:\n", arr_3d)

