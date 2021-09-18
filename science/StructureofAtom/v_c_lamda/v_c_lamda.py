from mendeleev import element
import random


# Light emitted from a lamp has a wavelength of w nm. Calculate the frequency of the light.
# Light emitted from a lamp has a wavelength of w nm. Calculate the frequency of the light. (c=10^8m/s)
# Light emitted from a lamp has a frequency of v sec-1. Calculate the wavelength of the light.
# Light emitted from a lamp has a frequency of v sec-1. Calculate the wavelength of the light. (c=10^8m/s)
# Light emitted from a lamp has a wavelength of w nm. Calculate the wave number of the light.
# Light emitted from a lamp has a wave number of w nm-1. Calculate the wavelength of the light.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 3000000

def cal1(w) :
   ans = round(300000000/w,2)
   ans = ans*(1000000000)
   return ans

def cal2(w) :
    return round(1000000000/w,2)

def type1() :
    w = random.randint(1,1000000)
    w = round(w/10,2)
    q = "Light emitted from a lamp has a wavelength of " + str(w) + " nm. Calculate the frequency of the light.\n"
    v = "{:.2e}".format(cal1(w)) + "sec-1\n"
    return q,v

def type2() :
    w = random.randint(1,1000000)
    w = round(w/10,2)
    q = "Light emitted from a lamp has a wavelength of " + str(w) + " nm. Calculate the frequency of the light. (c=10^8m/s)\n"
    v = "{:.2e}".format(cal1(w)) + "sec-1\n"
    return q,v

def type3() :
    w = random.randint(1,1000000)
    w = round(w/10,2)
    q = "Light emitted from a lamp has a wavelength of " + str(w) + " nm. Calculate the wave number of the light.\n"
    v = "{:.2e}".format(cal2(w)) + "m-1\n"
    return q,v

def type4() :
    w = random.randint(1,1000000)
    q = "Light emitted from a lamp has a wave number of " + str(w) + " nm-1. Calculate the wavelength of the light.\n"
    v = "{:.2e}".format(cal2(w)) + "nm-1\n"
    return q,v

def type5() :
    v = random.randint(1,1000000)
    q = "Light emitted from a lamp has a frequency of " + str(v) + " sec-1. Calculate the wavelength of the light.\n"
    w = "{:.2e}".format(cal1(v)) + "sec-1\n"
    return q,w

def type6() :
    v = random.randint(1,1000000)
    q = "Light emitted from a lamp has a frequency of " + str(v) + " sec-1. Calculate the wavelength of the light. (c=10^8m/s)\n"
    w = "{:.2e}".format(cal1(v)) + "sec-1\n"
    return q,w

for i in range(no_of_samples):
    types = random.randint(1,6)
    if types == 1 :
        ques,answer = type1()
    elif types == 2 :
        ques,answer = type2()
    elif types == 3 :
        ques,answer = type3()
    elif types == 4 :
        ques,answer = type4()
    elif types == 5 :
        ques,answer = type5()
    else:
        ques,answer = type6()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
