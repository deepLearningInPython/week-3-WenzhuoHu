import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.


# Task 1: Compute Output Size for 1D Convolution
# Instructions:
# Write a function that takes two one-dimensional numpy arrays (input_array, kernel_array) as arguments.
# The function should return the length of the convolution output (assuming no padding and a stride of one).
# The output length can be computed as follows:
# (input_length - kernel_length + 1)

# Your code here:
# -----------------------------------------------

def compute_output_size_1d(input_array, kernel_array):
    input_length = len(input_array)
    kernel_length = len(kernel_array)
    output_length = input_length - kernel_length + 1
    return output_length


# -----------------------------------------------
# Example:
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(compute_output_size_1d(input_array, kernel_array))


# Task 2: 1D Convolution
# Instructions:
# Write a function that takes a one-dimensional numpy array (input_array) and a one-dimensional kernel array (kernel_array)
# and returns their convolution (no padding, stride 1).

# Your code here:
# -----------------------------------------------

def convolve_1d(input_array, kernel_array):
    # Tip: start by initializing an empty output array (you can use your function above to calculate the correct size).
    # Then fill the cells in the array with a loop.
    pass

def convolve_1d(input_array, kernel_array):
    input_length = len(input_array)
    kernel_length = len(kernel_array)
    output_length = input_length - kernel_length + 1
    output_array = np.zeros(output_length)
    
    # Perform convolution
    for i in range(output_length):
        # Extract the relevant slice from the input array
        input_slice = input_array[i:i+kernel_length]
        
        # Compute the convolution at this position (element-wise multiplication and sum)
        output_array[i] = np.sum(input_slice * kernel_array)
    
    return output_array

# -----------------------------------------------
# Another tip: write test cases like this, so you can easily test your function.
input_array = np.array([1, 2, 3, 4, 5])
kernel_array = np.array([1, 0, -1])
print(convolve_1d(input_array, kernel_array))

# Task 3: Compute Output Size for 2D Convolution
# Instructions:
# Write a function that takes two two-dimensional numpy matrices (input_matrix, kernel_matrix) as arguments.
# The function should return a tuple with the dimensions of the convolution of both matrices.
# The dimensions of the output (assuming no padding and a stride of one) can be computed as follows:
# (input_height - kernel_height + 1, input_width - kernel_width + 1)

# Your code here:
# -----------------------------------------------

import numpy as np

def compute_output_size_2d(input_matrix, kernel_matrix):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel_matrix.shape
    
    # Calculate the output dimensions
    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1
    
    return (output_height, output_width)

# Example usage:
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel_matrix = np.array([[1, 0], [0, -1]])
print(compute_output_size_2d(input_matrix, kernel_matrix))  # Output: (2, 2)



# -----------------------------------------------


# Task 4: 2D Convolution
# Instructions:
# Write a function that computes the convolution (no padding, stride 1) of two matrices (input_matrix, kernel_matrix).
# Your function will likely use lots of looping and you can reuse the functions you made above.

# Your code here:
# -----------------------------------------------

def convolute_2d(input_matrix, kernel_matrix):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel_matrix.shape
    
    # Calculate output dimensions
    output_height = input_height - kernel_height + 1
    output_width = input_width - kernel_width + 1
    
    # Initialize the output matrix
    output_matrix = np.zeros((output_height, output_width))
    
    # Perform 2D convolution using nested loops
    for i in range(output_height):
        for j in range(output_width):
            # Extract the relevant slice from the input matrix
            input_slice = input_matrix[i:i+kernel_height, j:j+kernel_width]
            
            # Compute the convolution at this position (element-wise multiplication and sum)
            output_matrix[i, j] = np.sum(input_slice * kernel_matrix)
    
    return output_matrix

# Example usage:
input_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
kernel_matrix = np.array([[1, 0], [0, -1]])
print(convolute_2d(input_matrix, kernel_matrix))



# -----------------------------------------------