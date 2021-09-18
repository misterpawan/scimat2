import random

# A convex lens produces n times magnified real image of an object placed at u cm in front of it. At what distance image is formed from the lens ?
# A convex lens produces n times magnified real image of an object at a distance of v cm from the lens. At what distance object is placed in front of the lens ?
# A convex lens produces n times magnified virtual image of an object placed at u cm in front of it. At what distance image is formed from the lens ?
# A convex lens produces n times magnified virtual image of an object at a distance of v cm from the lens. At what distance object is placed in front of the lens ?
# A convex lens produces n times diminished real image of an object placed at u cm in front of it. At what distance image is formed from the lens ?
# A convex lens produces n times diminished real image of an object at a distance of v cm from the lens. At what distance object is placed in front of the lens ?
# m = v/u

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000

def calculation_v(n, u): 
    return round(n*u,1)

def calculation_u(n, v):
    return round(v/n, 1)

def calculation_v_dim(n, u): 
    return round(u/n,1)

def calculation_u_dim(n, v):
    return round(v*n, 1)

def type1():
    n = random.randint(1,100)
    u = random.randint(1,10000)
    u = round(u/100,2)
    v = str(calculation_v(n,u)) + " cm\n"
    q = "A convex lens produces " + str(n) + " times magnified real image of an object placed at " + str(u) + " cm in front of it. At what distance image is formed from the lens ?\n"
    return q,v

def type2():
    n = random.randint(1,100)
    v = random.randint(1,10000)
    u = str(calculation_u(n,v)) + " cm\n"
    q = "A convex lens produces " + str(n) + " times magnified real image of an object at a distance of " + str(v) + " cm from the lens. At what distance object is placed in front of the lens ?\n"
    return q,u

def type3():
    n = random.randint(2,100)
    u = random.randint(1,10000)
    u = round(u/100,2)
    v = str(calculation_v(n,u)) + " cm\n"
    q = "A convex lens produces " + str(n) + " times magnified virtual image of an object placed at " + str(u) + " cm in front of it. At what distance image is formed from the lens ?\n"
    return q,v

def type4():
    n = random.randint(2,100)
    v = random.randint(1,10000)
    u = str(calculation_u(n,v)) + " cm\n"
    q = "A convex lens produces " + str(n) + " times magnified virtual image of an object at a distance of " + str(v) + " cm from the lens. At what distance object is placed in front of the lens ?\n"
    return q,u

def type5():
    n = random.randint(2,100)
    u = random.randint(1,10000)
    v = str(calculation_v_dim(n,u)) + " cm\n"
    q = "A convex lens produces " + str(n) + " times diminished real image of an object placed at " + str(u) + " cm in front of it. At what distance image is formed from the lens ?\n"
    return q,v

def type6():
    n = random.randint(2,100)
    v = random.randint(1,10000)
    v = round(v/100,2)
    u = str(calculation_u_dim(n,v)) + " cm\n"
    q = "A convex lens produces " + str(n) + " times diminished real image of an object at a distance of " + str(v) + " cm from the lens. At what distance object is placed in front of the lens ?\n"
    return q,u

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