import random
import math

# In Mullikan’s oil drop experiment, what is the terminal speed of an uncharged drop of radius 2.0 x 10^(-5) m and density 1.2 x 10^3 kg m-3?
# In Mullikan’s oil drop experiment, what is the viscous force on the drop of radius 2.0 x 10^(-5) m and density 1.2 x 10^3 kg m-3 at terminal speed?.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    r = random.randint(1,2000)
    den = random.randint(1000,3000)
    vt = (2/(9*1.8*(10**(-5))))*(r*r*den*9.8*(10**(-12)))
    q = "In Mullikan’s oil drop experiment, what is the terminal speed of an uncharged drop of radius "+str(r)+" x 10^(-6) m and density "+str(den)+" kg m-3?\n"
    if random.randint(0,1):
        q = "In Mullikan’s oil drop experiment, what is the viscous force on the drop of radius "+str(r)+" x 10^(-6) m and density "+str(den)+" kg m-3 at terminal speed?\n"
        a = 6*math.pi*(1.8*(10**(-5)))*r*(10**(-6))*vt
        a = "{:.2e}".format(a) + " newton\n"
    else:
        a = "{:.2e}".format(vt) + " ms-1\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()