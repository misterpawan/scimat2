import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    q1 = random.randint(1,2000000)
    q = "A polythene is rubbed with wool is found to have a negative charge of "+str(q1)+" x 10^(-12) C. "
    types = random.randint(1,2)
    n = (q1*(10**(-12)))/(1.6*(10**(-19)))
    if types == 1:
        q = q + "Estimate the number of electrons transfered (from which to which)?\n"
        a = "{:.3e}".format(n)+" electrons transfered from wool to polythene\n"
    else:
        q = q + "Is there a transfer of mass from wool to polythene?\n"
        a = "yes, "+"{:.3e}".format(n*9.1*(10**(-31)))+" kg of mass is transfered\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
