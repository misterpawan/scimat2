import random
import math

# A end of string of mu = 8.0 x 10-3 kgm-1 is connected to tuning fork of nu = 256 Hz. The other end passes over a pulley and is tied to a mass of 90 kg. The pulley end is such that reflected waves at this end have negligible amplitude. At t = 0, the fork end of the string x = 0 has y = 0 and is moving along +ve y axis. The amplitude of the wave is 5.0 cm. Write down y as function of x and t that describes the wave on the string.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    freq = random.randint(100,500)
    mu = round(random.randint(1,30)/1000,3)
    amp = random.randint(1,40)
    m = random.randint(10,20)*5
    q = "A end of string of mu = "+str(mu)+" kgm-1 is connected to tuning fork of nu = "+str(freq)+" Hz. The other end passes over a pulley and is tied to a mass of "+str(m)+" kg. The pulley end is such that reflected waves at this end have negligible amplitude. At t = 0, the fork end of the string x = 0 has y = 0 and is moving along +ve y axis. The amplitude of the wave is "+str(amp)+" cm. Write down y as function of x,t that describes the wave on the string.\n"
    v = math.sqrt((m*9.8)/mu)
    w = 2*math.pi*v
    lamda = v/freq
    k = (2*math.pi)/lamda
    a = str(round(amp/100,2))+" sin("+"{:.1e}".format(w)+"t - "+"{:.1e}".format(k)+"x)"+"\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()