import random

# What is the number of photons of light with wavelength w pm which provide e Joule of energy ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
h = 6.6 * (10**-34)
c = 3 * (10**8)

def cal1(e,w) :
   return e*w*(10**-12)/(h*c)

def type1() :
    w = random.randint(100,1000000)
    e = random.randint(1,100)
    q = "What is the number of photons of light with wavelength " + str(w) + " pm which provide " + str(e) + " Joule of energy ? \n"
    n = "{:.2e}".format(cal1(e,w)) + "\n"
    return q,n

def type2() :
    w = random.randint(100,1000000)
    e = random.randint(1,100)
    q = "What is the number of photons of light with wavelength " + str(w) + " pm which provide " + str(e) + " Joule of energy ? (h = 6.6 * 10^-34 Js, c = 3 * 10^8 m/s)\n"
    n = "{:.2e}".format(cal1(e,w)) + "\n"
    return q,n

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques,answer = type1()
    elif types == 2 :
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
