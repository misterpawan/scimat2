import random
import math

# A closely wounded solenoid l cm long has k layers of windings of n turns each. The diameter of the solenoid is d cm. If the current carried is i A, Estimate the magnitude of b inside the solenoid near its center. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

pi = math.pi
mu = 4*pi*(10**-7)

no_of_samples = 500000

def cal1(k, n, l, i) :
    l = l * (10**-2)
    return (mu*n*i)/(l) 

def type1() :
    n = random.randint(1,10)
    n = n*50
    i = random.randint(1,50)
    k = random.randint(1,10)
    d = random.randint(1,100)
    l = random.randint(10,1000)
    t=random.randint(1,2)
    if t == 1 :
        q = "A closely wounded solenoid " + str(l) + " cm long has " + str(k) + " layers of windings of " + str(n) + " turns each. The diameter of the solenoid is " + str(d) +" cm. If the current carried is " + str(i) + " A, Estimate the magnitude of inside the solenoid near its center. (mu = 4 x pi x 10-7 TmA-1)\n"
    else :
        q = "A closely wounded solenoid " + str(l) + " cm long has " + str(k) + " layers of windings of " + str(n) + " turns each. The diameter of the solenoid is " + str(d) +" cm. If the current carried is " + str(i) + " A, Estimate the magnitude of  inside the solenoid near its center.\n"
    a = "{:.2e}".format(cal1(k,n,l,i)) + " tesla\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
