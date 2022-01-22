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
        des = "source frequency  = 1/sqrt(l*c) = 1/sqrt("+str(L)+"*"+str(round(C*(10**(-6)),10))+") = "+str(round((1/math.sqrt(L*C*0.000001)),1))+" rad/s\n"
    elif types == 4:
        q = q + "Determine the impedence of the circuit at the resonating frequency?\n"
        des = "impedence = sqrt(r^2+(w*l - 1/(w*c)^2)), but at resonating frequency, w*l = 1/(w*c), hence w*l-1/(w*c) = 0, which implies impedence = r = "+str(R)+" ohm\n"
    elif types>=5 and types<=7:
        q = q + "Determine the amplitude of current at the resonating frequency?\n"
        des = "i_amp = v_amp/impedence = v_avg*sqrt(2)/r (we know that v_amp = v_avg*sqrt(2), impedence is r at resonating frequency) => i_amp = 230*sqrt(2)/"+str(R)+" = "+str(round((230*math.sqrt(2))/R,1))+ " ampere\n"
    elif types == 8:
        q = q + "Determine the rms potential drop across resistance?\n"
        des = "at the resonating frequency, potential drop across the inductor is balanced by the potential drop across the capacitor, hence total potential of the circuit is same as potential drop at resistance which is equal to 230 volt\n"
    elif types>=9 and types<=12:
        q = q + "Determine the rms potential drop across inductance?\n"
        vl = (230/R)*(1/math.sqrt(L*C*0.000001))*L
        des = "(v_l)rms = i*w_r*l, where i is rms current = i_0/sqrt(2) = v/r = 230/"+str(R)+", potential drop across inductor = 230/"+str(R)+"*"+str(round((1/math.sqrt(L*C*0.000001)),1))+"*"+str(L)+" = "+"{:.2e} volt\n".format(vl)
    elif types>=13 and types<=16:
        q = q + "Determine the rms potential drop across capacitance?\n"
        vc = (230/R)*(1/math.sqrt(L*C*0.000001))*L
        des = "(v_c)rms = i*1/(w_r*c), where i is rms current = i_0/sqrt(2) = v/r = 230/"+str(R)+", potential drop across capacitor = (230/"+str(R)+")*(1/("+str(round((1/math.sqrt(L*C*0.000001)),1))+"*"+str(C)+")) = "+"{:.2e} volt\n".format(vc)
    qns.write(q)
    ans.write(des)

qns.close()
ans.close()