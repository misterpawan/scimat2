import random

# An object is placed at u cm in front of a concave mirror of focal length f cm. Find at what distance image is formed and its nature.
# An image is formed by a concave mirror of focal length f cm at a distance of v cm in front of it. Find at what distance object is placed in front of mirror.    
# An image is formed by a concave mirror of focal length f cm at a distance of v cm behind it. Find at what distance object is placed in front of mirror.
# An object is placed at u cm in front of a concave mirror. Image is formed at a distance of v cm in front of it. Find the focal length of the mirror.
# An object is placed at u cm in front of a concave mirror. Image is formed at a distance of v cm behind it. Find the focal length of the mirror. 
# All variants of 1/f = 1/v + 1/u for concave mirror

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000

def calculation_1(u, f) :
    return round((u*f)/(u-f),1)

def calculation_2(u, f) :
    return round((u*f)/(f-u),1)

def calculation_3(v, f) :
    return round((v*f)/(v-f),1)

def calculation_4(v, f) :
    return round((v*f)/(v+f),1)

def calculation_5(u, v) :
    return round((u*v)/(u+v),1)

def calculation_6(u, v) :
    return round((u*v)/(v-u),1)    

def type1() :
    f = random.randint(1,800)
    u = random.randint(f+1,f+1200)
    q = "An object is placed at " + str(u) + " cm in front of a concave mirror of focal length " + str(f) + " cm. Find at what distance image is formed and its nature.\n"
    v = str(calculation_1(u,f)) + "cm and real\n"
    return q,v

def type2() :
    u = random.randint(1,1000)
    f = random.randint(u+1,u+1000)
    q = "An object is placed at " + str(u) + " cm in front of a concave mirror of focal length " + str(f) + " cm. Find at what distance image is formed and its nature.\n"
    v = str(calculation_2(u,f)) + "cm and virtual\n"
    return q,v

def type3() :
    f = random.randint(1,800)
    v = random.randint(f+1,f+1200)
    q = "An image is formed by a concave mirror of focal length " + str(f) + " cm at a distance of " + str(v) + " cm in front of it. Find at what distance object is placed in front of mirror.\n"
    u = str(calculation_3(v,f)) + "cm\n"
    return q,u

def type4() :
    f = random.randint(1,1000)
    v = random.randint(1,1000)
    q = "An image is formed by a concave mirror of focal length " + str(f) + " cm at a distance of " + str(v) + " cm behind it. Find at what distance object is placed in front of mirror.\n"
    u = str(calculation_4(v,f)) + "cm\n"
    return q,u

def type5() :
    u = random.randint(1,1000)
    v = random.randint(1,1000)
    q = "An object is placed at " + str(u) + " cm in front of a concave mirror. Image is formed at a distance of " + str(v) + " cm in front of it. Find the focal length of the mirror.\n"
    f = str(calculation_5(u,v)) + "cm\n"
    return q,f

def type6() :
    u = random.randint(1,1000)
    v = random.randint(u+1,u+1000)
    q = "An object is placed at " + str(u) + " cm in front of a concave mirror. Image is formed at a distance of " + str(v) + " cm behind it. Find the focal length of the mirror.\n"
    f = str(calculation_6(u,v)) + "cm\n"
    return q,f

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
