#------------------------------------------------------------
# Exercise 14: Combined Checks (Password Policy)
# Requirements:
# - Non-empty
# - Length between 8 and 16
# - Must contain at least one digit 0-9
# - No spaces
# Keep prompting until valid, then print "Password set".
# Sample Inputs: "abc" (invalid), "abcd efgh1" (invalid), "GoodPass1" (valid)
#------------------------------------------------------------
while True:
    password = input('Enter a password: ')
    hasdigit = False
    hasspace = False
    hasspecial = False

    for c in password:
        if c.isdigit():
            hasdigit = True
        if c.isspace():
            hasspace = True
        if c in '@#_&^$%':
            hasspecial = True


    if password == '':
        print('Password cannot be blank.')  

    elif len(password) < 8 or len(password) > 16:
        print('Password invalid, must contain between 8 and 16 characters.')
 
    elif password == '':
        print('Password cannot be blank.')
        continue

    elif hasdigit == False:
        print('Password must contain a number form 0 to 9.')

    elif hasspace:
        print('password cannot contain spaces.')

    elif hasspecial:
        print ("Password must contain special characters '@#_&^$%' ")
    
    else:
        print('Password has been set.')

        

