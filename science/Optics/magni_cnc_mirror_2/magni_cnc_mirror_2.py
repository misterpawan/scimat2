import random

# A concave mirror produces n times magnified real image of a ho cm object placed in front of it. What is the height of the image formed by the mirror ?
# A concave mirror produces n times magnified real image of height hi cm of an object placed in front of it. What is the height of the object taken ?
# A concave mirror produces n times magnified virtual image of a ho cm object placed in front of it. What is the height of the image formed by the mirror ?
# A concave mirror produces n times magnified virtual image of height hi cm of an object placed in front of it. What is the height of the object taken ?
# A concave mirror produces n times diminished real image of a ho cm object placed in front of it. What is the height of the image formed by the mirror ?
# A concave mirror produces n times diminished real image of height hi cm of an object placed in front of it. What is the height of the object taken ?
# m = hi/ho

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000

def calculation_hi(n, ho): 
    return round(n*ho,1)

def calculation_ho(n, hi):
    return round(hi/n, 1)

def calculation_hi_dim(n, ho): 
    return round(ho/n,1)

def calculation_ho_dim(n, hi):
    return round(hi*n, 1)

def type1():
    n = random.randint(1,100)
    ho = random.randint(1,10000)
    ho = round(ho/100,2)
    hi = str(calculation_hi(n,ho)) + " cm\n"
    q = "A concave mirror produces " + str(n) + " times magnified real image of a " + str(ho) + " cm object placed in front of it. What is the height of the image formed by the mirror ?\n"
    return q,hi

def type2():
    n = random.randint(1,100)
    hi = random.randint(1,10000)
    ho = str(calculation_ho(n,hi)) + " cm\n"
    q = "A concave mirror produces " + str(n) + " times magnified real image of height " + str(hi) + " cm of an object placed in front of it. What is the height of the object taken ?\n"
    return q,ho

def type3():
    n = random.randint(2,100)
    ho = random.randint(1,10000)
    ho = round(ho/100,2)
    hi = str(calculation_hi(n,ho)) + " cm\n"
    q = "A concave mirror produces " + str(n) + " times magnified virtual image of a " + str(ho) + " cm object placed in front of it. What is the height of the image formed by the mirror ?\n"
    return q,hi

def type4():
    n = random.randint(2,100)
    hi = random.randint(1,10000)
    ho = str(calculation_ho(n,hi)) + " cm\n"
    q = "A concave mirror produces " + str(n) + " times magnified virtual image of height " + str(hi) + " cm of an object placed in front of it. What is the height of the object taken ?\n"
    return q,ho

def type5():
    n = random.randint(2,100)
    ho = random.randint(1,10000)
    hi = str(calculation_hi_dim(n,ho)) + " cm\n"
    q = "A concave mirror produces " + str(n) + " times diminished real image of a " + str(ho) + " cm object placed in front of it. What is the height of the image formed by the mirror ?\n"
    return q,hi

def type6():
    n = random.randint(2,100)
    hi = random.randint(1,10000)
    hi = round(hi/100,2)
    ho = str(calculation_ho_dim(n,hi)) + " cm\n"
    q = "A concave mirror produces " + str(n) + " times diminished real image of height " + str(hi) + " cm of an object placed in front of it. What is the height of the object taken ?\n"
    return q,ho

for i in range(no_of_samples):
    types = random.randint(1,6)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4:
        ques,answer = type4()
    elif types == 5:
        ques,answer = type5()
    elif types == 6:
        ques,answer = type6()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
