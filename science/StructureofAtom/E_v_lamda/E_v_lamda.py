import random

# Calculate the energy of each of the photons which correspond to light of frequency v Hz.
# Calculate the energy of each of the photons which correspond to light of frequency v Hz. (h = 6.6 * 10^-34 Js)
# Calculate the energy of each of the photons which have wavelength of w nm.
# Calculate the energy of each of the photons which have wavelength of w nm. (h = 6.6 * 10^-34 Js, c = 3 * 10^8 m/s)

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 2000000
h = 6.6 * (10**-34)
c = 3 * (10**8)

def cal1(w) :
   return h*w

def cal2(w) :
    return (h*c)*(10**9)/w

def type1() :
    v = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which correspond to light of frequency " + str(v) + " Hz.\n"
    e = "{:.2e}".format(cal1(v)) + "joules\n"
    return q,e

def type2() :
    w = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which have wavelength of " + str(w) + " nm.\n"
    e = "{:.2e}".format(cal2(w)) + "joules\n"
    return q,e

def type3() :
    v = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which correspond to light of frequency " + str(v) + " Hz. (h = 6.6 * 10^-34 Js)\n"
    e = "{:.2e}".format(cal1(v)) + "joules\n"
    return q,e

def type4() :
    w = random.randint(1,1000000)
    q = "Calculate the energy of each of the photons which have wavelength of " + str(w) + " nm. (h = 6.6 * 10^-34 Js, c = 3 * 10^8 m/s)\n"
    e = "{:.2e}".format(cal2(w)) + "joules\n"
    return q,e

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1 :
        ques,answer = type1()
    elif types == 2 :
        ques,answer = type2()
    elif types == 3 :
        ques,answer = type3()
    elif types == 4 :
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
