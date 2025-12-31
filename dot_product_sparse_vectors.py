# Problem: Compute dot product of two sparse vectors

def dot_product_sparse_vectors(v1, v2):

    v1_dict, v2_dict, res = {}, {}, 0
    for i, val in enumerate(v1):
        if val != 0:
            v1_dict[i] = val

    for i, val in enumerate(v2):
        if val != 0:
            v2_dict[i] = val

    iterate_on, check_on = (
        (v1_dict, v2_dict) if len(v1_dict) <= len(v2_dict) 
        else (v2_dict, v1_dict)
    )
    get = check_on.get # localize for speed
    for k, v in iterate_on.items():
        v_c = get(k)
        if v_c is not None:
            res += v * v_c
    return res


# ---------------------------------------------------
# Execution & Testing
# ---------------------------------------------------
v1 = [1, 0, 0, 0, 1, 0, 2, 3, 1, 0, 0, 0]
v2 = [3, 1, 0, 1, 1, 9, 0, 0, 4, 0, 1, 0, 1, 0, 0, 2]
assert dot_product_sparse_vectors(v1, v2) == 8



