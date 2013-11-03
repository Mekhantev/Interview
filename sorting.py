def merge(la: list, lb: list):
    lb_i = 0
    la_i = 0
    la_end = len(la) - 1
    while la_i <= la_end:
        while lb[lb_i] < la[la_i]:
            la.insert(la_i, lb[lb_i])
            lb_i += 1
            la_i += 1
            la_end += 1
        la_i += 1
    lb_end = len(lb)
    while lb_i < lb_end:
        la.append(lb[lb_i])
        lb_i += 1


def sort_strings_by_anagram(strings: list) -> list:
    return sorted(strings, key=sorted)


def search(ints: list, left, right, x) -> int:
    mid = (left + right) // 2
    if x == ints[mid]:
        return mid

    if ints[left] < ints[mid]:
        if ints[left] <= x <= ints[mid]:
            return search(ints, left, mid - 1, x)
        else:
            return search(ints, mid + 1, right, x)
    elif ints[left] > ints[mid]:
        if ints[mid] <= x <= ints[right]:
            return search(ints, mid + 1, right, x)
        else:
            return search(ints, left, mid - 1, x)