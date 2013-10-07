from copy import deepcopy

__author__ = 'Dmitry Mekhantev'


def binary_search(ints: 'Sorted linear collection',
                  i: int, left: int, right: int) -> int:
    pos = (left + right) // 2
    if i < ints[pos]:
        return binary_search(ints, i, left, pos - 1)
    if i > ints[pos]:
        return binary_search(ints, i, pos + 1, right)
    return pos


def rotate(matrix):
    m = deepcopy(matrix)
    m_len = len(m)
    layers_number = m_len // 2
    for layer in range(layers_number):
        first = layer
        last = m_len - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]
            #left -> top
            m[first][i] = m[last - offset][first]
            #bottom -> left
            m[last - offset][first] = m[last][last - offset]
            #right -> bottom
            m[last][last - offset] = m[i][last]
            #top -> right
            m[i][last] = top
    return m


def set_zeros(matrix):
    m_height = len(matrix)
    m_width = len(matrix[0])
    coordinates = ()
    for i in range(m_height):
        for y in range(m_width):
            if matrix[i][y] == 0:
                coordinates = (i, y)
    m = deepcopy(matrix)
    for i in range(m_height):
        for y in range(m_width):
            if i == coordinates[0] or y == coordinates[1]:
                m[i][y] = 0
    return m



