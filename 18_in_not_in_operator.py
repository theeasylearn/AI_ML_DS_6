#example of in and not in operator

countries = ["Brazil", "Canada", "Argentina", "United States", "South Africa", "Nigeria", "Kenya", "Egypt", "Germany", "France", "India", "Japan", "China", "Indonesia", "Australia", "Russia", "United Kingdom", "Spain", "Mexico", "Thailand"]

print(countries) 

my_country = input("Where are you from (country)?")
result = my_country in countries
print(f"result = {result}")

g20 = ("Argentina", "Australia", "Brazil", "Canada", "China", "France", "Germany", "India", "Indonesia", "Italy", "Japan", "Mexico", "Russia", "Saudi Arabia", "South Africa", "South Korea", "Turkey", "United Kingdom", "United States", "European Union", "African Union")

country = input("give one country name which is not a memeber of G20")
result2 = country not in g20
print(f"result2 = {result2}") 
