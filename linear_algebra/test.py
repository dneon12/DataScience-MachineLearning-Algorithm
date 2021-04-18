from functools import reduce
 
v = [1,2,3,4]
w = [6,7,8,9]

a = sum(v_i*w_i for v_i, w_i in zip(v, w))

print(a)

