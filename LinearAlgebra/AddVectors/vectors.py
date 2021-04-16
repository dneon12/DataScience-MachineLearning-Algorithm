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

# function using reduce() for add list vectors 
def vector_sum_1(my_list):
      return reduce(add_vector, my_list)

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,1,2,3]
d = [4,5,6,7]

my_list_vector = [a,b,c,d]

# test = vector_sum(my_list_vector)
# print(type(test))
# print(test)

# test_vector_sum_1 = vector_sum_1(my_list_vector)
# print(type(test_vector_sum_1))
# print(test_vector_sum_1)
