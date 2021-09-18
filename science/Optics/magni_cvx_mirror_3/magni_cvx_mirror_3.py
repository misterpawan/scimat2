import random

# A convex mirror produces aa real image at a distance of v cm from it of a real object placed u cm in front of it. What is the magnification of the mirror.
# A convex mirror produces an real image of height hi cm of a real object of height ho cm placed in front of it. What is the magnification of the mirror.
# m = hi/ho = v/u

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

def calculation_m (val1, val2):
    return round(val1/val2, 1)

def type1():
    v = random.randint(1,1000)
    u = random.randint(v+1,v+1000)
    m = str(calculation_m(v,u)) + "\n"
    q = "A convex mirror produces an real image at a distance of " + str(v) + " cm from it of a real object placed " + str(u) + " cm in front of it. What is the magnification of the mirror.\n"
    return q,m

def type2():
    hi = random.randint(1,1000)
    ho = random.randint(hi+1,hi+1000)
    m = str(calculation_m(hi,ho)) + "\n"
    q = "A concave mirror produces an real image of height " + str(hi) + " cm of a real object of height " + str(ho) + " cm placed in front of it. What is the magnification of the mirror.\n"
    return q,m

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
