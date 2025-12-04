# Task 5.1

def calculate_days(date):
    dd = int(date[:2])
    mm = int(date[3:])
    elapsed_day = (mm-1)*30
    total_elapsed = elapsed_day + dd
    return total_elapsed

# print(calculate_days("15-01"))
# print(calculate_days("30-01"))
# print(calculate_days("15-02"))

def days_difference(today, expire):
    today_days = calculate_days(today)
    expire_days = calculate_days(expire)
    difference = expire_days - today_days
    return difference

#print(days_difference('15-01', '15-02'))

def validate_date(date_str):
    dd_str = date_str[:2]
    mm_str = date_str[3:]
    if len(dd_str) != 2 or len(mm_str) != 2:
        print('length of month and day must be 2 digits only.')
        return False
    elif int(dd_str) < 1 or int(dd_str) > 30:
        print('Day should be between 1 and 30 inclusive.')
        return False
    elif int(mm_str) < 1 or int(mm_str) > 12:
        print('Month should be bewtwwn 1 and 12 inclusive.')
        return False
    elif date_str[2] != '-':
        print("Date must contain a '-' in between, DD-MM.")
        return False
    else:
        return True

# print(validate_date("4-12"))
# print(validate_date("01:01"))
# print(validate_date("012-01"))
# print(validate_date("01-033"))
# print(validate_date("55-08"))
# print(validate_date("01-55"))
# print(validate_date("01-02"))

while True:
    current_date = input('Enter todays date: ')
    if validate_date(current_date):
        break
while True:
    expire_date = input('Enter your products expire date: ')
    if validate_date(expire_date):
        break
difference_amtdays = days_difference(current_date, expire_date)
if difference_amtdays > 0 :
    print(f'Item is fresh and will expire in {difference_amtdays} days.')
elif difference_amtdays < 0:
    absdiff = abs(difference_amtdays)
    print(f'Item has expired {absdiff} days ago.')
else:
    print('The item will expire today.')
        













