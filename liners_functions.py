"""
Returns a list with the len of each string
:param lst: The list of strings
:return: New list of the lens
"""
str_len = lambda lst: list(map(len, lst))

"""
Return a list of the multiplied number
:param num: the number to multiply
:return: New list of the indexes of the to_find member in lst
"""
mul_table = lambda number: [i * number for i in range(1, number + 1)]
