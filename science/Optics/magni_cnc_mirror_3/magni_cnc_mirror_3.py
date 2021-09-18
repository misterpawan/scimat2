import random

# A concave mirror produces an virtual image at a distance of v cm from it of a real object placed u cm in front of it. What is the magnification of the mirror.
# A concave mirror produces aa real image at a distance of v cm from it of a real object placed u cm in front of it. What is the magnification of the mirror.
# A concave mirror produces an virtual image of height hi cm of a real object of height ho cm placed in front of it. What is the magnification of the mirror.
# A concave mirror produces an real image of height hi cm of a real object of height ho cm placed in front of it. What is the magnification of the mirror.
# m = v/u = hi/ho

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

def calculation_m (val1, val2):
    return round(val1/val2, 1)

def type1():
    u = random.randint(1,1000)
    v = random.randint(u+1,u+1000)
    m = str(calculation_m(v,u)) + "\n"
    q = "A concave mirror produces an virtual image at a distance of " + str(v) + " cm from it of a real object placed " + str(u) + " cm in front of it. What is the magnification of the mirror.\n"
    return q,m

def type2():
    u = random.randint(1,1000)
    v = random.randint(1,1000)
    m = str(calculation_m(v,u)) + "\n"
    q = "A concave mirror produces aa real image at a distance of " + str(v) + " cm from it of a real object placed " + str(u) + " cm in front of it. What is the magnification of the mirror.\n"
    return q,m

def type3():
    ho = random.randint(1,1000)
    hi = random.randint(ho+1,ho+1000)
    m = str(calculation_m(hi,ho)) + "\n"
    q = "A concave mirror produces an virtual image of height " + str(hi) + " cm of a real object of height " + str(ho) + " cm placed in front of it. What is the magnification of the mirror.\n"
    return q,m

def type4():
    ho = random.randint(1,1000)
    hi = random.randint(1,1000)
    m = str(calculation_m(hi,ho)) + "\n"
    q = "A concave mirror produces an real image of height " + str(hi) + " cm of a real object of height " + str(ho) + " cm placed in front of it. What is the magnification of the mirror.\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4:
        ques,answer = type4()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
