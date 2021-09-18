import random

# A carrier wave of peak voltage 12 V is used to transmit a message signal. What should be the peak voltage of the modulating signal in order to have a modulation index of 75 percent?
# For an amplitude modulated wave, the maximum amplitude is found to be 10 V while the minimum amplitude is found to be 2 V. Determine the modulation index.

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types:
        V = round(random.randint(100,40000)/100,2)
        percent = random.randint(1,100)
        q = "A carrier wave of peak voltage "+str(V)+" V is used to transmit a message signal. What should be the peak voltage of the modulating signal in order to have a modulation index of "+str(percent)+" percent?\n"
        a = "{:.2e} m2\n".format((percent/100)*V)
    else:
        A_min = round(random.randint(0,2000)/100,2)
        A_max = round(A_min + random.randint(1,2000)/100,2)
        q = "For an amplitude modulated wave, the maximum amplitude is found to be "+str(A_max)+" V while the minimum amplitude is found to be "+str(A_min)+" V. Determine the modulation index.\n"
        a = str(round((A_max-A_min)/(A_max+A_min),2)) + "\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()