__author__ = 'Dmitry Mekhantev'


def all_chars_single(s: str) -> bool:
    for i, c in enumerate(s):
        for y, cc in enumerate(s):
            if c == cc and i != y:
                return False
    return True


def reverse(s: str) -> str:
    chars = list(s)
    for i, c in enumerate(chars):
        l = len(chars) - i - 1
        if i < l:
            buffer = chars[l]
            chars[l] = c
            chars[i] = buffer
    return ''.join(chars)


def binary_search(ints: 'Sorted linear collection',
                  i: int, left: int, right: int) -> int:
    pos = (left + right) // 2
    if i < ints[pos]:
        return binary_search(ints, i, left, pos - 1)
    if i > ints[pos]:
        return binary_search(ints, i, pos + 1, right)
    return pos


def permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


def replace_spaces(s: str) -> str:
    chars = list(s)
    y = 0
    for i, c in enumerate(s):
        if c == ' ':
            index = i + y
            chars[index] = '%'
            chars.insert(index + 1, '2')
            chars.insert(index + 2, '0')
            y += 2
    return ''.join(chars)


def compress_string(s):
    chars = []
    current_c = s[0]
    i = 0

    append_char = lambda c: (
        chars.append(c),
        chars.append(str(i)))

    #def append_char(c):
    #    chars.append(c)
    #    chars.append(str(i))

    for c in s:
        if current_c == c:
            i += 1
        else:
            append_char(current_c)
            i = 1
            current_c = c
    append_char(current_c)
    return ''.join(chars)






