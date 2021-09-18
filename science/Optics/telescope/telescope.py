import random

# A small telescope has an objective lens of focal length 144 cm and an eyepiece of focal length 6.0 cm. What is the magnifying power of the telescope? 
# A small telescope has an objective lens of focal length 144 cm and an eyepiece of focal length 6.0 cm. What is the separation between the objective and the eyepiece?

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(f1, f2) :
    return round(f1/f2,2)

def cal2(f1, f2) :
    return f1+f2

def type1() :
    f2 = random.randint(10,1000)
    f2 = round(f2/10,1)
    temp = random.randint(10,1000)
    temp = round(temp/10,1)
    f1 = f2+temp
    q = "A small telescope has an objective lens of focal length " + str(f1) + " cm and an eyepiece of focal length " + str(f2) + " cm. What is the magnifying power of the telescope? \n"
    e = str(cal1(f1, f2)) + "\n"
    return q,e

def type2() :
    f2 = random.randint(10,1000)
    f2 = round(f2/10,1)
    temp = random.randint(10,1000)
    temp = round(temp/10,1)
    f1 = f2+temp
    q = "A small telescope has an objective lens of focal length " + str(f1) + " cm and an eyepiece of focal length " + str(f2) + " cm. What is the separation between the objective and the eyepiece?\n"
    e = str(cal2(f1,f2)) + " cm\n"
    return q,e

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1 :
        ques, answer = type1()
    elif types == 2 :
        ques, answer = type2()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
