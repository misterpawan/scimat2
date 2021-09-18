import random
import math

# If a particle is in linear SHM with w = w, amplitude A then find average kinetic energy over a period.
# If a particle is in linear SHM with w = w, amplitude A then find average poten energy over a period.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(10,200)*10
    w = random.randint(10,200)
    amp = random.randint(10,200)
    types = random.randint(0,1)
    qn_type = ["kinetic","potential"]
    q = "If a particle of mass "+str(m)+" g is in linear SHM with w = "+str(w)+", amplitude "+str(amp)+" cm then find average "+qn_type[types]+" energy over a period.\n"
    a = "{:.2e}".format(0.25*m*0.001*w*w*amp*amp*0.0001)+" joule\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()