'''
def hello():
    print('Hello World')

def greet(yourname):
    print(f'hello, {yourname}')

def intro(yourname, myname):
    greet(yourname)
    print(f'My name is {myname}')

intro("jayden", "david")
'''

def area_circle(radius):
    area = radius**2 * 3.14
    return area

cir1 = area_circle(656)
print(cir1)


temps = [25.6, 27.1, 28.3, 29.4, 31.1, 32.8, 27.1, 33.5, 22.5, 34.6]
# write a function to return the average temperature of a list of temperatures
def average_temps(temps):
    total = sum(temps)
    ave= total/len(temps)
    return ave
    
print(average_temps(temps))
                                                                                                                                          