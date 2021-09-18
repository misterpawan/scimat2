import random
import math

# A circular disc, of mass 10 kg, is suspended by a wire attached to its centre. The wire is twisted by rotating the disc and released. The period of torsional oscillations of found to be 1.5 s. The radius of the disc is 15 cm. Determine the torsional spring constant of the wire.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    m = random.randint(100,2000)*10
    t = random.randint(10,200)*10
    r = random.randint(10,30)
    q = "A circular disc, of mass "+str(m)+" g, is suspended by a wire attached to its centre. The wire is twisted by rotating the disc and released. If period of torsional oscillations is "+str(t)+" ms. The radius of the disc is "+str(r)+" cm. Determine the torsional spring constant of the wire.\n"
    alpha = 2*math.pi*math.pi*(m/1000)*(r/100)*(r/100)*(1000/t)*(1000/t)
    a = "{:.2e}".format(alpha)+" newton-m rad-1\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()