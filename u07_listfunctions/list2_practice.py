# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 0.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 63.0, 33.0, 30.5]
# Answer for Question 2 here
count = 0 
slowest = swim_times[0]
slowestlane = 0
fastest = swim_times[0]
fastestlane = 0
for i in swim_times:
    count += 1
    if i > slowest:
        slowest = i
        slowestlane = count
    if i < fastest:
        fastest = i
        fastestlane = count
        
print(f"The fastest swimmer has a time of {fastest} at lane {fastestlane}")
print(f"The slowest swimmer has a time of {slowest} at lane {slowestlane}")