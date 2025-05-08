# Custom implementations of list methods

def my_append(lst, item):
    lst += [item]


def my_clear(lst):
    del lst[:]


def my_count(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count


def my_extend(lst, other):
    for item in other:
        lst += [item]


def my_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    raise ValueError("Value not found")


def my_pop(lst, index=-1):
    value = lst[index]
    del lst[index]
    return value



def my_remove(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            del lst[i]
            return
    raise ValueError("Value not found")


def my_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
