import random
import math

# A coil of inductance 0.5 H and resistance 100 ohm is connected to a 240V, 50 Hz ac supply. What is the time lag between voltage maximum and current maximum?
# A 100 muF capacitor in series with a 40 ohm resistance is connected to a 110V, 60 Hz supply. What is the time lag between the current maximum and voltage maximum?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        L = round(random.randint(20,80)/100,2)
        R = random.randint(50,250)
        V = random.randint(220,240)
        f = random.randint(20,80)
        q = "A coil of inductance "+str(L)+" H and resistance "+str(R)+" ohm is connected to a "+str(V)+" V, "+str(f)+" Hz ac supply. What is the time lag between voltage maximum and current maximum?\n"
        a = "{:.2e} s\n".format(math.atan((f*L*2*math.pi)/R)/(2*math.pi*f))
    else:
        C = random.randint(20,220)
        R = random.randint(10,50)
        V = random.randint(220,240)
        f = random.randint(20,80)
        q = "A "+str(C)+" muF capacitor in series with a "+str(R)+" ohm resistance is connected to a "+str(V)+" V, "+str(f)+" Hz supply. What is the time lag between the current maximum and voltage maximum?\n"
        a = "{:.2e} s\n".format(math.atan(1/(f*C*(10**(-6))*2*math.pi*R))/(2*math.pi*f))
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()