def move_zeros(array):
    n = len(array)
    array[:] = filter(None, array)
    array.extend([0] * (n - len(array)))
    return array
