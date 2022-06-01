ideal_places = ['Italy', 'Spain', 'Costa Rica', 'Canada', 'Japan']
print(ideal_places)
print("This is the original order")

print(sorted(ideal_places))
print("this is the sorted order")

print(ideal_places)
print("Here it is in its original order again")

ideal_places.sort(reverse=True)
print(ideal_places)
print("Here is the list reversed alphabetical order")

ideal_places.sort()
print(ideal_places)
print("Here is the list in alphabetical order")

ideal_places.reverse()
print(ideal_places)
print("\nHere is the list in reverse.")

# I messed up numerous times because instead of using
# the reverse() function for my list, I used the sort(reverse=True) function.
#This permanently altered my list. Had I used the reverse() function,
#I could have used that function again to return my list to its
#original order. Unfortunately, sort(reverse=True) does
#not work the same way.