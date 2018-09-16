#!/usr/bin/python
#-*- coding: utf8 -*-

def print_n_digits(n, method=0):
    if n <= 0:
        print("ERROR: Illegal parameters n <= 0!")
        return
    if method == 1:
        print("\nUse the recursive method to print the numbers from 1 to maximum n digits: ")
        string = ["0" for i in range(n)]
        print_n_digits_recursive(string, n, 0)
    else:
        print("\nSimulate the self incrementation of the integer: ")
        print_n_digits_simulation(n)


# Use the recursive method to print
def print_n_digits_recursive(string, length, start):
    if length == start:
        output = remove_leading_zeros("".join(string))
        if output != '0':
            print(output)
        return

    for i in range(0,10):
        string[start] = repr(i)
        print_n_digits_recursive(string, length, start+1)


# Use the simulation method to print
def print_n_digits_simulation(n):
    max_num = '9' * n
    curr_num = '1'
    while True:
        print(curr_num)
        next_num = increment_by_one(curr_num)  # add by 1 function: i += 1
        # Check if next_num > max_num
        if compare(next_num, max_num) > 0:  # compare function: i > , <, or == some_number
            break
        else:
            curr_num = next_num


def remove_leading_zeros(num):
    i = 0
    for ch in num[:-1]:
        if '0' == ch:
            i += 1
        else:
            break
    return num[i:]


# Compare two digits string
def compare(num_1, num_2):
    result = 0

    real_num_1 = remove_leading_zeros(num_1)
    real_num_2 = remove_leading_zeros(num_2)
    len_1 = len(real_num_1)
    len_2 = len(real_num_2)

    if len_1 == len_2:
        if real_num_1 > real_num_2:
            result = 1
        elif real_num_1 < real_num_2:
            result = -1
        else:
            result = 0
    else:
        if len_1 > len_2:
            result = 1
        else:
            result = -1
    return result

print(compare('11110','9999'))



def check_digits_string(num):
    is_legal = True

    # Check if the input num string is legal or not
    # Check the type
    if not isinstance(num, str):
        is_legal = False
        print("Input param is not str type!")
    # Check the length
    num_length = len(num)
    if num_length <= 0:
        is_legal = False
        print('Illegal String: null str')
    # Check the characters contained
    legal_chars = set([repr(i) for i in range(10)])
    for ch in num:
        if ch not in legal_chars:
            print("Input number string includes non-digit character")
            is_legal = False
            break

    return is_legal


def increment_by_one(num):
    next_ = ''
    num = remove_leading_zeros(num)
    # First, check that it is a legal input number string.
    if not check_digits_string(num):
        return next_
    # The effective length of num
    num_length = len(num)
    # The Least Significant Bit
    #carry = False
    char_code = ord(num[-1]) + 1
    out_seq, index = [], 0
    for i in range(num_length-2, -1, -1):
        if char_code > ord('9'):  #ord() 它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值
            #carry = True
            out_seq.append('0')
        else:
            out_seq.append(chr(char_code)) #chr()函数用一个范围在range（256）内的（就是0～255）整数作参数，返回一个对应的字符
            index = i + 1
            break
        # Process the case with carry
        char_code = ord(num[i]) + 1
        #carry = False

    # Reverse the output sequence
    out_seq.reverse()
    next_ = ''.join(out_seq)
    if char_code > ord('9'):
        next_ = '10' + next_    # Overflow
    elif index == 0:
        next_ = chr(char_code) + next_
    else:
        next_ = num[:index] + next_
    return next_


def unitest():
    n = 4
    print_n_digits(n, 1)  # recursive method
    print_n_digits(n, 0)  # simulation method
'''
if __name__ == '__main__':
    unitest()
'''