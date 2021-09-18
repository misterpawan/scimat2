import random

# A sound produces c crests and c troughs in t seconds. When the second crest is produced, 
# the first is s m away from the source, then calculate  

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    c = random.randint(1,2000)
    t = random.randint(1,100)
    s = random.randint(1,2000)
    ques = "A sound produces "+str(c)+" crests and "+str(c)+" troughs in "+str(t)+" seconds. When the first trough is produced, the first crest is "+str(s)+" m away from the source, then calculate "
    types = random.randint(0,3)
    if types == 0:
        ques += "the wavelength ?\n"
        answer = str(2*s) + " m\n"
    if types == 1:
        ques += "the frequency ?\n"
        answer = str(round(c/t,1)) + " hz\n"
    if types == 2:
        ques += "the wave speed ?\n"
        answer = str(round((2*s)/t,1)) + " m/s\n"
    if types == 3:
        ques += "the time period ?\n"
        answer = str(round((t*1000)/c,1)) + " ms\n"
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
