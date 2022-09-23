'''Zaineb Halibi
Project 1
A Breathe of Fresh Air'''

import math
me = 1
highaqi = 0
aqiList = [ ]
print("Air Quality Index Calculator ")

# ask user for number of location tell we get a valid answer
number= int(input("How many locations for this report? \n"))
while number <= 0 :
  number= int(input("How many locations for this report? \n"))


# entire code will loop according to the amount of locations user puts in 
for x in range(number):
  location = input(f"What is the name of Location {me}? ")
  me += 1
  
#----------------Calculate PM-2.5 concentration---------------------------------------
  pm = float(input(" -> Enter PM-2.5 concentration: \n"))
  if pm < 0:
    number -= 1
    #make list of PM-2.5 to return average in summary(only positive answers)
  if pm > 0:
    aqiList.append(pm)
    summ = sum(aqiList)
    average =(summ/number)
  if 0 <= pm <= 12.0:
    ilow, ihigh, clow,chigh = 0,50,0,12.0
  elif pm <= 35.4:
    ilow, ihigh, clow,chigh = 51, 100, 12.1, 35.4
  elif pm <= 55.4:
    ilow, ihigh, clow,chigh = 101, 150, 35.5, 55.4
  elif pm <= 150.4:
    ilow, ihigh, clow,chigh = 151, 200, 55.5, 150.4
  elif pm <= 250.4:
    ilow, ihigh, clow,chigh = 201, 300, 150.5, 250.4
  else:
    ilow, ihigh, clow,chigh = 301, 500, 250.5, 500.4
  if pm >= 0:
    impm = ((ihigh - ilow) / (chigh - clow)) * (pm - clow) + ilow
    print("    PM-2.5 concentration of ", ((math.trunc(10*pm))/10),"is index level", round(impm))
  elif pm < 0:
       impm = 0

#------------------------Calculate PM-10---------------------------------------------------------
  ten = float(input(" -> Enter PM-10 concentration: \n"))
  ten = math.trunc(ten)
  if 0 <= ten <= 54:
    ilow, ihigh, clow,chigh = 0,50, 0,54
  elif ten <= 154:
    ilow, ihigh, clow,chigh = 51, 100, 55, 154
  elif ten <= 254:
    ilow, ihigh, clow,chigh = 101, 150, 155, 254
  elif ten <= 354:
    ilow, ihigh, clow,chigh = 151, 200, 255, 354
  elif ten <= 424:
    ilow, ihigh, clow,chigh = 201, 300, 355, 424
  elif ten <= 604:
    ilow, ihigh, clow,chigh = 301, 500, 425, 604
  if ten >= 0:
    ipten = ((ihigh - ilow) / (chigh - clow)) * (ten - clow) + ilow
    print("    PM-10 concentration of", math.trunc(ten),"is index level", round(ipten),"\n")
  elif ten < 0:
      ipten = 0

#---------------------------Calculate NO-2 concentration----------------------------------------------
  nitro = float(input(" -> Enter NO-2 concentration: \n"))
  if 0 <= nitro <= 54:
    ilow, ihigh, clow,chigh = 0,50, 0,53
  elif nitro <= 154:
    ilow, ihigh, clow,chigh = 51, 100, 54, 100
  elif nitro <= 254:
    ilow, ihigh, clow,chigh = 101, 150, 101, 360
  elif nitro <= 354:
    ilow, ihigh, clow,chigh = 151, 200, 361, 649
  elif nitro <= 424:
    ilow, ihigh, clow,chigh = 201, 300, 650, 1249
  elif nitro <= 604:
    ilow, ihigh, clow,chigh = 301, 500, 1250, 2049
  if nitro >= 0:
    ipnitro = ((ihigh - ilow) / (chigh - clow)) * (nitro - clow) + ilow
    print("    NO-2 concentration of", math.trunc(nitro),"is index level",math.trunc(round(ipnitro)),"\n")
  elif nitro < 0:
       ipnitro = 0
#-----------------------------------------Calculate S0-2------------------------------------------------------
  so = float(input(" -> Enter SO-2 concentration: \n"))
  if 0 <= so <= 35:
    ilow, ihigh, clow,chigh = 0,50, 0,35
  elif so <= 75:
    ilow, ihigh, clow,chigh = 51, 100, 36, 75
  elif so <= 185:
    ilow, ihigh, clow,chigh = 101, 150, 76, 185
  elif so <= 304:
    ilow, ihigh, clow,chigh = 151, 200, 186, 304
  elif so <= 604:
    ilow, ihigh, clow,chigh = 201, 300, 305, 604
  elif so <= 605:
    ilow, ihigh, clow,chigh = 301, 500, 605, 1004
  if so >= 0:
    ipso = ((ihigh - ilow) / (chigh - clow)) * (so - clow) + ilow
    print("    SO-2 concentration of", math.trunc(so),"is index level",math.trunc(round(ipso)),"\n")
  elif so < 0:
       ipso = 0
#---------------------------------------Calculate CO--------------------------------------------------
  co = float(input(" -> Enter CO concentration: \n"))
  if 0 <= co <= 4.4:
    ilow, ihigh, clow,chigh = 0,50, 0,4.4
  elif co <=9.4:
    ilow, ihigh, clow,chigh = 51, 100, 4.5, 9.4
  elif co <= 12.4:
    ilow, ihigh, clow,chigh = 101, 150, 9.5, 12.4
  elif co <= 15.4:
    ilow, ihigh, clow,chigh = 151, 200, 12.5, 15.4
  elif co <= 30.4:
    ilow, ihigh, clow,chigh = 201, 300, 15.5, 30.4
  elif co <= 50.4:
    ilow, ihigh, clow,chigh = 301, 500, 30.5, 50.4
  if co >= 0:
    ipco = ((ihigh - ilow) / (chigh - clow)) * (co - clow) + ilow
    print("    CO concentration of", co,"is index level",math.trunc(round(ipco)),"\n")
  elif co < 0:
    ipco = 0
#---------------------------------------Calculate O-------------------------------------------------
  o = float(input(" -> Enter O3 concentration: \n"))
  if o <= 164:
    ilow, ihigh, clow,chigh = 101, 150, 125, 164
  elif o <= 204:
    ilow, ihigh, clow,chigh = 151, 200, 165, 204
  elif o <= 404:
    ilow, ihigh, clow,chigh = 201, 300, 15.5, 30.4
  elif o <= 604:
    ilow, ihigh, clow,chigh = 301, 500, 30.5, 50.4
  if o >= 125:
    ipo = ((ihigh - ilow) / (chigh - clow)) * (o - clow) + ilow
    print("    O3 concentration of", math.trunc(o),"is index level",math.trunc(round(ipo)),"\n")
  elif o < 125:
       ipo = 0
       
    #finds aqi, and highest aqi for summary
  aqi = round(max(impm, ipten, ipnitro,ipco,ipso,ipo))
  if aqi > highaqi:
    highaqi = aqi
    maxaqi = highaqi
    maxlocation = location

#prints out final AQI, Quality label based on calculations, and summary report
  print("AQI for",location,"is", aqi)
  if 0<= aqi <= 50:
    air_quality = ("Good") 
  elif aqi <= 100:
    air_quality = ("Moderate") 
  elif aqi <= 150:
    air_quality = ("Unhealthy for Sensitive Groups")
  elif aqi <= 200:
    air_quality = ("Unhealthy")
  elif aqi <= 300:
    air_quality = ("Very Unhealthy")
  elif aqi <= 500:
    air_quality = ("Hazardous") 

  print("Air Quality: ", air_quality)


print(f"\n Summary:")
print("     Location with highest AQI is " ,maxlocation,"(", highaqi,")\n\n  Average PM-2.5 concentration:" , average)
      
