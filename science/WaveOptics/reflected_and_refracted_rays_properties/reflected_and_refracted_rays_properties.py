import random
import math

# Monochromatic light of wavelength of l nm is incident on aa surface of refractive index mu. What is the wavelength, speed and frequenct of reflected light.
# Monochromatic light of wavelength of l nm is incident on aa surface of refractive index mu. What is the wavelength, speed and frequenct of refracted light.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

c = 3 * (10**8)

for i in range(no_of_samples):
    l = random.randint(1,10000)
    mu = random.randint(101,200)
    mu = round(mu/100,2)
    mu = round(l/10,1)
    t = random.randint(1,2)
    if t == 1 :
        ques = "Monochromatic light of wavelength of " + str(l) + " nm is incident on aa surface of refractive index " + str(mu) + ". What is the wavelength, speed and frequenct of reflected light.\n"
        l = l * (10**-9)
        answ1 = str(l/(10**-9)) + " nm "
        answ3 = "{:.2e}".format((c/l)) + " hz "
        answ2 = "{:.2e}".format(c) + " m/s " 
    else :
        ques = "Monochromatic light of wavelength of " + str(l) + " nm is incident on aa surface of refractive index " + str(mu) + ". What is the wavelength, speed and frequenct of refracyed light.\n"
        v = c/mu
        l = l * (10**-9)
        answ3 = "{:.2e}".format((c/l)) + " hz "
        answ2 = "{:.2e}".format(v) + " m/s " 
        answ1 = "{:.2e}".format(((v*l)/(c*(10**-9)))) + " nm "
    answer = answ1 + ", " + answ2 + "and " + answ3 + "\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
