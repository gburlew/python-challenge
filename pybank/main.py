import os
import csv

month_count = 0
net_change = 0
changes = []
max_change = float('-inf')
min_change = float('inf')
with open("C:/Users/genna/Desktop/python-challenge/pybank/resources/PyBank/Resources/budget_data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    previous_profit = 0
    for row in reader:
        month_count += 1
        profit = int(row[1])
        net_change += profit
        if previous_profit != 0:
            change = profit - previous_profit
            changes.append(change)
            if change > max_change:
                max_change = change
            if change < min_change:
                min_change = change
        previous_profit = profit

average_change = sum(changes)/len(changes)
        
with open("C:\\Users\\genna\\desktop\\python-challenge\\pybank\\analysis\\analysis_output.txt", "a") as f:
    print(" ", file=f)
    print("Financial Analysis", file=f)
    print(" ", file=f)
    print("---------------------------------------------------------", file=f)
    print(" ", file=f)
    print("Total Months: " + str(month_count), file=f)
    print(" ", file=f)
    print("Net Profit: $" + str(net_change), file=f)
    print(" ", file=f)
    print(f"Average Change: ${average_change:.2f}", file=f)
    print(" ", file=f)
    print("Greatest Increase in Profits: $" + str(max_change), file=f)
    print(" ", file=f)
    print("Greatest Decrease in Profits: $" + str(min_change), file=f)

print(" ")
print("Financial Analysis")
print(" ")
print("---------------------------------------------------------")
print(" ")
print("Total Months: " + str(month_count))
print(" ")
print("Net Profit: $" + str(net_change))
print(" ")
print(f"Average Change: ${average_change:.2f}")
print(" ")
print("Greatest Increase in Profits: $" + str(max_change))
print(" ")
print("Greatest Decrease in Profits: $" + str(min_change))
