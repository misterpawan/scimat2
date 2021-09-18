import random

# An object is placed at u cm in front of a convex mirror of focal length f cm. Find at what distance image is formed and its nature.
# An image is formed by a convex mirror of focal length f cm at a distance of v cm behind it. Find at what distance object is placed in front of mirror.
# An object is placed at u cm in front of a convex mirror. Image is formed at a distance of v cm behind it. Find the focal length of the mirror.
# All variants of 1/f = 1/v + 1/u for convex mirror

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_1(u,f) :
    return round((f*u)/(f+u))

def calculation_2(v,f) :
    return round((f*v)/(f-v))

def calculation_3(u,v) :
    return round((u*v)/(u-v))

def type1() :
    f = random.randint(1,1000)
    u = random.randint(1,1000)
    q = "An object is placed at " + str(u) + " cm in front of a convex mirror of focal length " + str(f) + " cm. Find at what distance image is formed and its nature.\n"
    v = str(calculation_1(u,f)) + "cm and virtual\n"
    return q,v

def type2() :
    v = random.randint(1,1000)
    f = random.randint(v+1,v+1000)
    q = "An image is formed by a convex mirror of focal length " + str(f) + " cm at a distance of " + str(v) + " cm behind it. Find at what distance object is placed in front of mirror.\n"
    u = str(calculation_2(v,f)) + "cm\n"
    return q,u

def type3() :
    v = random.randint(1,1000)
    u = random.randint(v+1,v+1000)
    q = "An object is placed at " + str(u) + " cm in front of a convex mirror. Image is formed at a distance of " + str(v) + " cm behind it. Find the focal length of the mirror.\n"
    f = str(calculation_3(u,v)) + "cm\n"
    return q,f

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
