import random

# A bullet of mass m1 g and speed v1 m/s is fired into a door and gets embedded exactly at the centre of the door. The door is l m wide and weighs m kg. It is hinged at one end and rotates about a vertical axis practically without friction. Find the angular speed of the door just after the bullet embeds into it.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

def cal1(m1, m2, v1, l) :
    am = (m1*v1*l)/(1000*2)
    i = (m2*l*l)/3
    return round(am/i,1)

def type1() :
    m1 = random.randint(1,500)
    m2 = random.randint(1,100)
    l = random.randint(1,100)
    v1 = random.randint(1000,1500)
    q = "A bullet of mass " + str(m1) + " g and speed " + str(v1) + " m/s is fired into a door and gets embedded at centre of the door. The door is " + str(l) + " m wide and weighs " + str(m2) + " kg. It is hinged at one end and rotates about a vertical axis. Find the angular speed of the door just after the bullet embeds into it.\n"
    a = str(cal1(m1, m2, v1, l)) + " rad/s\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
