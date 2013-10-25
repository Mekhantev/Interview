__author__ = 'Dmitry Mekhantev'


def binary_search(ints: 'Sorted linear collection',
                  i: int, left: int, right: int) -> int:
    pos = (left + right) // 2
    if i < ints[pos]:
        return binary_search(ints, i, left, pos - 1)
    if i > ints[pos]:
        return binary_search(ints, i, pos + 1, right)
    return pos


def get_subsets(ints: []) -> []:
    all_subsets = []
    #the same as multiplying 1 by 2**len(ints)
    subsets_number = 1 << len(ints)
    for bitmask in range(0, subsets_number):
        subset = []
        for j in range(0, len(ints)):
            #same as //'ing bitmask by 2**j
            if ((bitmask >> j) & 1) == 1:
                subset.append(ints[j])
        all_subsets.append(subset)
    return all_subsets