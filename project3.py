'''
Zaineb Halibi
Homework 1
CECS 174
Neal Terrell'''

import math

C = 299792458
DISTANCE = 7.4740e16
SECONDS_PER_DAY = 86400
d = 7.4740 * 10**16 

#Ask user to enter velocity of space ship 
vel = float(input("Enter space ship velocity as a fraction of the speed of light:"))
v = vel * C

dilation = math.sqrt( 1 - (( v**2)/(C**2)) )


#formula for amount of time passes for human on earth looking at airplane 
earth_time = DISTANCE / v

#convert time experienced by observer on earth
daycount = earth_time / SECONDS_PER_DAY
years = int(daycount / 365)
days = int(daycount - ( years * 365 ))


#time to get to proxima 
pass_time = (d / v) * dilation

#convert time experienced by passenger on ship
daycountp = pass_time / SECONDS_PER_DAY
yearsp = int(daycountp / 365)
daysp = int(daycountp - (yearsp * 365))


print()
print('Traveling to Wolf 359...')
print("An observer on Earth ages", years, 'years,', days,'days during the trip.')
print('A passenger on the ship ages' , yearsp,'years,',daysp,'days during the trip.')


