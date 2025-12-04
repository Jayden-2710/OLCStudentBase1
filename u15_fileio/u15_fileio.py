# #Text files
# #How to open, read, write a file

# #how to create a file
# with open('test.txt','w') as x:
#     #write to this file
#     x.write('bye\n')
#     x.write('bye\n')
#     x.write('gvttrgfy :')
#     x.write(' g3482759872fy')

# #how to read from a file
# with open('test.txt', 'r') as x:
#     #read from the file
#     contents = x.read()
#     print(contents)

# #read the file, choose random animal from list of animals
# import random
# with open('test/txt','r') as x:
#     contents = x.readlines()
#     print (contents)
# randamilal=random.choice(contents)
# print(randamilal)


with open('test.txt', 'r') as x:
    contentstr = x.read()
    contentlist = contentstr.split(',')

    for shape in contentlist:
        print(shape)
u15_fileio
