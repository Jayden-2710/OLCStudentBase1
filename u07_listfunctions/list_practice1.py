list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

count = 0 
for num in list1:
    count += 1
print(count)

total = 0 
for num in list1:
    total += num
print(total)

average = total/count
print(average)

biggest = list1[0]
for num in list1:
    if num>biggest:
        biggest = num
    
    


#######################################################

# shapes = ["star", "square", "circle", "triangle"]
# colors = ["red","green","yellow","blue"]

# # -----------------------------------------
# # Task 1
# # Write a code to loop through both list
# # and match the color to the shape

# # Example output
# # red star
# # green square
# # yellow circle
# # blue triangle

# for i in range(len(shapes)):
#     # how to retrieve red?
#     # colors[i]
#     print(shapes[i]+' '+colors[i])



# # -----------------------------------------
# # Task 2
# # ask the user to input a shape
# # output the color for that shape

# for i in range(len(shapes)):
#     # how to retrieve red?
#     # colors[i]
#     print(shapes[i]+' '+colors[i])
# shapecheck=input('what shape would you like to figure out the colour for')
# if shapecheck in shapes :
#     for i in range (len(shapes)):
#         if shapecheck == shapes [i]:
#             print(f'the colour for {shapecehck} is {colours[i]}')

# # Example output
# # Enter a shape: circle
# # The color for circle is yellow