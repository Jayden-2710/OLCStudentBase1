# # Task 2.1   3.14pm
#### 4 marks (-0.5) for improper variable naming
'''
a=[] ## proper list variable name e.g. player1_list
while True:
	p1_animal = input("Player 1, please enter an animal: ")
	p1_animal = p1_animal.lower()
	x=input('do you want to enter more animals? (y,n)') # need proper variable name
	a.append(p1_animal) # rightfully this should be before asking more animals
	if x.lower() != 'y':
		break
p2_guess = input("Player 2, please enter your guess:")
p2_guess = p2_guess.lower()
	
'''




# #Task 2.2
'''
a=[]
while True:
	p1_animal = input("Player 1, please enter an animal: ")
	p1_animal = p1_animal.lower()
	x=input('do you want to enter more animals? (y,n)')
	a.append(p1_animal)
	if x.lower() != 'y':
		break

### 3 marks
p2_guess = input("Player 2, please enter your guess:")
p2_guess = p2_guess.lower()
p2_score = 0
if p2_guess in a:
	a.remove(p2_guess)
	p2_score +=1

'''










#Tasl 2.3
while True:
    animals=[]
    count = 1
    while True:
        
        if count == 1:
            suffix = ("st")
        elif count == 2:
            suffix = ('nd')
        elif count == 3:
            suffix = ('rd')
        else:
            suffix =('th')

        p1_animal = input(f"Player 1, Please enter your {count}{suffix} animal" )
        p1_animal = p1_animal.lower()
        animals.append(p1_animal)
        check=input('(p1)do you want to enter more animals? (y,n)') 
        count += 1  
         
        if check.lower() != 'y':
            lenlist=int(len(animals))
            break
    p2_score = 0
    while True:
        p2_guess = input("Player 2, please enter your guess:")
        p2_guess = p2_guess.lower()
        if p2_guess in animals:
            animals.remove(p2_guess)
            p2_score +=1
        else: 
            print('Game Over, guess not correct')
            print('P2 score is', p2_score) 
            p1_score = lenlist-int(p2_score)
            print('P1 score is', p1_score)
            print('The remaining animals are', animals) 
            break
        if len(animals) == 0:
            print('Congrades, youve won')
            break
        if p2_score>p1_score:
            print('P2 wins!!')
        elif p1_score>p2_score:
            print('P1 wins!!')
        else:
            print('Its a draw!')

    play_again = input('Would you like to play again? Y/N')
    if play_again.upper() != 'Y':
        break



		

# about 8/ 10 ()