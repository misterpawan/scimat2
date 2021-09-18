import random
import math

# A jet plane is travelling towards west at a speed of v kmph. What is the voltage difference developed between the ends of the wing having a span of l m, if the Earth's magnetic field at the location has a magnitude of 5 x 10-4 T and the dip angle is 30 degrees.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

pi = math.pi
bH = 5 * (10**-5)

def cal1(v, l, d) :
    b = bH*math.sin((pi*d)/180)
    v = (v * 5)/18
    return (b*l*v)/2    

def type1() :
    v = random.randint(1000,2000)
    l = random.randint(10,80)
    d = random.randint(1,90)
    q = "A jet plane is travelling towards west at a speed of " + str(v) + " kmph. What is the voltage difference developed between the ends of the wing having a span of " + str(l) + " m, if the Earth's magnetic field at the location has a magnitude of 5 x 10^(-4) T and the dip angle is " + str(d) + " degrees.\n"
    a = "{:.2e}".format(cal1(v, l, d)) + " volt\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
