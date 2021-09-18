import random
import math

#A car is travelling with an initial velocity u m/s accelerates with a constant acceleration of a m/s2 and reaches a final velocity of v m/s. What is the distance travelled by the car ?
#A car travelleing with a constant acceleration of a m/s2 reaches a final velocity of v m/s after travelling a distance of s m. What is the initial velocity of the car ? 
#A car is travelling with an initial velocity u m/s accelerates with a constant acceleration of a m/s2. If it travels for a distance of s m , then what is it’s final velocity?
#A car is traveling with an initial velocity u m/s accelerates with a constant acceleration reaches a final velocity of v m/s after travelleing a distance of s m. What is its acceleration ?


qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_s(u,v,a):
  return round(((v**2 - u**2)/(2*a)),1)

def calculation_u(v,h,a) :
    return round(math.sqrt((v**2) - (2*a*h)), 1)

def calculation_v(u,h,a) :
    return round(math.sqrt((u**2) + (2*a*h)), 1)

def calculation_a(u,v,h) :
    return round((((v**2) - (u**2))/(2*h)), 1)
    
def type1():
    u = random.randint(1,100)
    v = random.randint(u,u+100)
    a = random.randint(1,100)
    s = str(calculation_s(u,v,a)) + " m\n"
    q = "A car is travelling with an initial velocity " + str(u) + " m/s accelerates with a constant acceleration of " + str(a) + " m/s2 and reaches a final velocity of " + str(v) + " m/s. What is the distance travelled by the car ?\n"
    return q,s

def type2():
    s = random.randint(1,100)
    a = random.randint(0,100)
    tmp = 2*a*s
    v = random.randint(int(tmp),int(tmp)+100)
    u = str(calculation_u(v,s,a)) + " m/s\n"
    q = "A car travelleing with a constant acceleration of " + str(a) + " m/s2 reaches a final velocity of " + str(v) + " m/s after travelling a distance of " + str(s) + " m. What is the initial velocity of the car ?\n"
    return q,u

def type3():
    s = random.randint(1,100)
    a = random.randint(0,100)
    u = random.randint(0,200)
    v = str(calculation_v(u,s,a)) + " m/s\n"
    q = "A car is travelling with an initial velocity " + str(u) + " m/s accelerates with a constant acceleration of " + str(a) + " m/s2. If it travels for a distance of " + str(s) + " m , then what is it’s final velocity ?\n"
    return q,v

def type4():
    s = random.randint(1,100)
    u = random.randint(0,100)
    v = random.randint(u,u+100)
    a = str(calculation_a(u,v,s)) + " m/s2\n"
    q = "A car is traveling with an initial velocity " + str(u) + " m/s accelerates with a constant acceleration reaches a final velocity of " + str(v) + " m/s after travelleing a distance of " + str(s) + " m. What is its acceleration ?\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3:
        ques,answer = type4() 
    qns.write(ques)
    ans.write(answer)
    #print(ques)
    #print(answer)

qns.close()
ans.close()