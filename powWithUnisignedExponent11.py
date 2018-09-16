#!/usr/bin/python
# -*- coding: utf8 -*-

# Invalid input exception class
class InvalidInput(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


# power function with non-negative exponent in the common method
def power_common(base, exponent):
    result = 1

    for i in range(exponent):
        result *= base

    return result


# power function with non-negative exponent in the fast method
def power_fast(base, exponent):
    if 0 == exponent:
        return 1
    elif 1 == exponent:
        return base
    else:
        result = power_fast(base, exponent >> 1)
        if exponent & 1:
            # odd integer
            return result * result * base
        else:
            # even integer
            return result * result


# Check if value (int/float) is zero
# parameters:
#   value - int type or float type
def is_zero(value):
    # Check the type that value belongs to
    if isinstance(value, float):
        # float type
        zero_limit = 1e-7
        return (value >= -zero_limit) and (value <= zero_limit)
    else:
        # int type
        return value == 0


# Generic interface for power function with integer exponent including positives, zero and negatives
# parameters:
#     method: 1 -- fast method; others -- common method
def power(base, exponent, method=0):
    # sign flag: positive(default)
    is_positive_exponent = True
    if exponent <= 0:
        if is_zero(base):
            raise InvalidInput(base)
        exponent = - exponent
        is_positive_exponent = False
    # computation result
    result = 0
    if 1 == method:
        result = power_fast(base, exponent)
    else:
        result = power_common(base, exponent)
    # check the sign of the exponent
    if not is_positive_exponent:
        result = 1.0 / result

    return result


def unitest():
    try:
        print("---------------- Power function in Fast Method Test ----------------")
        print("The result of -2^-3 is %f." % power(-2, -3, 1))
        print("The result of -2^3 is %f." % power(-2, 3, 1))
        print("The result of 2^-3 is %f." % power(2, -3, 1))
        print("The result of 2^3 is %f."% power(2, 3, 1))
        print("---------------- Power function in Common Method Test ----------------")
        print("The result of -2^-3 is %f." % power(-2, -3))
        print("The result of -2^3 is %f." % power(-2, 3))
        print("The result of 2^-3 is " % power(0, -3))
        print("The result of 2^3 is " % power(2, 3))
    except Exception as e:
        print("Invalid input exception happened: input %s with negative exponent" % e)

if __name__ == '__main__':
    unitest()