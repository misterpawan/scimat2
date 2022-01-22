import random
import math

# Calculate root mean square velocity of a gas molecule having molar mass of m at t degree C.
# If a gas molecule has root mean square velocity of v and is at a temperature t. What is the molar mass of the gas.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1500000

r = 8.31

def cal1(t1,m) :
    t1 = t1 + 273   
    return math.sqrt((3*r*t1*1000)/m) 

def cal2(t1,v) : 
    t1 = t1 + 273  
    return (3*r*t1*1000)/(v*v) 

def type1() :
    t1 = random.randint(100,1600)
    m = random.randint(1,400)
    t = random.randint(1,2)
    if t == 1 :
        q = "Calculate root mean square velocity of a gas molecule having molar mass of " + str(m) + " g/mol at " + str(t1) + " degree C.\n"
    else :
        q = "Calculate root mean square velocity of a gas molecule having molar mass of " + str(m) + " g/mol at " + str(t1) + " degree C. (R = 8.31 J/molK)\n"
    a = "If m is the molar mass of the gas in g/mol and t is the temperature in k (t = 273 + " + str(t1) + "), then Vrms = sqrt((3 x Rx tx 1000)/m) = sqrt((3 x 8.31 x " + str(t1) + " x 1000)/" + str(m) + ") = " + "{:.1e}".format(cal1(m,t1)) + "m/s\n"
    return q,a

def type2() :
    t1 = random.randint(100,1600)
    v = random.randint(1000,2000)
    t = random.randint(1,2)
    if t == 1 :
        q = "If a gas molecule has root mean square velocity of " + str(v) + " m/s and is at a temperature " + str(t) + " degree C. What is the molar mass of the gas.\n"
    else :
        q = "If a gas molecule has root mean square velocity of " + str(v) + " m/s and is at a temperature " + str(t) + " degree C. What is the molar mass of the gas. (R = 8.31 J/molK)\n"
    a = "If v is Vrms velocity in m/s and t is the temperatur in k (t = 273 + " + str(t1) + "), then molarmass(m) = (3 x R x t x 1000)/(v x v) = (3 x 8.31 x " + str(t1) + " x 1000)/(" + str(v) + " x " + str(v) + ") = " + "{:.1e}".format(cal2(v,t1)) + "g/mol\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    else :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
