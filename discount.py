def calculate_discount(price, discount_percent):
#Calculate the final price after applying discount if discount_percent is 20% or higher.
#Otherwise, return the original price:
    
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input:
original_price = float(input("Enter the original price of the item: "))
currency=(input("Enter the currency of the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percentage)

if final_price < original_price:
        print(f"Discount applied. Final price: {currency} {final_price:.2f}")
else:
        print(f"No discount applied. Original price remains: {currency} {original_price:.2f}")
