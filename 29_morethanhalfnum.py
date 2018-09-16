def MoreThanHalfNum_Solution(numbers):
    if not numbers:
        return 0
    checkNum = numbers[0]
    count = 1
    for n in numbers[1:]:
        if n == checkNum or count == 0:
            count += 1
            checkNum = n
        else:
            count -= 1
    # 验证部分
    if count > 0:
        count = 0
        for n in numbers:
            if n == checkNum:
                count += 1
        return checkNum if count*2>len(numbers) else 0
    else:
        return 0

list1=[1,2,2,2,3,3,4]
print(MoreThanHalfNum_Solution(list1))