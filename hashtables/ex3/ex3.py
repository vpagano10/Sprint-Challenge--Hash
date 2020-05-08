def intersection(arrays):
    base_arr = dict()
    other_arrs = dict()
    len_of_other_arrs = len(arrays)-1
    results = []

    for i in arrays[0]:
        base_arr[i] = 0
    # sets keys in base_arr = elements in arr[0] and values = 0

    for i in range(len_of_other_arrs):
        for x in arrays[i+1]:
            other_arrs[x] = x
    # sets keys in other_arrs = elements in all other arrs[1:] and values = key

    # for key in other_arrs.keys():
    #     vals = other_arrs[key]
    #     print(key, ":", vals)

    for key in base_arr.keys():
        # value = base_arr[key]
        # print('value', value)
        for key2 in other_arrs.keys():
            if key == key2:
                # value += 1
                results.append(key)
    # print(results)
    return results


arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1, ]
]
print(intersection(arrays))

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
