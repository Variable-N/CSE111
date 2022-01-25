item_name = ["bbq chicken cheese burger", "beef burger", "naga drums"]
item_price = [250,170,200]
def foodPanda (name, place = 'mohakhali') :
    name.lower()
    place.lower()
    mealcost = item_price[item_name.index(name)]
    if place == 'mohakhali':
        print(round(mealcost + mealcost * 0.08 + 40, 1))
    else :
        print(round(mealcost + mealcost * 0.08 + 60, 1))

a =input()
b =input()
if b == "":
    foodPanda(a)
else :
    foodPanda(a,b)