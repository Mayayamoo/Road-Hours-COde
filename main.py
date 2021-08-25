
import random
#required variabes, input the prefered hours and minutes driving can occur at, then length of drive
hour= [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
minute = [0, 15, 30, 45, 20, 40]
length = [20, 30, 40, 45, 60, 75]
#accompanying driver
p = ["mom", "dad"]
#needed for to calculate hours left
x= 0
y= 0
# adds weight to length and accompanying driver variables
lengths=(random.choices(length, weights=[20, 25, 30, 15 ,5, 5], k=6))
pa=random.choices(p,weights=[80,20], k=2)

# x = day hours needed, y = night hours needed, program will calculate a set of times driving occured at, how long and with who. the program will execute until day and night hour conditions are met
while ((int(x) < 3000) or (int(y) < 600)):
    guz=str(random.choice(minute))
    times = str(random.choice(lengths))
    hours=str(random.choice(hour))
    if guz == str(0):
        print (hours + " O' clock" + " for " + times + " minutes. Driving with " + random.choice(pa))
    else:
        print (hours +":" + guz + " for " + times + " minutes. Driving with " + random.choice(pa))
    if int(hours) >= int(18):
        hours = y
        y = int(y) + int(times)
        minutesy = int(y)/60
        
    if int(hours) <= int(17):
        hours = x
        x = int(x) + int(times)
        minutesx = int(x)/60

    #prints the amount of hours done at this point
    #extra note, for some reason night hours sometimes wont print and shows an error, if you just keep trying to run it itll print eventually, i dont know why. oh! could be because there arent any night hours at that point and it cant print 0?
    #seems that if the function does run itll add the hours to both the day and night hours, weird because it only does this for the first line, this issue does not happen again, will have to check this later?
    print ("Day Hours: " + str(minutesx))
    print ("Night Hours: " + str(minutesy))