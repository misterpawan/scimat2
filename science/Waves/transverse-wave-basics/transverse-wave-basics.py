import random
import math

# A transverse harmonic wave on a string is described by y(x, t) = 3.0 sin (36 t + 0.018 x + π/4) where x and y are in cm and t in s. The positive direction of x is from left to right.
# (a) Is this a travelling wave or a stationary wave? If it is travelling, what are the speed and direction of its propagation ?
# (b) What are its amplitude and frequency?
# (c) What is the initial phase at the origin?
# (d) What is the least distance between two successive crests in the wave?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 20

for i in range(no_of_samples):
    amp = random.randint(1,50)
    w = random.randint(1,100)
    k = round(random.randint(1,200)/1000,3)
    div = random.randint(2,10)
    q = "A transverse harmonic wave on a string is described by y(x, t) = "+str(amp)+" sin ("+str(w)+" t + "+str(k)+" x + π/"+str(div)+") where x and y are in cm and t in s. The positive direction of x is from left to right, "
    types = random.randint(1,5)
    if types == 1:
        q = q + "is this a travelling wave or a stationary wave? If it is travelling, what are the speed and direction of its propagation ?\n"
        a = "it is a travelling wave, it is travelling in -ve x direction with "+"{:.2e}".format(w/k)+" ms-1\n"
    elif types == 2:
        q = q + "then what is value of amplitude?\n"
        a = str(round(amp/100,2))+" m\n"
    elif types == 3:
        q = q + "then what is the value of frequency?\n"
        a = str(round(w/(2*math.pi),1)) + " hertz\n"
    elif types == 4:
        q = q + "then what is the initial phase at the origin?\n"
        a = "π/"+str(div)+"\n"
    else:
        q = q +"then what is the least distance between two successive crests/troughs in the wave?\n"
        a = str(round((2*math.pi)/k,1))+" m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()