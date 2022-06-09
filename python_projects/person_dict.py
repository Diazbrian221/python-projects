person_0 = {'first_name': 'Jessica', 'last_name': 'Rodriguez', 'age':'32',
            'city': 'New York'}
for key, value in person_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print(f"\n{person_0['first_name']}")
print(f"{person_0['last_name']}")
print(f"{person_0['age']}")
print(f"{person_0['city']}")

person_1 = {'favorite_number': 1, 'name': 'Eric'}
person_2 = {'favorite_number': 2, 'name': 'John'}
person_3 = {'favorite_number': 3, 'name': 'Samantha'}
person_4 = {'favorite_number': 4, 'name': 'Sarah'}
person_5 = {'favorite_number': 5, 'name': 'Ron'}

#Upon a second look of this code, I realize I can clean it up and
#make it simpler. I will do this by creating a dictionary that has
#multiple entries of a person and their favorite number.

favorite_numbers = {
    'Eric': 1,
    'John': 2,
    'Samantha': 3,
    'Sarah': 4,
    'Ron': 5,
}

#Below is my original code for printing out people's favorite number.
#This is inefficient because of the repetitive statements.
#I will clean this up through the use of a for loop.

#print(f"\n{person_1['name']}'s favorite number is {person_1['favorite_number']}.")
#print(f"\n{person_2['name']}'s favorite number is {person_2['favorite_number']}.")
#print(f"\n{person_3['name']}'s favorite number is {person_3['favorite_number']}.")
#print(f"\n{person_4['name']}'s favorite number is {person_4['favorite_number']}.")
#print(f"\n{person_5['name']}'s favorite number is {person_5['favorite_number']}.")

for name, number in favorite_numbers.items():
    if name == 'Eric':
        print(f"\n\n{name.title()}'s favorite number is {number}.")
    else:
        print(f"\n{name.title()}'s favorite number is {number}.")


python_tuple = {'meaning': 'a list in which values cannot be changed.'}
python_list = {'meaning':'a way to store values for a variable.'}
python_boolean = {'meaning': ' a value that is either true or false.'}

print(f"\n\nA tuple is {python_tuple['meaning']}")
print(f"\nA list is {python_list['meaning']}")
print(f"\nA boolean is {python_boolean['meaning']}")

major_rivers = {
    'Nile': 'Egypt',
    'Lena': 'Asia',
    'Danube': 'Europe',
}
for river, source in major_rivers.items():
    if river == 'Nile':
        print(f"\n\nThe {river.title()} river runs through {source.title()}.")
    else:
        print(f"\nThe {river.title()} river runs through {source.title()}.")

favorite_languages = {
    'Jen': 'python',
    'Sarah': 'C',
    'Edward': 'Ruby',
    'Phil': 'python',
}

have_taken_poll = ['Jen', 'Edward']

for name in favorite_languages.keys():
    if name in have_taken_poll:
        print(f"\n{name.title()}, thank you for taking the poll!")
    else:
        print(f"\n{name.title()}, please take the poll.")


