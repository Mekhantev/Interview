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


def search_string(strings: list, left, right, s) -> int:
    mid = (left + right) // 2

    if not strings[mid]:
        l = mid - 1
        r = mid + 1
        while True:
            if l < left and r > right:
                raise IndexError()
            elif l >= left and strings[l]:
                mid = l
                break
            elif r <= right and strings[r]:
                mid = r
                break
            l -= 1
            r += 1

    if s == strings[mid]:
        return mid

    if s > strings[mid]:
        return search_string(strings, mid + 1, right, s)
    else:
        return search_string(strings, left, mid - 1, s)


def build_human_tower(people):
    sorted_people = sorted(people, key=lambda h: (h[0], h[1]))
    return sorted_people