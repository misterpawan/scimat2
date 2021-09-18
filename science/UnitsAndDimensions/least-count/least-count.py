import random

# Which of the following is the most precise device for measuring length:

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 10
for i in range(no_of_samples):
    div_ver = random.randint(1,4000)
    pitch = random.randint(1,10)
    div_guage = random.randint(100,10000)
    ques = "Which of the following is the most precise device for measuring length: (a) a vernier callipers with "+str(div_ver)+" divisions on the sliding scale, (b) a screw guage of pitch "+str(pitch)+" mm and "+str(div_guage)+" divisions on the circular scale, (c) an optical instrument that can measure length to within a wavelength of light?\n"
    answer = ""
    ans_prob = [1/(div_ver*1000),pitch/(1000*div_guage),6*(10**(-7))]
    temp = ans_prob.index(min(ans_prob))
    # print(ans_prob,temp)
    if temp == 0:
        answer = '(a)\n'
    elif temp == 1:
        answer = '(b)\n'
    elif temp == 2:
        answer = '(c)\n'
    # print(ques,answer)
    qns.write(ques)
    ans.write(answer)
qns.close()
ans.close()