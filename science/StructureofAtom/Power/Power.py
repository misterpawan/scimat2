
from mendeleev import element
import random

# Nitrogen laser produces radiation of wavelength of w nm. If the number of photons emitted is n, calculate the power of this laser.
# Nitrogen laser produces radiation of wavelength of w nm. If the number of photons emitted is n, calculate the power of this laser. ( h = 6.6 * 10^-34Js, c = 3 * 10^8m/s)

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000
h = 6.6 * (10**-34)
c = 3 * 10**8
names = []
for i in range(1,118) :
   names.append(element(i))

for i in range(no_of_samples):
    ele = random.randint(1,117)
    ele_name = names[ele-1]
    n = random.randint(1,10000)
    w = random.randint(1,1000)
    types = random.randint(1,2)
    if types == 1 :
       ques = str(ele_name) + " laser produces radiation of wavelength of " + str(w) + " nm. If the number of photons emitted is " + str(n) + ", calculate the power of this laser.\n"
    else :
       ques = str(ele_name) + " laser produces radiation of wavelength of " + str(w) + " nm. If the number of photons emitted is " + str(n) + ", calculate the power of this laser.( h = 6.6 * 10^-34Js, c = 3 * 10^8m/s)\n" 
    n = n * 10**21
    w = w * 10**-9
    answ = round(h*c*n/w,2)
    answer = str(answ) + "\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
