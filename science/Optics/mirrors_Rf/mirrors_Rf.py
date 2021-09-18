import random

# Find the focal length of a convex mirror whose radius of curvature is R cm.
# Find the focal length of a concave mirror whose radius of curvature is R cm.
# Find the radius of curvature of a convex mirror whose focal lenfth is f cm. 
# Find the radius of curvature of a concave mirror whose focal lenfth is f cm.
# R = 2*f

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

def calculation_R(f):
    return round(2*f,1)

def calculation_f(R):
    return round(R/2, 1)

def type1():
    R = random.randint(1,500000)
    R = round(R/50,2)
    f = str(calculation_f(R)) + " cm\n"
    q = "Find the focal length of a convex mirror whose radius of curvature is " + str(R) + " cm.\n"
    return q,f

def type2():
    R = random.randint(1,500000)
    R = round(R/50,2)
    f = str(calculation_f(R)) + " cm\n"
    q = "Find the focal length of a concave mirror whose radius of curvature is " + str(R) + " cm.\n"
    return q,f

def type3():
    f = random.randint(1,500000)
    f = round(f/100,2)
    R = str(calculation_R(f)) + " cm\n"
    q = "Find the radius of curvature of a convex mirror whose focal lenfth is " + str(f) + " cm.\n"
    return q,R

def type4():
    f = random.randint(1,500000)
    f = round(f/100,2)
    R = str(calculation_R(f)) + " cm\n"
    q = "Find the radius of curvature of a concave mirror whose focal lenfth is " + str(f) + " cm.\n"
    return q,R

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