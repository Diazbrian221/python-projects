pizzas = ["pepperoni", "chicken", "margherita"]
#for pizza in pizzas:
    #print(f"I like {pizza} pizza.\n")
#print("What more can I say, I just really like pizza!\n")
#friend_pizzas = pizzas[:]
#pizzas.append("Bacon")
#print(f"My favorite pizzas are: {pizzas}")

#friend_pizzas.append("Hawaiian")
#print(f"My friend's favorite pizzas are: {friend_pizzas}")


big_cats = ["Lion", "Tiger", "Cheetah"]
#for big_cat in big_cats:
    #print(f"A {big_cat} would make for an interesting pet.\n")
#print("They're just so fascinating!")

twenties = list(range(1, 21))
#for twenty in twenties:
    #print(twenty)

millions = list(range(1, 1000001))
#for million in millions:
    #print(million)
#print(min(millions))
#print(max(millions))
#print(sum(millions))

odd_twenties = list(range(1, 21, 2))
#for odd_twenty in odd_twenties:
    #print(odd_twenty)

multiples_of_three = list(range(3, 31, 3))
#for multiple_of_three in multiples_of_three:
    #print(multiple_of_three)

cubes = []
#for value in range(1,11):
    #cubes.append(value**3)
    #print(cubes)

#first_three = cubes[ :3]
#print(f"The first three items in the list are {first_three}")
#middle_three = cubes [3:6]
#print(f"The middle three items in the list are {middle_three}")
#last_three = cubes[-3: ]
#print(f"The last three items are: {last_three}")

buffet_foods = ("Fried chicken", "Rice", "Potatoes",
                "Garden Salad", "Fruit Salad")
#buffet_foods[0] = "crabcakes"
#A note for line 50 is that I was intentionally causing an error to test
#tuple immutability.
print("Original Menu:") 
for buffet_food in buffet_foods:
    print(buffet_food)
buffet_foods = ("Grilled chicken", "Yellow Rice", "Potatoes",
                "Garden Salad", "Fruit Salad")
print("\nModified Menu:")
for buffet_food in buffet_foods:
    print(buffet_food)