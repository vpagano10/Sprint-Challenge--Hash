def has_negatives(a):
    a.sort()
    a.reverse()
    cache = dict()
    abs_vals = []
    for i in a:
        if i > 0:
            cache[i] = i
        elif i < 0:
            i *= -1
            for key in cache.keys():
                if i == key:
                    abs_vals.append(key)
    return abs_vals


a = []
print(has_negatives(a))

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
