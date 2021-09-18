import random

# A convex mirror produces n times diminished real image of an object of height ho cm placed in front of it. What is the height of the image formed by it ?
# A convex mirror produces n times diminished real image of height hi cm of an object placed in front of it. What is the height of the object taken ?
# m = hi/ho

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

def calculation_hi_dim(n, ho): 
    return round(ho/n,1)

def calculation_ho_dim(n, hi):
    return round(hi*n, 1)

def type1():
    n = random.randint(2,100)
    ho = random.randint(1,10000)
    hi = str(calculation_hi_dim(n,ho)) + " cm\n"
    q = "A convex mirror produces " + str(n) + " times diminished real image of an object of height " + str(ho) + " cm placed in front of it. What is the height of the image formed by it ?\n"
    return q,hi

def type2():
    n = random.randint(2,100)
    hi = random.randint(1,10000)
    hi = round(hi/100,2)
    ho = str(calculation_ho_dim(n,hi)) + " cm\n"
    q = "A convex mirror produces " + str(n) + " times diminished real image of height " + str(hi) + " cm of an object placed in front of it. What is the height of the object taken ?\n"
    return q,ho

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
