import random
import math

# A string of mass 2.50 kg is under a tension of 200 N. The length of the stretched string is 20.0 m. If the transverse jerk is struck at one end of the string, how long does the disturbance take to reach the other end?
# A steel wire has a length of 12.0 m and a mass of 2.10 kg. What should be the tension in the wire so that speed of a transverse wave on the wire equals the speed of sound in dry air at 2 0°C = 340 ms-1.
# A wire stretched between two rigid supports vibrates in its fundamental mode with a frequency of 45 Hz. The mass of the wire is 3.5 x 10-2 kg and its linear mass density is 4.0 x 10-2 kg m-3. What is (a) the speed of a transverse wave on the string, and (b) the tension in the string?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 20

def type1():
    m = random.randint(1,100)
    l = random.randint(1,100)
    t = random.randint(1,800)
    q = "A string of mass "+str(m)+" kg is under a tension of "+str(t)+" N. The length of the stretched string is "+str(l)+" m. If the transverse jerk is struck at one end of the string, how long does the disturbance take to reach the other end?\n"
    v = math.sqrt(t*l/m)
    time = l/v
    a = "{:.2e}".format(time) + " s\n"
    return q,a

def type2():
    l = random.randint(1,400)
    m = random.randint(1,400)
    temp = random.randint(15,35)
    q = "A steel wire has a length of "+str(l)+" m and a mass of "+str(m)+" kg. What should be the tension in the wire so that speed of a transverse wave on the wire equals the speed of sound in dry air at "+str(temp)+" degree C = 340 ms-1.\n"
    T = (340*340)*(m/l)
    a = "{:.2e}".format(T) + " newton\n"
    return q,a

def type3(types):
    f = random.randint(1,200)
    m = round(random.randint(1,200)/1000,3)
    mu = round(random.randint(1,200)/1000,3)
    q = "A wire stretched between two rigid supports vibrates in its fundamental mode with a frequency of "+str(f)+" Hz. The mass of the wire is "+str(m)+" kg and its linear mass density is "+str(mu)+" kg m-3. What is "
    l = m/mu
    lamda = 2*l
    speed = f*lamda
    if types == 3:
        q = q + "the speed of a transverse wave on the string?\n"
        a = "{:.2e}".format(speed) + " ms-1\n"
    else:
        q = q + "the tension in the string?\n"
        a = "{:.2e}".format(speed*speed*mu) + " newton\n"
    return q,a
        
    
for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1:
        q,a = type1()
    elif types == 2:
        q,a = type2()
    else:
        q,a = type3(types)
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()