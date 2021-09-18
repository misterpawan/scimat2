import random

# A steam engine delivers w J of work per minute and services h J of heat per minute from its boiler. What is the efficiency of the engine? 
# A steam engine delivers w J of work per minute and services h J of heat per minute from its boiler. How much heat is wasted per minute?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

r = 8.31

def cal1(w,h) :
    return round((w*100)/h,1) 

def cal2(w,h) : 
    return h-w

def type1() :
    w = random.randint(1,1000)
    h = random.randint(w+1,w+1000)
    q = "A steam engine delivers " + str(w) + " J of work per minute and services " + str(h) + " J of heat per minute from its boiler. What is the efficiency of the engine?\n"
    a = str(cal1(w,h)) + "\n"
    return q,a

def type2() :
    w = random.randint(1,1000)
    h = random.randint(w+1,w+1000)
    q = "A steam engine delivers " + str(w) + " J of work per minute and services " + str(h) + " J of heat per minute from its boiler. How much heat is wasted per minute?\n"
    a = str(cal2(w,h)) + " joules\n"
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
