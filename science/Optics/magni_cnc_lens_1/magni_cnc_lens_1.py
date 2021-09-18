import random

# A concave lens produces n times diminished real image of an object placed at u cm in front of it. At what distance image is formed from the lens ?
# A concave lens produces n times diminished real image of an object at a distance of v cm from the lens. At what distance object is placed in front of the lens ?
# A concave lens produces a real image at a distance of v cm from it of a real object placed u cm in front of it. What is the magnification of the lens.
# m = v/u

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_v_dim(n, u): 
    return round(u/n,1)

def calculation_u_dim(n, v):
    return round(v*n, 1)

def calculation_m (val1, val2):
    return round(val1/val2, 1)

def type1():
    n = random.randint(2,100)
    u = random.randint(1,10000)
    v = str(calculation_v_dim(n,u)) + " cm\n"
    q = "A concave lens produces " + str(n) + " times diminished real image of an object placed at " + str(u) + " cm in front of it. At what distance image is formed from the lens ?\n"
    return q,v

def type2():
    n = random.randint(2,100)
    v = random.randint(1,10000)
    v = round(v/100,2)
    u = str(calculation_u_dim(n,v)) + " cm\n"
    q = "A concave lens produces " + str(n) + " times diminished real image of an object at a distance of " + str(v) + " cm from the lens. At what distance object is placed in front of the lens ?\n"
    return q,u

def type3():
    v = random.randint(1,1000)
    u = random.randint(v+1,v+1000)
    m = str(calculation_m(v,u)) + "\n"
    q = "A concave lens produces a real image at a distance of " + str(v) + " cm from it of a real object placed " + str(u) + " cm in front of it. What is the magnification of the lens.\n"
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