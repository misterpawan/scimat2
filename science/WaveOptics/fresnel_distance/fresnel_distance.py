import random

# Estimate the distance for which ray optics is good approximation for an aperture of d mm and wavelength l nm.
# Two towers on top of two hills are d km apart. The line joining them passes l m above a hill halfway between the towers. What is the longest wavelength of radio waves, which can be sent between the two towers without appreciable diffraction effects. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 20000

def type1() :
    d = random.randint(1,20)
    l = random.randint(1,1000)
    q = "Estimate the distance for which ray optics is good approximation for an aperture of " + str(d) + " mm and wavelength " + str(l) + " nm.\n"
    l = l *(10**-9)
    a = "{:.2e}".format((d*d)/l) + " m\n"
    return q,a 

def type2() :
    d = random.randint(1,100)
    l = random.randint(1,200)
    q = "Two towers on top of two hills are " + str(d) + " km apart. The line joining them passes " + str(l) + " m above a hill halfway between the towers. What is the longest wavelength of radio waves, which can be sent between the two towers without appreciable diffraction effects.\n"
    d = d * (10**3)
    a = "{:.2e}".format((l*l)/d) + " m\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,2) 
    if types == 1 :
        ques,answer = type1()
    else :
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
