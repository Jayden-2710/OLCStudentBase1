#Task 5.1
def calculate_minutes(time):
    hour=time[:2]
    mins=time[3:]
    
    htm=int(hour)*60
    total_min=htm+int(mins)
    return total_min


num_minutes = calculate_minutes("01:30")
print(num_minutes)

#Task 5.2
def calculate_wage(clock_intime, clock_outtime):
    intime = int(calculate_minutes(clock_intime))
    outtime = int(calculate_minutes(clock_outtime))
    diff=outtime - intime
    hours=diff // 60 
    if hours < 8:
        wages = hours * 20
    else:
        hours = hours - 8
        wages = 160 + (hours * 30)
    return wages



wages = calculate_wage("09:00", "18:00")
print(wages)

def validate(time):
    hh = int(time[:2])
    mm = int(time[3:])
    if hh > 23 or hh < 0:
        print("Hour must be between 00 and 23(inclusive)")
        return False
    elif mm > 59 or mm < 0:
        print('Min must be between 0 and 59(inclusive)')
        return False
    elif time[2] != ':':
        print("':' must be present!")
        return False
    else:
        return True
    
while True:
    while True:
        intime = input('What time did you start work?')
        if validate(intime)==True:
            break
    while True:
        outtime = input('What time did you end work?')
        if validate(outtime)==True:
            break

inmins=calculate_minutes(intime)
outmins=calculate_minutes(outtime)

\if outmins>inmins:
    print('invalid, try again.')














































