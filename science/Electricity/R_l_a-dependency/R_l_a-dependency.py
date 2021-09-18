import random

# A piece of wire of resistance R ohm is drawn out so that its length is increased n times. Calculate the resistance of reformed wire?
# A piece of wire of resistance R ohm is drawn out so that its cross-sectional area is increased n times. Calculate the resistance of reformed wire?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20
i = 0

while i < no_of_samples:
    R = random.randint(10,100010)
    n = random.randint(2,11)
    types = random.randint(0,2)
    if types == 0 or types == 1:
        q = "A piece of wire of resistance "+str(R)+" ohm is drawn out so that its length is increased "+str(n)+" times. Calculate the resistance of reformed wire?\n"
        answer = str(R*n*n) + " \n"
        i+=1
    elif types == 2:
        q = "A piece of wire of resistance "+str(R)+" ohm is drawn out so that its cross-sectional area is increased "+str(n)+" times. Calculate the resistance of reformed wire?\n"
        answer = str(round(R/(n**2),1)) + " \n"
        i+=1
    qns.write(q)
    ans.write(answer)
    # print(q)
    # print(answer)
qns.close()
ans.close()
