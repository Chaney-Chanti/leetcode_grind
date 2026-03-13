# Weird IBM question that I googled
def minTotalCost(numItems, itemId, costs):
    i = 0
    items = {}
    # Group the items together
    while i < len(itemId):
        if itemId[i] not in items:
            items[itemId[i]] = costs[i]
        else:
            items[itemId[i]] = min(items[itemId[i]], costs[i])
        i += 1
        
    if len(items) != numItems:
        return -1
        
    min_sum = 0
    for value in items.values():
        min_sum += value
    

    return min_sum
