import random
import math

# In a chamber, a uniform magnetic field of b T is maintained. An electron is shoot into in the field with a speed of v m/s making an angle of d degrees with the field. Determine the radius of the circular path of the electron.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

m = 9.1 * (10**-31)
e = 1.6 * (10**-19)
pi = math.pi

def cal1(b, v, d) :
    d = math.sin((d*pi)/180)
    return (m*v)/(b*e*d)

def type1() :
    b = random.randint(1,120)
    b = b*(10**-4)
    v = random.randint(1,120)
    v = v*(10**6)
    d = random.randint(1,90)
    q = "In a chamber, a uniform magnetic field of " + str(b) + " T is maintained. An electron is shoot into in the field with a speed of " + str(v) + " m/s making an angle of " + str(d) + " degrees with the field. Determine the radius of the circular path of the electron.\n"
    a = "{:.2e}".format(cal1(b,v,d)) + " m\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,1)
    if types == 1 :
        ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
