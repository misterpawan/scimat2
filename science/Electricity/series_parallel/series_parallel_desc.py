import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    R1 = random.randint(1,200)
    R2 = random.randint(1,200)
    R3 = random.randint(1,100)
    types = random.randint(0,3)
    if types == 0:
        word = "the highest"
        answer = "the highest combination of any number of resistances can be obtained by their series combination, final effective resistance of 3 resistors in a series combination is r1+r2+r3 = "+str(R1)+"+"+str(R2)+"+"+str(R3)+" = " 
        answer += str(R1+R2+R3) + " ohm\n"
    else:
        word = "the lowest"
        answer = "the lowest combination of any number of resistances can be obtained by their parallel combination, final effective resistance of 3 resistors in a parallel combination is (r1*r2*r3)/(r1*r2+r2*r3+r3*r1), which is equal to " 
        answer += str(round((R1*R2*R3)/(R1*R2+R2*R3+R3*R1),1)) + " ohm\n"
    ques = "What is " + str(word) + " total resistance that can be secured by combinations of three coils of resistance " + str(R1) + ", " + str(R2) + ", " + str(R3) + " ?\n"
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
