import random

# A steel rod 100 cm long is clamped at its middle. The fundamental frequency of longitudinal vibrations of the rod is given to be 2.53 k Hz. What is the speed of sound in steel?
# A pipe 20 cm long is closed at one end. Which harmonic mode of the pipe is resonantly excited by a 430 Hz source? Will the same source be in resonance with the pipe if both ends are open? (speed of sound in air is 340 ms-1).

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        l = random.randint(10,2000)
        freq = random.randint(1000,3000)
        an = (2*l*freq)/100
        q = "A steel rod "+str(l)+" cm long is hinged at its middle. The fundamental frequency of longitudinal vibrations of the rod is given to be "+str(freq)+" Hz. What is the speed of sound in steel?\n"
        a = "{:.1e}".format(an) + " ms-1\n"
    else:
        l = random.randint(10,200)
        f = random.randint(100,600)
        speed = random.randint(320,360)
        q = "A pipe "+str(l)+" cm long is closed at one end. Which harmonic mode of the pipe is resonantly excited by a "+str(f)+" Hz source? Will the same source be in resonance with the pipe if both ends are open? (speed of sound in air is "+str(speed)+" ms-1).\n"
        temp = (4*f*(l/100))/speed
        temp = (temp+1)/2
        if abs(temp-round(temp))<0.01:
            a = "resonance in first case with "+str(round(temp))+", "
        else:
            a = "no resonance in first case, "
        temp = (2*f*(l/100))/speed
        if abs(temp-round(temp))<0.01:
            a = a +"resonance in second case with "+str(round(temp))+"\n"
        else:
            a = a +"no resonance in second case\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()