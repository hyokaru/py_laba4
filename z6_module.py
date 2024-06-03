def replace(lst, k, m):
    """
    Заменяет все элементы списка lst, отличающиеся от значения k, на значение m.
    :param lst: Список чисел.
    :param k: Значение, которое должно остаться неизменным.
    :param m: Значение, на которое будут заменены все остальные элементы.
    :return: Измененный список.
    """
    return [x if x == k else m for x in lst]
