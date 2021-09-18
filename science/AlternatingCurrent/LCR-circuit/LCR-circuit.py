import random
import math

# A series LCR circuit is connected to a variable frequency 230 V source with L = 5 H, C = 80 muF, R = 40 ohm.

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 3000000

for i in range(no_of_samples):
    L = random.randint(1,200)
    C = random.randint(1,200)
    R = random.randint(1,200)
    q = "A series LCR circuit is connected to a variable frequency 230 V source with L = "+str(L)+" H, C = "+str(C)+" muF, R = "+str(R)+" ohm. "
    types = random.randint(1,16)
    if types>=1 and types<=3:
        q = q + "Determine the source frequency which drives the circuit in resonance?\n"
        a = str(round((1/math.sqrt(L*C*0.000001)),1))+" rad/s\n"
    elif types == 4:
        q = q + "Determine the impedence of the circuit at the resonating frequency?\n"
        a = str(R) + " ohm\n"
    elif types>=5 and types<=7:
        q = q + "Determine the amplitude of current at the resonating frequency?\n"
        a = str(round((230*math.sqrt(2))/R,1))+ " ampere\n"
    elif types == 8:
        q = q + "Determine the rms potential drop across resistance?\n"
        a = "230 volt\n"
    elif types>=9 and types<=12:
        q = q + "Determine the rms potential drop across inductance?\n"
        vl = (230/R)*(1/math.sqrt(L*C*0.000001))*L
        a = "{:.2e} volt\n".format(vl)
    elif types>=13 and types<=16:
        q = q + "Determine the rms potential drop across capacitance?\n"
        vc = (230/R)*(1/math.sqrt(L*C*0.000001))*L
        a = "{:.2e} volt\n".format(vc) 
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()