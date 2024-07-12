import numpy as np

arr_test = [1, 2, 3]

def sum_numbers(spec_arr):

    if len(spec_arr) == 1:
        return spec_arr[0]

    return spec_arr[0] + sum_numbers(spec_arr[1:])

print(sum_numbers(arr_test))