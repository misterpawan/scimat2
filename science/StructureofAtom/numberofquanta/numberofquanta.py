import random

# A p watt bulb emits monochromatic yellow light of wavelength w pm. Calculate the rate of emission of quanta per second.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
h = 6.6 * (10**-34)
c = 3 * (10**8)

def cal1(p,w) :
   return p*w*(10**-12)/(h*c)

for i in range(no_of_samples):
    p = random.randint(1,100)
    w = random.randint(1,1000000)
    ques = "A " + str(p) + " watt bulb emits monochromatic yellow light of wavelength " + str(w) + " pm. Calculate the rate of emission of quanta per second.\n"
    answer = "{:.2e}".format(cal1(p,w)) + "per second\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
