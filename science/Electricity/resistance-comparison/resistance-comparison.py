import random

# Two lamps, one rated P1 W at V1 V, and the other P2 W at V2 V, which has more resistance?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20
i = 0
while i < no_of_samples:
    V1 = random.randint(220,240)
    V2 = random.randint(220,240)
    P1 = random.randint(1,100)
    P2 = random.randint(1,100)
    q = "Two lamps, one rated "+str(P1)+" W at "+str(V1)+" V, and the other "+str(P2)+" W at "+str(V2)+" V, which has more resistance?\n"
    if (V1**2)/P1 > (V2**2)/P2:
        answer = "lamp1\n"
        i+=1
    elif (V1**2)/P1 < (V2**2)/P2:
        answer = "lamp2\n"
        i+=1
    else:
        continue
    # print(i)
    qns.write(q)
    ans.write(answer)
    # print(q)
    # print(answer)
qns.close()
ans.close()
