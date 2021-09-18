import random

# A trolley of mass m1 kg moves with a uniform speed of v1 m/s on a friction less track. A child of mass m2 kg runs on the trolley from one end to the other (l m away) with a speed of v2 ms-1 relative to the trolley in a direction opposite to the trolley’s motion, and jumps out of the trolley. What is the final speed of the trolley? 
# A trolley of mass m1 kg moves with a uniform speed of v1 m/s on a friction less track. A child of mass m2 kg runs on the trolley from one end to the other (l m away) with a speed of v2 ms-1 relative to the trolley in a direction opposite to the trolley’s motion, and jumps out of the trolley. How much has the trolley moved from the time the child begins to run?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(m1, v1, m2, v2, l) :
    v = round((m2*v2)/(m1+m2),1) 
    return v + v1

def cal2(m1, v1, m2, v2, l) :
    v = round((m2*v2)/(m1+m2),1) + v1
    t = round(l/v2,1)
    return round(v*t,1)

def type1() :
    m1 = random.randint(1,80)
    v1 = random.randint(1,50)
    m2 = random.randint(1,40)
    v2 = random.randint(1,10)
    l = random.randint(1,20)
    q = "A trolley of mass " + str(m1) + " kg moves with a uniform speed of " + str(v1) + " m/s on a friction less track. A child of mass " + str(m2) + " kg runs on the trolley from one end to the other (" + str(l) + " m away) with a speed of " + str(v2) + " ms-1 relative to the trolley in a direction opposite to the trolley’s motion, and jumps out of the trolley. What is the final speed of the trolley?\n"
    v = str(cal1(m1, v1, m2, v2, l)) + " m/s\n"
    return q,v

def type2() :
    m1 = random.randint(1,80)
    v1 = random.randint(1,50)
    m2 = random.randint(1,40)
    v2 = random.randint(1,10)
    l = random.randint(1,20)
    q = "A trolley of mass " + str(m1) + " kg moves with a uniform speed of " + str(v1) + " m/s on a friction less track. A child of mass " + str(m2) + " kg runs on the trolley from one end to the other (" + str(l) + " m away) with a speed of " + str(v2) + " ms-1 relative to the trolley in a direction opposite to the trolley’s motion, and jumps out of the trolley. How much has the trolley moved from the time the child begins to run?\n"
    s = str(cal2(m1, v1, m2, v2, l)) + " m\n"
    return q,s

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
