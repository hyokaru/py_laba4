def num_sum(num):
    """
    Вычисляет сумму цифр числа.

    :param num: Целое число.
    :return: Сумма цифр числа.
    """
    return sum(int(digit) for digit in str(abs(num)))

def max_sum(nums):
    """
    Находит число с максимальной суммой цифр в списке чисел.

    :param nums: Список целых чисел.
    :return: Число с максимальной суммой цифр.
    """
    if not nums:
        return None
    return max(nums, key=num_sum)
