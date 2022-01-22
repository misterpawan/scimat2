import random

# A carrier wave of peak voltage 12 V is used to transmit a message signal. What should be the peak voltage of the modulating signal in order to have a modulation index of 75 percent?
# For an amplitude modulated wave, the maximum amplitude is found to be 10 V while the minimum amplitude is found to be 2 V. Determine the modulation index.

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 10

for i in range(no_of_samples):
    types = random.randint(0,1)
    if types:
        V = round(random.randint(100,40000)/100,2)
        percent = random.randint(1,100)
        q = "A carrier wave of peak voltage "+str(V)+" V is used to transmit a message signal. What should be the peak voltage of the modulating signal in order to have a modulation index of "+str(percent)+" percent?\n"
        a = "we know that modulation index is ratio of voltage of modulating signal to that of voltage of carrier, hence we have mod-index(in decimal) = V_sig/V_car, hence V_sig = mod-index*V_car = "+str(round(percent/100,2))+"*"+str(V)+" = "
        a += "{:.2e} V\n".format((percent/100)*V)
    else:
        A_min = round(random.randint(0,2000)/100,2)
        A_max = round(A_min + random.randint(1,2000)/100,2)
        q = "For an amplitude modulated wave, the maximum amplitude is found to be "+str(A_max)+" V while the minimum amplitude is found to be "+str(A_min)+" V. Determine the modulation index.\n"
        a = "we know that modulation index of amplitude modulated wave is ratio of difference of a_max and a_min and sum of a_max and a_min, difference of a_max, a_min is equal to "+str(A_max)+"-"+str(A_min)+" = "+str(round(A_max-A_min,2))+", sum of a_max, a_min is equal to "+str(A_max)+"+"+str(A_min)+" = "+str(round(A_max+A_min,2))+", hence the modulation index is equal to "+str(round(A_max-A_min,2))+"/"+str(round(A_max+A_min,2))+" = " 
        a += str(round((A_max-A_min)/(A_max+A_min),2)) + "\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()