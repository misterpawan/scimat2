import random

# A concave lens produces n times diminished real image of an object of height ho cm placed in front of it. What is the height of the image formed by it ?
# A concave lens produces n times diminished real image of height hi cm of an object placed in front of it. What is the height of the object?
# A concave lens produces an real image of height hi cm of a real object of height ho cm placed in front of it. What is the magnification of the lens.
# m = hi/ho

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_hi_dim(n, ho): 
    return round(ho/n,1)

def calculation_ho_dim(n, hi):
    return round(hi*n, 1)

def calculation_m (val1, val2):
    return round(val1/val2, 1)

def type1():
    n = random.randint(2,100)
    ho = random.randint(1,10000)
    hi = str(calculation_hi_dim(n,ho)) + " cm\n"
    q = "A concave lens produces " + str(n) + " times diminished real image of an object of height " + str(ho) + " cm placed in front of it. What is the height of the image formed by it ?\n"
    return q,hi

def type2():
    n = random.randint(2,100)
    hi = random.randint(1,10000)
    hi = round(hi/100,2)
    ho = str(calculation_ho_dim(n,hi)) + " cm\n"
    q = "A concave lens produces " + str(n) + " times diminished real image of height " + str(hi) + " cm of an object placed in front of it. What is the height of the object taken ?\n"
    return q,ho

def type3():
    hi = random.randint(1,1000)
    ho = random.randint(hi+1,hi+1000)
    m = str(calculation_m(hi,ho)) + "\n"
    q = "A concave lens produces an real image of height " + str(hi) + " cm of a real object of height " + str(ho) + " cm placed in front of it. What is the magnification of the lens.\n"
    return q,m

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()