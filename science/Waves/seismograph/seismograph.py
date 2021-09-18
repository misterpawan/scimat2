import random

# Earthquakes generate sound waves inside the earth. Unlike a gas, the earth can experience both transverse (S) and longitudinal (P) sound waves. Typically the speed of S wave is about 4.0 km s-1 . A seismograph records P and S waves from an earthquake. The first P wave arrives 4 min before the first S wave. Assuming the waves travel in straight line, at what distance does the earthquake occur?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    speed_s = random.randint(100,700)*10
    diff_speed_v = random.randint(20,90)*10
    time = random.randint(20,220)*2
    q = "Earthquakes generate sound waves inside the earth, assuming the speed of transverse(S) wave is "+str(speed_s)+" ms-1, speed of longitudinal(P) wave is "+str(speed_s+diff_speed_v)+" ms-1, if the first P wave arrives "+str(time)+" s before the first S wave to seismograph, at what distance does the earthquake occur?\n"
    a = "{:.2e}".format((time*speed_s*(speed_s+diff_speed_v))/(diff_speed_v*1000))+" km\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()