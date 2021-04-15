def add_vector(a, b):
      return [a_i + b_i
              for a_i, b_i in zip(a,b)]

def vector_sum(my_list_vector):
      result = my_list_vector[0]
      for my_list in my_list_vector[1:]:
            result = add_vector(result, my_list)
      return result

a = [1,2,3,4]
b = [5,6,7,8]
c = [9,1,2,3]
d = [4,5,6,7]

my_list_vector = [a,b,c,d]

test = vector_sum(my_list_vector)
print(type(test))
print(test)