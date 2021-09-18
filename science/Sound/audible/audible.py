import random

# A sound wave travels at a speed of v ms-1, if it's wavelength is lambda m, will the sound wave be audible?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    lamb = random.randint(1,50)
    v = (round(random.randint(1,400000)/10,1))*lamb
    ques = "A sound wave travels at a speed of "+str(v)+" m/s, if it's wavelength is "+str(lamb)+" m, will the sound wave be audible ? \n"
    qns.write(ques)
    answer = ""
    if v/lamb > 20 and v/lamb < 20000:
        answer = "audible\n"
    else:
        answer = "not audible\n" 
    ans.write(answer)
    # print(ques)
    # print(answer)
   
qns.close()
ans.close()
