###########################################################
# Part 2. IN-CLASS Practice Exercises

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
'''students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
'''
# Task 1: Identify and print the name of the highest scoring student.

# students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
# maxscore=0
# topstudent=''
# for name, grade in students.items():
#     if grade>maxscore:
#         maxscore=grade
#         topstudent = name


# print('the highest scoring student in the class is', topstudent)

#------------------------------------------------------------
# Task 2: Calculate and display the name and score of students scoring above 80. 
	#   Display the total number of students who scored above 80.
'''
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
count=0
for name, grade in students.items():
    if grade>80:
        # student name and the score
        print(f"{name} : {grade}")
        count+=1
print('The amount of students who scored above 80 is :', count)
        
  '''      




#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.
'''
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}
for name, grade in students.items():
    students[name]= grade+5
print(students)
'''





###################################
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Available", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

#------------------------------------------------------------
# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies, status Available.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Available", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},

}

books["To Kill a Mockingbird"] = {'status':'Available', 'copies':3}
print (books)
#------------------------------------------------------------
# Task 2: Update the status of the books to "Checked Out" if 
# all copies are borrowed.
for book, stat in books.items():
    # stat >>> {"status": "Available", "copies": 5}
    if stat["copies"] == 0:
        stat["status"] = "Checked Out"
print(books)



#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.
for book, stat in books.items():
    if stat['status'] == 'Available':
        #copy_count = stat["copies"]
        print(book,':', stat['copies'])