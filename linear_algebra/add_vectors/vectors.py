from functools import *

# function for add 2 vectors 
def add_vector(a, b):
      '''adds corresponding elements'''
      return [a_i + b_i
              for a_i, b_i in zip(a,b)]

# function for add list vectors 
def vector_sum(my_list):
      '''sums all corresponding elements'''
      result = my_list[0]
      for my_list in my_list[1:]:
            result = add_vector(result, my_list)
      return result

# subtraction 2 vectors 
def vector_subtract(v, w):
      ''' subtracts corresponding elements'''
      return [v_i - w_i 
                  for v_i, w_i in zip(v, w)]

# function using reduce() for add list vectors 
def vector_sum_1(my_list):
      return reduce(add_vector, my_list)

# funtion multiply a vector by a scalar 
def scalar_multiply(c, v):
      ''' c is number, v is a vector'''
      return [c * v_i for v_i in v]

def vector_mean(vectors):
      '''compute the vector whose ith element is the mean of the ith elements of the input vectors'''
      n = len(vectors)
      return scalar_multiply(1/n, vector_sum(vectors))


a = [1,2,3,4]
b = [5,6,7,8]
c = [9,1,2,3]
d = [4,5,6,7]

my_list_vector = [a,b]

# test = vector_sum(my_list_vector)
# print(type(test))
# print(test)

# test_vector_sum_1 = vector_sum_1(my_list_vector)
# print(type(test_vector_sum_1))
# print(test_vector_sum_1)

# test_scalar_multiply = scalar_multiply(2, a)
# print(test_scalar_multiply)

test_vector_mean = vector_mean(my_list_vector)
print(test_vector_mean)