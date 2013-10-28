from copy import deepcopy


def rotate(m):
    m = deepcopy(m)
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


def set_zeros(m):
    m_height = len(m)
    m_width = len(m[0])
    coordinates = ()
    for i in range(m_height):
        for y in range(m_width):
            if m[i][y] == 0:
                coordinates = (i, y)
    m = deepcopy(m)
    for i in range(m_height):
        for y in range(m_width):
            if i == coordinates[0] or y == coordinates[1]:
                m[i][y] = 0
    return m