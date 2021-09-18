import random


# The volume of a cube of side 1 cm is equal to ..... m3.
# The surface area of a solid cylinder of radius 2.0 cm and height 10.0 cm is equal to ……..(mm)2.
# A vehicle moving with a speed of 18 km h-1 covers ………. m in 1 s.
# The relative density of lead is 11.3. Its density is …….. g cm-3 or ………. kg m-3.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
#no_of_samples = 30

def type1():
    volume = round(random.randint(1,2000000)/1000,3)
    q = "What is the side of a cube of volume "+str(volume)+" cm3 (in m).\n"
    a = str(round((volume**(1/3))*1000000)) + "\n"
    return q,a

def type2():
    speed = random.randint(1,1000)
    time = random.randint(1,1000)
    q = "An object moving with a speed of "+str(speed)+" kmph covers x m in "+str(time)+" s, then find the value of x?\n"
    a = str(round(speed*time*(5/18),1)) +"\n"
    return q,a

def type3():
    speed = random.randint(1,1000)
    time = random.randint(1,1000)
    q = "An object moving with a speed of "+str(speed)+" ms-1 covers x km in "+str(time)+" hr, then find the value of x?\n"
    a = str(round(speed*time*(18/5),1)) +"\n"
    return q,a

def type4():
    density = round(random.randint(1,1000000)/100,2)
    q = "The relative density of a substance is "+str(density)+". Its density is x g cm-3 or y kg m-3, then find the value of x,y?\n"
    a = "x = " + str(round(density,2))+", y = "+str(round(density*1000,2)) +"\n"
    return q,a

def type5():
    radius = random.randint(1,1000)
    height = random.randint(1,1000)
    q = "The surface area of a solid cylinder of radius "+str(radius)+" cm and height "+str(height)+" cm is equal to (in mm2).\n"
    a = str(round(628*radius*(height+radius))) + "\n"
    return q,a

def type6():
    density = round(random.randint(1000,1010000)/100,2)
    q = "The density of a substance is "+str(density)+" kg m-3, then find relative density?\n"
    a = str(round(density/1000,3)) + "\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,9)
    if types == 1 or types == 2 or types == 3:
        ques,answer = type1()
    elif types == 4:
        ques,answer = type2()
    elif types == 5:
        ques,answer = type3()
    elif types == 6:
        ques,answer = type4()
    elif types == 7 or types == 9:
        ques,answer = type5()
    elif types == 8:
        ques,answer = type6()
    #print(ques)
    #print(answer)
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
