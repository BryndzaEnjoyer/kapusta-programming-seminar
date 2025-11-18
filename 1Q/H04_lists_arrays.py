import numpy as np
import time
import random


def create_list_and_array():
    """
    Creates a simple Python list and converts it into a NumPy array.

    This function demonstrates the difference between a built-in Python list
    and a NumPy array by constructing both and returning them.

    Returns
    -------
    tuple
        A tuple (lsd, als) where:
        - lsd is a Python list of integers.
        - als is a NumPy array created from that list.
    """
    lsd = [1, 2, 3, 4, 5]
    als = np.array(lsd)
    print(type(lsd), lsd,"\n", type(als), als)
    return lsd, als


def indexing_and_slicing(nums_list):
    """
    Performs basic indexing and slicing on a list and its NumPy array version.

    Parameters
    ----------
    nums_list : list
        The input list from which a NumPy array is created.

    Returns
    -------
    dict
        A dictionary containing results of indexing and slicing for both
        the original list and the NumPy array.
    """
    nums_array = np.array(nums_list)
    return {
        "list_second": nums_list[1],
        "list_last": nums_list[-1],
        "array_second": nums_array[1],
        "array_last": nums_array[-1],
    }


def multiply_demo(list_a):
    """
    Demonstrates how Python lists and NumPy arrays behave differently
    when multiplied by a number.

    Parameters
    ----------
    list_a : list
        A list of numbers used for comparison.

    Returns
    -------
    tuple
        A tuple (list_result, array_result) containing:
        - list_result : result of list_a * 2 (repetition)
        - array_result : elementwise multiplication using NumPy
    """
    array_a = np.array(list_a)
    return list_a * 2, array_a * 2


def elementwise_operations(list_a, list_b):
    """
    Demonstrates list concatenation vs NumPy elementwise addition.

    Parameters
    ----------
    list_a : list
        First list of numbers.
    list_b : list
        Second list of numbers.

    Returns
    -------
    tuple
        A tuple (list_addition, array_addition) where:
        - list_addition is list concatenation
        - array_addition is NumPy elementwise addition
    """
    array_a = np.array(list_a)
    array_b = np.array(list_b)
    return list_a + list_b, array_a + array_b


def conversions_demo(my_list, my_array):
    """
    Converts a list into a NumPy array and a NumPy array into a list.

    Parameters
    ----------
    my_list : list
        List to convert into a NumPy array.
    my_array : numpy.ndarray
        Array to convert into a Python list.

    Returns
    -------
    tuple
        A tuple (list_to_array, array_to_list)
    """
    return type(np.array(my_list)), np.array(my_list), type(list(my_array)),list(my_array)


def numpy_functions_demo(nums):
    """
    Demonstrates basic NumPy functions: sum, mean, and square root.

    Parameters
    ----------
    nums : list
        A list of numbers to convert into a NumPy array.

    Returns
    -------
    dict
        Results from NumPy operations: sum, mean, and sqrt.
    """
    arr = np.array(nums)
    return {
        "sum": np.sum(arr),
        "mean": np.mean(arr),
        "sqrt": np.sqrt(arr)
    }


def performance_test(n=1_000_000):
    """
    Compares performance of squaring numbers in a list vs a NumPy array.

    Parameters
    ----------
    n : int, optional
        Number of elements to test with. Default is 1,000,000.

    Returns
    -------
    dict
        Execution times for list and NumPy array operations.
    """
    L = list(range(n))
    A = np.array(L)

    start = time.time()
    sum_L = sum([x * x for x in L])
    list_time = time.time() - start

    start = time.time()
    sum_A = np.sum(A * A)
    array_time = time.time() - start

    return {"list_time": list_time, "array_time": array_time}


def twod_array_demo():
    """
    Demonstrates working with a 2D Python list and a NumPy 2D array.

    Returns
    -------
    dict
        A dictionary containing:
        - list_element : element from Python nested list
        - array_element : element from NumPy 2D array
        - transpose : transposed version of the NumPy 2D array
    """
    list_2d = [[1, 2], [3, 4]]
    array_2d = np.array([[1, 2], [3, 4]])

    return {
        "list_element": list_2d[1][1],
        "array_element": array_2d[1, 1],
        "transpose": array_2d.T
    }


def bonus_random_operations(b=10):
    """
    Performs a collection of random NumPy operations as a bonus exercise.

    Parameters
    ----------
    b : int, optional
        Length of the random arrays to generate. Default is 10.

    Returns
    -------
    dict
        Contains multiple results such as:
        - concatenated digits
        - array with modified element
        - random binary array
        - math-transformed array
        - sum of array
        - doubled array
    """
    arr = np.array([random.randint(1, 10) for _ in range(b)])

    first_half = "".join(str(arr[i]) for i in range(b // 2))

    arr_modified = arr.copy()
    arr_modified[3] = np.max(arr_modified)

    arr01 = np.array([random.randint(0, 1) for _ in range(b)])

    arrm = (arr + 5) * 3
    arms = np.sum(arr)
    arre = arr * 2

    return {
        "first_half": first_half,
        "modified": arr_modified,
        "binary": arr01,
        "math_array": arrm,
        "sum": arms,
        "double": arre
    }
    
    
nums = [1, 2, 3, 4, 5]
nums_list=[10, 20, 30, 40, 50]
list_a = [1, 2, 3]
list_b = [4, 5, 6]
array_b=np.array(list_b)

#create_list_and_array()
#print(indexing_and_slicing(nums_list)) 
#print(multiply_demo(list_a))
#print(elementwise_operations(list_a, list_b))
#print(conversions_demo(list_a, array_b))
#print(numpy_functions_demo(nums))
#print(performance_test(n=1_000_000))
#print(twod_array_demo())
#print(bonus_random_operations(b=10))