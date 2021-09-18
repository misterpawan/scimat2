import random

# A closely wounded solenoid of n turns and area of cross-section carries a current of i A. What is its associated magnetic moment. 

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

def cal1(n, i, A) :
    return n*i*A

def type1() :
    n = random.randint(1,50)
    n = n*20
    i = random.randint(1,100)
    A = random.randint(1,200)
    A = round(A*0.0001,4)
    q = "A closely wounded solenoid of " + str(n) + " turns and area of cross-section " + str(A) + " m2 carries current of " + str(i) + " A. What is its associated magnetic moment.\n"
    a = "{:.2e}".format(cal1(n, i, A)) + " joule/tesla\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
