import random

# A steady current of I A flows through a conductor, then calculate number of electrons through any cross section of the conductor in t s?
# A steady current flows through a conductor, if number of electrons through any cross section of conductor in t s are n, then calculate the value of the current?
# A steady current of I A flows through a conductor, then calculate the time taken for n electrons to pass through any cross section of the conductor?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20
e = 1.6*1e-19

def type1():
    I = random.randint(1,1000)
    t = random.randint(1,1000)
    n = str(round((I*t)/e,1)) + "\n"
    n1 = str(n)
    n2 = n1[:4]+n1[-5:]
    q = "A steady current of "+str(I)+" A flows through a conductor, then calculate number of electrons through any cross section of the conductor in "+str(t)+" s?\n"
    return q,n2

def type2():
    n = random.randint(1e19,1e20)
    n1 = str(n)
    n2 = n1[0] + "." + n1[1:5] + "e" + str(len(n1)-1)
    t = random.randint(1,10)
    I = str(round((n*e)/t,1)) + " ampere\n"
    n = n2
    q = "A steady current flows through a conductor, if number of electrons through any cross section of conductor in "+str(t)+" s are "+str(n)+", then calculate the value of the current?\n"
    return q,I

def type3():
    n = random.randint(1e19,1e20)
    n1 = str(n)
    n2 = n1[0] + "." + n1[1:6] + "e" + str(len(n1)-1)
    I = random.randint(1,10)
    t = str(round((n*e)/I,1)) + " s\n"
    n = n2
    q = "A steady current of "+str(I)+" A flows through a conductor, then calculate the time taken for "+str(n)+" electrons to pass through any cross section of the conductor?\n"
    return q,t

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()