import random


# An electric appliance of P W power rating is operated in a domestic electric circuit of V V that has a current rating of I A. Will the appliance be safe for longer time.
# An electric appliance of P W power is operated in domestic circuit of V V. What is the minimum current rating it should have to avoid overloading.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def type1():
    V = random.randint(220,240)
    P = random.randint(24,2200)
    I = round(random.randint(1,1000)/10,1)
    q = "An electric appliance of "+str(P)+" W power rating is operated in a domestic electric circuit of "+str(V)+" V that has a current rating of "+str(I)+" A. Will the appliance be safe for longer time.\n"
    if P/V-I > 0.01:
        a = "no, it will not be safe for longer time\n"
    else:
        a = "it will be safe for longer time\n"
    return q,a

def type2():
    V = random.randint(220,240)
    P = random.randint(24,100000)
    q = "An electric appliance of "+str(P)+" W power is operated in domestic circuit of "+str(V)+" V. What is the minimum current rating it should have to avoid overloading.\n"
    a = str(round(P/V,1))+" ampere\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1 or types == 2 or types == 4:
        ques,answer = type1()
    elif types == 3:
        ques,answer = type2()

    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()