usernames = ['admin', 'brian', 'jacob', 'ayden', 'jayden']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("\nWelcome back, Admin, would you like a status report?")
        elif username != 'admin':
            print(f"\nHello {username.title()}, thanks for logging in.")
else:
    print('\nWe need to find some users!')

current_users = ['eric', 'lily', 'marcus', 'susanne', 'amy']
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())
new_users = ['AmY', 'Eric', 'John', 'Rosanna', 'mari']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"\nPlease enter a different username. {new_user} already in use.")
    else:
        print(f"\nWelcome, {new_user}. Thanks for logging in.")

#Ordinal Numbers Exercise
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")



