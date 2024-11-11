def set_cover(universal, subsets):
    covered = set()
    selected_sets = []

    while covered != universal:
        selected_set = max(subsets, key=lambda s: len(s - covered))
        covered.update(selected_set)
        print(covered)
        selected_sets.append(selected_set)
    return selected_sets

universal = {1, 2, 3, 4, 5}
subsets = [
    {1},
    {2},
    {5},
    {2, 3, 5},
    {2, 3, 4},
    {1, 2, 3, 4},
]

print(set_cover(universal, subsets))
