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
    #the same as 1 * 2**len(ints)
    subsets_number = 1 << len(ints)
    for bitmask in range(subsets_number):
        #convert bitmask to set
        subset = []
        for i in range(len(ints)):
            #same as bitmask // 2**i
            if ((bitmask >> i) & 1) == 1:
                subset.append(ints[i])
        all_subsets.append(subset)
    return all_subsets