import random
import math

# A 100 ohm resistor is connected to a 220 V, 50 Hz ac supply. What is the rms value of current in the circuit?
# A 100 ohm resistor is connected to a 220 V, 50 Hz ac supply. What is the net power consumed over a full cycle?
# A 44 mH inductor is connected to 220 V, 50 Hz ac supply. Determine the rms value of the current in the circuit?
# A 60 microfarad capacitor is connected to a 110 V, 60 Hz ac supply. Determine the rms value of the current in the circuit?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 2000000
pi = math.pi

for i in range(no_of_samples):
    types = random.randint(1,4)
    val = random.randint(1,200)
    V = random.randint(20,250)
    freq = random.randint(1,200)
    if types == 1:
        q = "A "+str(val)+" ohm resistor is connected to a "+str(V)+" V, "+str(freq)+" Hz ac supply. What is the rms value of current in the circuit?\n"
        a = "{:.2e} ampere\n".format(V/val)
    elif types == 2:
        q = "A "+str(val)+" ohm resistor is connected to a "+str(V)+" V, "+str(freq)+" Hz ac supply. What is the net power consumed over a full cycle?\n"
        a = "{:.2e} watt\n".format((V*V)/val)
    elif types == 3:
        q = "A "+str(val)+" mH inductor is connected to a "+str(V)+" V, "+str(freq)+" Hz ac supply. Determine the rms value of current in the circuit?\n"
        xl = 2*pi*val*0.001*freq
        a = "{:.2e} ampere\n".format(V/xl)
    elif types == 4:
        q = "A "+str(val)+" microfarad capacitor is connected to a "+str(V)+" V, "+str(freq)+" Hz ac supply. Determine the rms value of current in the circuit?\n"
        xc_inverse = 2*pi*val*freq*0.000001
        a = "{:.2e} ampere\n".format(V*xc_inverse)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()