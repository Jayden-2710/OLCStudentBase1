
planets = ['earth','mars']
p1=planets[0]
planets[0]='newplanetname'
planets.append('newnewnewplanetname')

#how to add to front of list
planets.insert(0,'planet3')

#how to delete
# opt1: del
del planet[1]
# opt2: .remove()
planets.remove('earth')
print(planets)

# existance check
if 'mars' in planets:
    print('planet exist')
else:
    print('planet does ntoe exist')


# how to loop through a list option 1
for pedfhsuiefhsuiefhue in planets:
    print pedfhsuiefhsuiefhue

# option 2
 for i in range(len(planets)):
    print(planets[i])






















# # string variable
# # integer, float
# # boolean >> True False

# # List
# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Accessing List Elements by Index
# # Write a program to access and print the first, second, and last 
# # elements of a list using indexing.

# fruits = ["apple", "orange", "banana","durian"] # my list
# print(fruits[2]) # retrieve a specific value from the list



# #------------------------------------------------------------
# # Exercise 2: Adding Elements to a List
# # Write a program to add an element to the end of a list using 
# # append(), and add another element at a specific index using 
# # insert().


# fruits.append("durian") # add a new item to the list, adds at the back

# fruits.insert(1, "grapes") # add at specific position





# #------------------------------------------------------------
# # Exercise 3: Using del() to Remove an Element by Index
# # Write a program to delete an element at a specific index.
# # Example: Remove the second color.

# del(fruits[1]) # deleting by the index



# #------------------------------------------------------------
# # Exercise 4: Using remove() to Remove an Element by Value
# # Write a program to remove a specific element by its value.
# # Example: Remove "green" from the list.
# # colors = ["red", "green", "blue", "yellow"]
# # colors.remove("green")  # Remove by value
# # print("Colors after removal: {}".format(colors))

# # fruits.remove("durian")

# # while True:
# #     if "durian" in fruits:
# #         fruits.remove("durian")
# #     else:
# #         break



# #------------------------------------------------------------
# # Exercise 5: Using pop() to Remove and Retrieve an Element
# # Write a program to remove the last element of a list using pop().
# # Example: Remove and print the last color.
# # colors = ["red", "green", "blue", "yellow"]
# # removed_color = colors.pop()  # Remove the last element
# # print("Removed color: {}".format(removed_color))
# # print("Colors after pop: {}".format(colors))

# lastfruit = fruits.pop() # removes last one and assign to variable
# print(fruits)




# #------------------------------------------------------------
# # Exercise 6: Modifying Elements in a List
# # Write a program to change the second element in a list to "pink."
# # colors = ["red", "green", "blue"]
# # colors[1] = "pink"  # Modify value at index 1
# # print("Modified colors: {}".format(colors))
# print(lastfruit)
# fruits[3] = "spikyfruit" # change the value
# print(fruits)

# #------------------------------------------------------------
# # Exercise 7: Membership Check
# # Write a program to check if "blue" is in the list.
# # colors = ["red", "green", "blue"]
# # if "blue" in colors:
# #     print("Blue is in the list.")
# # else:
# #     print("Blue is not in the list.")

# # validation check - existence check
# checkfruit = input("Enter a fruit name: ")
# if checkfruit in fruits:
#     print(f"{checkfruit} is in the list")
# else:
#     print(f"{checkfruit} is not in the list")

# #------------------------------------------------------------

# ##### to loop through every single item
# for i in fruits:
#     print(i)

# # for i in range(5): 