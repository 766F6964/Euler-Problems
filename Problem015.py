def count_lattice_paths(size):
    x = [1] * size
    for k in range(0, size):
        for n in range(0, k):
            x[n] = x[n] + x[n - 1]
        x[k] = 2 * x[k - 1]
    return x[size - 1]


print(count_lattice_paths(20))