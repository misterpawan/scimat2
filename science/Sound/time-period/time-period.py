import random

# The frequency of sound is f Hz.How many times does it vibrate in t seconds?
# A person is listening to a tone of f Hz sitting at a distance of s m from the source
# of the sound. What is the time interval between successive compressions from the source? 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 8

def calculation_vib(f, t): 
    return f * t

def calculation_t(f):
    return round(1000000/f,1)

def type1():
    f = random.randint(1,1000)
    t = random.randint(1,2000)
    num = str(calculation_vib(f,t)) + " \n"
    q = "The frequency of sound is "+str(f)+" Hz.How many times does it vibrate in "+str(t)+" seconds?\n"
    return q,num

def type2():
    f = random.randint(1,1000000)
    s = random.randint(1,200)
    t = str(calculation_t(f)) + " microseconds\n"
    q = "A person is listening to a tone of "+str(f)+" Hz sitting at a distance of "+str(s)+" m from the source of the sound. What is the time interval between successive compressions from the source?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
