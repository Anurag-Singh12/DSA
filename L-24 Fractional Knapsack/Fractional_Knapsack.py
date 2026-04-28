def Fractional_knapsack( price, items_wt, capacity):
    n = len(items_wt)

    items = [(price[i], items_wt[i], price[i] / items_wt[i]) for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if (items[i][2] < items[j][2]):
                items[i], items[j] = items[j], items[i]

    profit = 0.0

    for price, item_wt, perKgPrice in items:
        if (capacity >= item_wt):
            capacity = capacity - item_wt
            profit = profit + price
        else:
            profit = profit + perKgPrice * capacity
        
    print("total profit = ", profit)

price = [24, 21, 12, 10]
items_wt = [7, 3, 4, 5]
capacity = 20

Fractional_knapsack(price, items_wt, capacity)