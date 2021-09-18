import random

# Which uses more energy, a P1 W TV set in t1 s, or a P2 W toaster in t2 s? 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20
i = 0
while i < no_of_samples:
    P1 = random.randint(1,20)
    P2 = random.randint(1,20)
    t1 = random.randint(1,100)
    t2 = random.randint(1,100)
    question = "Which uses more energy, a "+str(P1)+" W TV set in "+str(t1)+" s, or a "+str(P2)+" W toaster in "+str(t2)+" s?\n"
    if P1*t1 > P2*t2:
        answer = "TV set\n"
        i+=1
    elif P2*t2 > P1*t1:
        answer = "toaster\n"
        i+=1
    else:
        continue
    # print(i)
    qns.write(question)
    ans.write(answer)
    # print(question)
    # print(answer)
qns.close()
ans.close()
