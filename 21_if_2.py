# write a program to findout which product is cheaper to purchase from 2 product's price and weight given by user
product_price_1 = float(input("Enter 1st product price"))
product_weight_1 = float(input("Enter 1st product weight (grams)"))

product_price_2 = float(input("Enter 2nd product price"))
product_weight_2 = float(input("Enter 2nd product weight (grams)"))

price_per_gram_1 = product_price_1 / product_weight_1
price_per_gram_2 = product_price_2 / product_weight_2 

if price_per_gram_1<price_per_gram_2:
    print("1st product is cheaper then 2nd product ",(price_per_gram_2 - price_per_gram_1))
else:
    print("2nd product is cheaper then 1st product ",(price_per_gram_1 - price_per_gram_2))

print("Good bye")
