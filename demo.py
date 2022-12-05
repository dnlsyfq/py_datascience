import numpy as np

python_list = list(range(5))
numpy_array = np.array(range(5))
print(python_list)
print(numpy_array)

inclusive_begin = 3
exclusive_end = 10
print(np.arange(inclusive_begin, exclusive_end))

size = (1, 2, 3) # Could also be (1, 2) or (4, 3, 2, 1, ...), etc.
print(np.random.random_sample(size=size))

size = (1, 2) # Could also be (1, 2) or (4, 3, 2, 1, ...), etc.
print(np.random.random_sample(size=size))

print(np.random.random_sample())