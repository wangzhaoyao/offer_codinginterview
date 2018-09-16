#!/usr/bin/python
# -*- coding: utf8 -*-

# Define ParamError Exception
class ParamError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


# Find the minimum in rotated array
def min_in_rotated_array(data, length):
    if data is None or length <= 0:
        raise ParamError("Error: input parameters exception!")
    # Index initialization
    sta, mid, end = 0, 0, length-1
    # Ensure this requisite before binary search
    while data[sta] >= data[end]:
        if end - sta == 1:
            mid = end
            break
        # Get the middle index
        mid = (sta + end) // 2
        # Find the minimum in order
        if (data[sta] == data[mid]) and (data[mid] == data[end]):
            minimum = data[sta]
            for i in range(sta+1, end+1):
                if minimum > data[i]:
                    minimum = data[i]
            return minimum

        if data[sta] <= data[mid]:
            sta = mid
        elif data[end] >= data[mid]:
            end = mid

    return data[mid]


def unitest():
    arr1 = [3, 4, 5, 1, 2]
    arr2 = [1, 0, 1, 1, 1]
    arr3 = [1, 1, 1, 0, 1]
    arr4 = [1, 2, 3, 4, 5]

    print("The minimum of the rotated array [3, 4, 5, 1, 2] is %d." % min_in_rotated_array(arr1, 5))
    print("The minimum of the rotated array [1, 0, 1, 1, 1] is %d." % min_in_rotated_array(arr2, 5))
    print("The minimum of the rotated array [1, 1, 1, 0, 1] is %d." % min_in_rotated_array(arr3, 5))
    print("The minimum of the rotated array [1, 2, 3, 4, 5] is %d." % min_in_rotated_array(arr4, 5))

    try:
        min_in_rotated_array(arr1, -2)
    except :
        print ("Function call: min_in_rotated_array(arr1, -2)")


if __name__ == '__main__':
    unitest()