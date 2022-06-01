guest_list = ['Jesus', 'Seneca', 'Nietzchie']
greeting = f"Thank you for coming, {guest_list[0].title()}, so glad you could make it!"

unable = f"Aww, I'm sorry you couldn't attend, {guest_list[1].title()}."
print(unable)
guest_list[1] = 'Epictetus'
print(guest_list)

invitees = guest_list
invite = f"I'd like to invite you to my dinner party this evening, {guest_list[1]}."
print(invite)

bigger_table = f"Hello, {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, I found a larger table!"
print(bigger_table)

guest_list.insert(0, 'Marcus Aurelius')
guest_list.insert(2, 'Aristotle')
guest_list.append('Plato')
print(guest_list)
new_invite = f"I'd love to invite you, {guest_list[0]}"
print(new_invite)

so_sorry = f"Apologies, {guest_list[0]}, we only have room for two guests."
print(so_sorry)

popped_guest_list = guest_list.pop(0)
print(guest_list)
print(popped_guest_list)

still_invited = f"{guest_list[2]} and {guest_list[3]} are still invited though!"
print(still_invited)
del guest_list[-5]
del guest_list[-4]
print(guest_list)