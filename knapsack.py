def knapsack(wts: list, vals: list, size: int):
    if len(wts) != len(vals):
        return "LISTS NOT MATCH, CHECK YOUR LISTS!"
    item_count = len(wts)
    table = [[0 for _ in range(size+1)] for _ in range(item_count+1)]
    # fill in the table
    # note that the table first row and first col should be 0
    # all calculation starts from the second row and col

    # i is tha idx for the item
    for i in range(1, item_count+1):
        # j is the idx for the bag size
        for j in range(1, size+1):
            # if the bag cant even fit this item, we cant take it ofc
            if wts[i-1] > j:
                table[i][j] = table[i-1][j]
            # else we compare take it or not
            else:
                table[i][j] = max(table[i-1][j], table[i-1]
                                  [j-wts[i-1]]+vals[i-1])
    print(table)
    return table[item_count][size]


item_weights = [2, 4, 6, 7, 10]
item_values = [3, 5, 6, 9, 19]
print(knapsack(item_weights, item_values, 16))