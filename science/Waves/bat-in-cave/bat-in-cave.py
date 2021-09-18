import random
import math

# A bat is flitting about in a cave, navigating via ultrasonic beeps. Assume that the sound emission frequency of the bat is 40 kHz. During one fast swoop directly toward a flat wall surface, the bat is moving at 0.03 times the speed of sound in air. What frequency does the bat hear reflected off the wall ?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    freq = random.randint(1000,6000)*10
    ratio = round(random.randint(200,2000)/10000,4)
    q = "A bat is flitting about in a cave, navigating via ultrasonic beeps. Assume that the sound emission frequency of the bat is "+str(freq)+" Hz. During one fast swoop directly toward a flat wall surface, the bat is moving at "+str(ratio)+" times the speed of sound in air. "
    types = random.randint(1,2)
    if types == 1:
        q = q + "What is the apparent frequency of the sound striking the wall?\n"
        app_freq = (1/(1-ratio))*freq
    else:
        q = q + "What frequency does the bat hear reflected off the wall?\n"
        app_freq = ((1+ratio)/(1-ratio))*freq
    a = "{:.2e}".format(app_freq) + " hertz\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()