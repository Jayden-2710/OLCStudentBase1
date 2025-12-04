
menu = {'pasta':'99.00', 
        'pizza':'145.00', 
        'fries':'49.99'}

# to retreve a value
value1 = menu ['pizza']
print(value1)

#how to change value
menu['pizza']='159.00'

#how to add a new key/value pair
menu['mercedes'] = '2'

changing and adding is the same codes.

#deleting a key/value pair
del menu['pasta']  # dictionary has no .remove()

#checking if key exist
if 'mercedes' in menu:
    print('i sell mercs')
else:
    print('i dont sell mercs')

#loop through dictionary
for key in menu:
    print (key)
    print (menu[key])

#function you can use
for key, value in menu.items():
    print(f'{key}:{value}')

########################################################
# Question 3:
# The student council organised a charity fundraising event. 
# The amount collected from each class is stored in the dictionary below. 
# Identify the class that raised the highest and lowest amounts. 
# Print out the class names and their respective contribution amounts.
########################################################
import math
donations = {
    'Class 1A': 320, 'Class 1B': 480, 'Class 1C': 290, 'Class 1D': 375,
    'Class 1G': 450, 'Class 1H': 530, 'Class 2C': 470, 'Class 3D': 310,
    'Class 4E': 415, 'Class 5F': 390
}
# Answer for Question 3 here
maxclass = ''
maxamt = 0
minamt = math.inf
for classname, amount in donations.items():
    if  amount>maxamt:
        maxamt=amount
        maxclass = classname
print .............


























# dict1 = {"hamburger": 5, 
#          "pasta": 10, 
#          "fries": 2}

# # add / amend
# dict1["hamburger"] = 10

# # for key,value in dict1.items():
# #     print(key)
# #     print(value)

# # for key in dict1:
# #     print(key) # key
# #     print(dict1[key]) # value

# def oddoreven(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
