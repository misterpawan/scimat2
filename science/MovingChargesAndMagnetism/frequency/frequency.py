import random
import math

# In a chamber, auniform magnetic field of b T is maintained. An electron is shoot into in the field with a speed of v m/s making an angle of d degrees with the field. Determine the fequency of the revolution of the electron.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

m = 9.1 * (10**-31)
e = 1.6 * (10**-19)
pi = math.pi

def cal1(b, v, d) :
    return (b*e)/(2*pi*m)

def type1() :
    b = random.randint(1,120)
    b = b*(10**-4)
    v = random.randint(1,120)
    v = v*(10**6)
    d = random.randint(1,90)
    q = "In a chamber, auniform magnetic field of " + str(b) + " T is maintained. An electron is shoot into in the field with a speed of " + str(v) + " m/s making an angle of " + str(d) + " degrees with the field. Determine the fequency of the revolution of the electron.\n"
    v = "{:.2e}".format(cal1(b,v,d)) + " sec-1\n"
    return q,v

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    ans.write(answer)

qns.close()
ans.close()
