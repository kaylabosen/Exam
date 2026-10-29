# Version 2: Investment Calculator

shares = float(input("10: "))
purchase_price = float(input("150: $"))
new_share_price = float(input("175: $"))

total_cost = shares * purchase_price
current_value = shares * current_price
profit_loss = current_value - total_cost
percent_return = (profit_loss / total_cost) * 100

print("\nInvestment Summary")
print("-" * 25)
print(f"Total Cost: ${total_cost:,.2f}")
print(f"Current Value: ${current_value:,.2f}")
print(f"Profit/Loss: ${profit_loss:,.2f}")
print(f"Return: {percent_return:.2f}%")


