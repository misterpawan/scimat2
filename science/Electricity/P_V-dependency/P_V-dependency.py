import random

# The wattage of a bulb is P1 W when it is connected to a V1 V battery. Calculate its effective wattage if it operates on a V2 V battery.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20
i = 0

while i < no_of_samples:
    P1 = random.randint(251,1250)
    V1 = random.randint(1,50)
    V2 = random.randint(1,50)
    if V1!=V2:
        q = "The wattage of a bulb is "+str(P1)+" W when it is connected to a "+str(V1)+" V battery. Calculate its effective wattage if it operates on a "+str(V2)+" V battery?\n"
        answer = str(round(((V2**2)*P1)/(V1**2),1)) + " \n"
        qns.write(q)
        ans.write(answer)
        # print(q)
        # print(answer)
        i += 1
qns.close()
ans.close()
