https://dmoj.ca/problem/ccc06j1

burger = {"cheese" : 461, "fish" : 431, "veggie" : 420, "no_burger": 0}
drink = {"soft_drink" : 130, "orange_juice" : 160, "milk" : 118, "no_drink" : 0}
side = {"fries" : 100, "baked_potato" : 57, "chef_salad" : 70, "no_side" : 0}
dessert = {"apple_pie" : 167, "sundae" : 266, "fruit_cup" : 75, "no_dessert" : 0}

burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

burger_key = list(burger)[burger_choice - 1]
side_key = list(side)[side_choice - 1]
drink_key = list(drink)[drink_choice - 1]
dessert_key = list(dessert)[dessert_choice - 1]

calories = burger[burger_key] + drink[drink_key] + side[side_key] + dessert[dessert_key]

print("Your total Calorie count is " + str(calories) + ".")

