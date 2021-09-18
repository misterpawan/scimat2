import random
import math

# In a Youngs double-slit experiment, the slits are seperated by d mm and the screen is placed D m away. The distance between the central bright fringe and the fourth bright fringe is measured to be l cm. Determine the wavelength of the ligth used for the experiment.
# In a Youngs double-slit experiment using monochromatic light of wavelength l, the intensity of light at a point on the screen where path difference is l, is K units. What is the intensity of light at a point where path difference is l/3.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

pi = math.pi

def cal1(n,d,D,l) :
    l = l * (10**-2)
    d = d * (10**-3)
    return (l*d)/(n*D)

def cal2(l, k, d1, d2) :
    i = k/(2*(1+math.cos((2*pi)/d1)))
    return 2*i*(1+math.cos((2*pi)/d2))

def type1() :
    d = random.randint(1,100)
    d = round(d/100,2)
    D = random.randint(1,100)
    D = round(D/10,1)
    l = random.randint(1,10)
    n = random.randint(1,10)
    q = "In a Youngs double-slit experiment, the slits are seperated by " + str(d) + " mm and the screen is placed " + str(D) + " m away. The distance between the central bright fringe and the " + str(n) + " bright fringe is measured to be " + str(l) + " cm. Determine the wavelength of the ligth used for the experiment.\n"
    m = "{:.2e}".format(cal1(n,d, D, l)) + " m\n"
    return q,m

def type2() :
    l = random.randint(1,100)
    k = random.randint(1,100)
    d1 = random.randint(1,10)
    while d1 == 2 :
        d1 = random.randint(1,10)
    d2 = d1
    while d2 == d1 or d2 == 2 :
        d2 = random.randint(1,10)
    q = "In a Youngs double-slit experiment using monochromatic light of wavelength " + str(l) + ", the intensity of light at a point on the screen where path difference is " + str(round(l/d1,1)) + ", is " + str(k) + " units. What is the intensity of light at a point where path difference is " + str(round(l/d2,1)) + ".\n"
    a = "{:.2e}".format(cal2(l, k, d1, d2)) + " units\n"
    return q,a

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
