#Banking and transactions
#05. Update balance after deposit.
current_balance = 10000
deposit_balance = 5000

print(f"current balance : {current_balance}")
print(f"deposit balance : {deposit_balance}")

current_balance=current_balance+deposit_balance
print(f"after deposit 10000+5000=15000 : {current_balance}")

#06. Update balance after withdrawal.
current_balance=12000
withdrawal_amount=3000
print("your current balance before withdrawal is ",current_balance)
print("withdrawal amount",withdrawal_amount)
current_balance=current_balance-withdrawal_amount
print("after withdrawal current balance is",current_balance)

#07.Increase shopping cart items by 3, 
current_cart_item=5
increase_cart_item=3
print("before  shooping cart item",current_cart_item)
new_cart_item=current_cart_item+increase_cart_item
print("after increase your cart item is",new_cart_item)

#08. Apply a 20% discount to a price,
price_tv=5000
print("before any discount tv price is",price_tv)
discount_price=price_tv*20//100
new_price=price_tv-discount_price
print("after discount the price of tv is",new_price)

#09. calculate student percentage