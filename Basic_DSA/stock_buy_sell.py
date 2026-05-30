
prices = [7,1,5,3,6,4]

smallest_seen_so_far = prices[0]
max_profit = 0
for price in prices:
    
    if price < smallest_seen_so_far:
        smallest_seen_so_far = price
    
    else:
        profit = price - smallest_seen_so_far
        if profit > max_profit:
            max_profit = profit

print(max_profit)