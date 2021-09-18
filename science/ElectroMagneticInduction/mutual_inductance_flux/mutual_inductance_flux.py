import random

# A pair of adjacent coils has a mutual inductance of m H. If the current in one coil changes from i1 A to i2 A in t sec, what is the change of flux linkage with the other coil.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 500000

def cal1(i1, i2, t, m) :
    return round((m*(i1-i2))/t,2)    

def type1() :
    t = random.randint(1,100)
    t = round(t*0.1,1)
    i2 = random.randint(1,30)
    i1 = random.randint(i2+1,i2+20)
    m = random.randint(1,100)
    m = round(m*0.1,1)
    q = "A pair of adjacent coils has a mutual inductance of " + str(m) + " H. If the current in one coil changes from " + str(i1) + " A to " + str(i2) + " A in " + str(t) + " sec, what is the change of flux linkage with the other coil.\n"
    a = str(cal1(i1, i2, t, m)) + " weber\n"
    return q,a

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
