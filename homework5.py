# Hot Weather (Above 28°C / 82°F): A breathable cotton t-shirt paired with lightweight shorts and sandals or sneakers to stay cool, sweat-free, and ventilated in high heat.

# Mild / Cool Weather (15°C–20°C / 59°F–68°F): A long-sleeve pullover sweater paired with comfortable jeans to provide light insulation against a chilly breeze without causing overheating.

# Cold / Winter Weather (Below 5°C / 41°F): A heavy down puffer jacket worn over a thermal base layer with insulated trousers (along with a beanie and gloves) to trap body heat and block freezing winds.

temp = float(input("What is the temperature in °C? "))

if temp > 28:
    print("You should wear a breathable cotton t-shirt paired with lightweight shorts and sandals or sneakers to stay cool, sweat-free, and ventilated in high heat.")
elif temp > 15 and temp < 20:
    print("You should wear a long-sleeve pullover sweater paired with comfortable jeans to provide light insulation against a chilly breeze without causing overheating.")
elif temp < 5:
    print("You should wear a heavy down puffer jacket worn over a thermal base layer with insulated trousers (along with a beanie and gloves) to trap body heat and block freezing winds.")
else:
    print("ERROR PLEASE TRY WITH DIFFERENT TEMPERATURE")