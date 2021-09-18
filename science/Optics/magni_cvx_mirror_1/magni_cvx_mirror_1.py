import random

# A convex mirror produces n times diminished real image of an object placed at u cm in front of it. At what distance image is formed from the mirror ?
# A convex mirror produces n times diminished real image of an object at a distance of v cm from the mirror. At what distance object is placed in front of the mirror ?
# m = v/u

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

def calculation_v_dim(n, u): 
    return round(u/n,1)

def calculation_u_dim(n, v):
    return round(v*n, 1)

def type1():
    n = random.randint(2,100)
    u = random.randint(1,10000)
    v = str(calculation_v_dim(n,u)) + " cm\n"
    q = "A convex mirror produces " + str(n) + " times diminished real image of an object placed at " + str(u) + " cm in front of it. At what distance image is formed from the mirror ?\n"
    return q,v

def type2():
    n = random.randint(2,100)
    v = random.randint(1,10000)
    v = round(v/100,2)
    u = str(calculation_u_dim(n,v)) + " cm\n"
    q = "A convex mirror produces " + str(n) + " times diminished real image of an object at a distance of " + str(v) + " cm from the mirror. At what distance object is placed in front of the mirror ?\n"
    return q,u

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