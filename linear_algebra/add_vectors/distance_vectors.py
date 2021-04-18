import math
from linear_algebra.add_vectors import vectors 


# sum of conponentwise of vectors 
def dot(v, w):
    '''v_1 * w_1 + ... + v_n * w_n'''
    return sum(v_i * w_i 
                for v_i, w_i in zip(v, w))

# a vector's sum of squares 
def sum_of_squares(v):
    '''v_1 * v_1 + ... + v_n * v_n'''
    return(dot(v,v))

#length of a vector 
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# distance between two vectors 
def squared_distance(v,w):
    '''(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2'''
    return sum_of_squares(vectors.vector_subtract(v, w))

a = [1, 2] # 1st vector 
b = [3, 4] # 2nd vector 

# test_dot = dot(a, b)
# print(type(test_dot))
# print(test_dot)

# test_sum = sum_of_squares(b)
# print(test_sum)

# test_magnitude = magnitude(b)
# print(test_magnitude)

test_squared_distance = squared_distance(b, a)
print(test_squared_distance)
