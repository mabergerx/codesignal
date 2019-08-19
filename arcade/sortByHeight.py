def sortByHeight(a):
    tree_indeces = [index for index, i in enumerate(a) if i == -1]
    
    not_trees = [i for i in a if i != -1]
    sorted_not_trees = sorted(not_trees)
    
    for ti in tree_indeces:
        sorted_not_trees.insert(ti, -1)

    return sorted_not_trees