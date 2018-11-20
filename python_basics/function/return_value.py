def sum_num(n1, n2):
    return n1 + n2


print(sum_num(2, 3))
print(sum_num(10, 5))


def is_metro(city):
    lst = ['sfo', 'la', 'nyc']
    if city in lst:
        return True
    else:
        return False


print(is_metro('Tx'))