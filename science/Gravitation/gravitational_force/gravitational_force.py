import random

# What is the gravitational force between two masses m1 kg and m2 kg seperated bt a distance r m. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

g =  6.67 * (10**-11)

def cal1(m1, m2, r) :
    return (g*m1*m2)/(r*r)

def type1() :
    m1 = random.randint(1,100)
    m1 = m1 * (10**3)
    m2 = random.randint(1,100)
    m2 = m2 * (10**3)
    R = random.randint(1,100)
    t = random.randint(1,2)
    if t == 1 :
        q = "What is the gravitational force between two masses " + str(m1) + " kg and " + str(m2) + " kg seperated bt a distance " + str(R) + " m.\n"
    else :
        q = "What is the gravitational force between two masses " + str(m1) + " kg and " + str(m2) + " kg seperated bt a distance " + str(R) + " m. G = 6.67 x 10-11\n"
    w = "{:.2e}".format(cal1(m1, m2, R)) + " m/s\n"
    return q,w

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
