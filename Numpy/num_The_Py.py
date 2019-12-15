import numpy as np 

# arrays in Numpy hold one type of data
np.array([1, 2, 3, 4])

# numpy arrays can be multidimensional
original_list = [[1,2,3],[3,4,5],[6,7,8]]
two_dimensional_array = np.array(original_list)
    # setting multidimensional arrays manualy   
# An array of length 10, filled with 0:
np.zeros(10, dtype=int)
# An array of size 3x5 filled with 1.0 (float)
np.ones((3, 5), dtype=float)
# An array of size 3x5 filled with 3.14
np.full((3, 5), 3.14)
# An array containing a linear sequence starting at 0 and 
# going up to 20, with steps of 2
np.arange(0, 20, 2)
# An array of 5 numbers, linearly spaced between 0 and 1
np.linspace(0, 1, 5)
# An array of the given shape and populate it with random
# samples. You can also try using "randint" and "normal"
np.random.random((3, 3))
# The identity matrix of size 3
np.eye(3)