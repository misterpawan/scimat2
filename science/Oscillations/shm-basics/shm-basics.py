import random
import math

# A body describes simple harmonic motion with an amplitude of 5 cm and a period of 0.2 s. Find the acceleration and velocity of the body when the displacement is (a) 5 cm (b) 3 cm (c) 0 cm
# A mass attached to a spring is free to oscillate, with angular velocity w, in a horizontal plane without friction or damping. It is pulled to a distance x0 and pushed towards the centre with a velocity v0 at time t = 0. Determine the amplitude of the resulting oscillations.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

def type2(types):
    t = random.randint(10,200)
    amp = random.randint(0,200)
    amp1 = random.randint(max(amp,1),amp+200)
    qntype = ["velocity","acceleration"]
    q = "A body describes simple harmonic motion with an amplitude of "+str(amp1)+" mm and a period of "+str(t)+" ms. Find the "+qntype[types-2]+" of the body when the displacement is "+str(amp)+" mm?\n"
    w = (2*math.pi*1000)/t
    if types == 2:
        v = w*math.sqrt(amp1**2-amp**2)
        a = "{:.2e}".format(v) + " ms-1\n"
    else:
        acc = w*w*amp
        a = "{:.2e}".format(acc) + " ms-2\n"
    return q,a

def type1():
    x0 = random.randint(10,200)
    v0 = random.randint(10,200)
    w = random.randint(10,200)
    q = "A mass attached to a spring is free to oscillate, with angular velocity "+str(w)+", in a horizontal plane. It is pulled to a distance "+str(x0)+" m and pushed towards the centre with a velocity "+str(v0)+" ms-1 at time t = 0. Determine the amplitude of the resulting oscillations?\n"
    amp = math.sqrt(x0**2+(v0/w)**2)
    a = "{:.2e}".format(amp) + " m\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        q,a = type1()
    else:
        q,a = type2(types)
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()