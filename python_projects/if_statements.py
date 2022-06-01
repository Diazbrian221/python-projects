car = 'Type R'
print("Is car == 'Type R'? I predict True.")
print(car == 'Type R')

print("\nIs car == 'Audi'? I predict False.")
print(car == 'Audi')

fav_food = 'cookies'
print("\nIs your favorite food cookies? I think it's true.")
print(fav_food == 'cookies')

print("\nIs your favorite food watermelon? I don't think it is.")
print(fav_food == 'watermelon')

fav_show = 'Game of Thrones'
print("\nIsn't your favorite show Game of Thrones?")
print(fav_show == 'Game of Thrones')

print("\nI could have sworn your favorite show was Queen's Gambit.")
print(fav_show == 'Queen\'s Gambit')

instrument = "bass"
print("\nDon't you play the bass?")
print(instrument == 'bass')

print("\nI'm pretty sure I remember you playing the piano.")
print(instrument == 'piano')

dog_name = "Teddy"
print("\nHow's your dog Teddy doing? That was his name right?")
print(dog_name == 'Teddy')

print("\nDidn't you have a dog named Bentley?")
print(dog_name == 'Bentley')

university = "mit".upper()
if university == "MIT":
    print(f"\nYes, I do go to {university}!")
else:
    print(f"\nNo, I don't go to {university}.") 

age = 25
age_2 = 19
age_3 = 24
if age >= 21:
    print("\nOkay sir, here's your drink!")
if age_2 and age_3 >= 21:
    print("\nOkay gentlemen, here's your drinks!")
else:
    print("\nSorry sir, I can't give you this drink.")
if age >= 21 and age_3 >= 21:
    print("\nOkay gentlemen, here's your drinks!")
else:
    print("\nSorry, I can only give one of you drinks.")
if age_2 >=21 or age_3 >=21:
    print("\nWell, I can only give one of you a drink.")
else:
    print("Sorry, I can't give you guys drinks!")

alien_color = "yellow"
if alien_color == "green":
    print("\nPlayer 1 has earned 5 points!")
elif alien_color == "blue":
    print("\nPlayer 1 has earned 10 points!")
elif alien_color == "yellow":
    print("\nPlayer 1 has earned 20 points!")
else:
    print("\nGame Over")

stage_of_life = 62
if stage_of_life < 2:
    print("\nThe person is a baby.")
if stage_of_life >= 2 and stage_of_life < 4:
    print("\nThe person is a toddler.")
if stage_of_life >= 4 and stage_of_life < 13:
    print("\nThe person is a kid.")
if stage_of_life >=13 and stage_of_life < 20:
    print("\nThe person is a teenager.")
if stage_of_life >= 20 and stage_of_life < 65:
    print("\nThe person is an adult.")
if stage_of_life >= 65:
    print("\nThe person is an elder.")

favorite_fruits = ['banana', 'rambutan', 'pineapple']
if 'banana' in favorite_fruits:
    print("\nI really like bananas!")
if 'rambutan' in favorite_fruits:
    print("\nI really like rambutan!")
if 'pineapple' in favorite_fruits:
    print("\nI really like pineapple!")

