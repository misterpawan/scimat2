import random

# A sonar device on a submarine sends out a signal and receives an echo t s later. Find the speed of sound in that material if the distance of the object from the submarine is s m ?
# A sonar device on a submarine sends out a signal. Find the time after which echo is received if speed of sound in that material is v m/s and distance of the object from the submarine is s m ?
# A sonar device on a submarine sends out a signal and receives an echo t s later. Find the distance of the object from the submarine if speed of sound in that material is v m/s ?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 10

def calculation_s(v, t): 
    return round(v * (t/2), 1)

def calculation_v(s, t):
    return round((2*s) / t, 1)

def calculation_t(s, v):
    return round((2*s) / v, 1)

def type1():
    v = random.randint(1,1000)
    t = random.randint(1,1000)
    s = "if s is the distance between object and submarine, then wave will travel 2*s(s to reach the object, s for return) distance for echo to be listened, we know that distance = v*t, given v = "+str(v)+", t = "+str(t)+", we get 2*s = "+str(v*t)+", we get s = "+str(calculation_s(v,t)) + " m\n"
    q = "A sonar device on a submarine sends out a signal and receives an echo "+str(t)+" s later. Find the distance of the object from the submarine if speed of sound in that material is "+str(v)+" m/s ?\n"
    return q,s

def type2():
    s = random.randint(4000,5000)
    t = random.randint(1,1000)
    v = "if s is the distance between object and submarine, then wave will travel 2*s(s to reach the object, s for return) distance for echo to be listened, we know that distance = v*t, given s = "+str(s)+", t = "+str(t)+", we get 2*"+str(s)+" = v*"+str(t)+", we get v = "+str(calculation_v(s,t)) + " m/s\n"
    q = "A sonar device on a submarine sends out a signal and receives an echo "+str(t)+" s later. Find the speed of sound in that material if the distance of the object from the submarine is "+str(s)+" m ?\n"
    return q,v

def type3():
    s = random.randint(4000,5000)
    v = random.randint(1,1000)
    t = "if s is the distance between object and submarine, then wave will travel 2*s(s to reach the object, s for return) distance for echo to be listened, we know that distance = v*t, given s = "+str(s)+", v = "+str(v)+", we get 2*"+str(s)+" = t*"+str(v)+", we get t = "+str(calculation_t(s,v)) + " s\n"
    q = "A sonar device on a submarine sends out a signal. Find the time after which echo is received if speed of sound in that material is "+str(v)+" m/s and distance of the object from the submarine is "+str(s)+" m ?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
