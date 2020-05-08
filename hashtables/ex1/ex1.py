import math

weights = [4, 6, 10, 15, 16]
# weights = [4, 4]
length = 5
# length = 2
limit = 21
# limit = 8


def get_indices_of_item_weights(weights, length, limit):
    cache = dict()
    index_weights = dict()
    index = 0
    if length < 2:
        return None
    if length == 2 and sum(weights) == limit:
        return [1, 0]

    for i in weights:
        index_weights[index] = i
        index += 1
    # {0: 4, 1: 6, 2: 10, 3: 15, 4: 16}
    for i in weights:
        cache[i] = limit - i
    # {4: remainder, 6: remainder, 10: remainder, 15: remainder, 16: remainder,}

    for key in cache.keys():
        value = cache[key]
        if value in cache.keys():
            value_res = value
            key_res = key

    val_index = value_res
    key_index = key_res
    for key in index_weights.keys():
        val = index_weights[key]
        if val == value_res:
            val_index = key
            # print(key)
        if val == key_res:
            key_index = key
            # print(key)
    return [max(val_index, key_index), min(val_index, key_index)]


print(get_indices_of_item_weights(weights, length, limit))
# get_indices_of_item_weights(weights, length, limit)
