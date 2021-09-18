import random

# Two absolute scales A and B have triple points of water defined to be 200 A and 350 B. What is the relation between TA and TB 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

r = 8.31

def cal1(t1,t2) :
    return round(t1/t2,2) 

def type1() :
    t1 = random.randint(-200,800)
    t2 = random.randint(-200,800)
    while t2 == 0 :
        t2 = random.randint(-200,800)  
    while t1 == 0 :
        t1 = random.randint(-200,800)  
    q = "Two absolute scales A and B have triple points of water defined to be " + str(t1) + " A and " + str(t2) + " B. What is the relation between TA and TB.\n"
    a = "ta = " + str(cal1(t1,t2)) + "tb\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
