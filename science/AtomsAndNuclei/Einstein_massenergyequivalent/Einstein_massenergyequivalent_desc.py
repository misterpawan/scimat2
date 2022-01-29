import random

# What is the energy associated with a mass of m g ?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

c = 3 * (10**8)

no_of_samples = 10000

for i in range(no_of_samples):
    m = random.randint(1,10000)
    m = round(m/10,1)
    t = random.randint(1,2)
    if t == 1 :
        ques = "What is the energy associated with a mass of " + str(m) + " g ?\n"
    else :
        ques = "What is the energy associated with a mass of " + str(m) + " g ? (c = 3 x 10^8 m/s)\n"
    m = m * (10**-3)
    answ = "{:.2e}".format(m*c*c)
    answer = "we know that the energy associated with mass m is, e = m x c^2 = " + str(m) + " x 10^-3 x (3 x 10^8)^2 = " + answ + "joule\n"
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
