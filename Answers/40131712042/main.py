import numpy as np
import self
from scipy.sparse import csr_matrix
import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5

arr = np.array(list(map(int, input("Enter numbers for array1:").split())))
#Find The Missing Number
print("The missing number is:", t1(arr))

#Rotate Array:
k = int(input("enter k:"))
R = t2(arr, k)
print("rotated array: ", R)
#Remove Duplicates From Sorted Array:
newLength = t3(arr)
print("New :", newLength)
# Merge Sorted Array:
arr2 = np.array(list(map(int, input("Enter numbers for array 2:").split())))
t4(arr, len(arr), arr2, len(arr2))
print("Merged sorted array: ", arr)
# Maximum Subarray Sum:
print("maximum subarray sum:", t5)

class SparseMatrix :
   def __init__(self, matrix):
       self.sparse_matrix = self.convert_to_sparse(matrix)
   def convert_to_sparse(self, matrix):
       sparse_matrix = []
       for i, row in enumerate(matrix):
           for j, val in enumerate(row):
               if val != 0:
                   sparse_matrix.append((i, j, val))
       return sparse_matrix
   def transpose(self):
       transposed_matrix = []
       for j in range(len((self.sparse_matrix[0][1]))):
           transposed_row = []
           for i in range(len((self.sparse_matrix))):
               if self.sparse_matrix[i][1] == j:
                   transposed_row.append((self.sparse_matrix[i][1], self.sparse_matrix[i][0], self.sparse_matrix[i][2]))
           transposed_matrix.append(transposed_row)
       return transposed_matrix
   def change_element(self, address, new_val):
       for i, element in enumerate(self.sparse_matrix):
           if(element[0], element[1]) == address:
               self.sparse_matrix[i] = (address[0], address[1, new_val])
               break
   def __str__ (self):
       return str(self.sparse_matrix)


normalMatrix = np.matrix(input("enter nums: "))
sparse_obj = SparseMatrix(normalMatrix)
print("sparse matrix:")
print(sparse_obj)
#Transpose the matrix
transposed_matrix = sparse_obj.transpose()
print("\nTransposed Sparse Matrix:")
print(transposed_matrix)
#change an element
sparse_obj.change_element((0,1),5)
print("\n Sparse Matrix after changing element :")
print(sparse_obj)
