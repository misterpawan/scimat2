import random

# The radius of a sphere is measured as (2.1 +/- 0.5) cm calculate its surface area with error limits
# A force of F_val +/- F_error N is applied over an area of A_val +/- A_error m2. Calculate the pressure exerted over the area.
# Find the value of g using simple pendulum, the following observations were made: length of thread l = l_val +/- l_error cm, time period of oscillation T = t_val +/- t_error s, then value of g in error limits is?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 30
# +/-

def type1():
    r = round(random.randint(410,30000)/10,1)
    error = round(random.randint(1,300)/10,1)
    q = "The radius of a sphere is measured as "+ str(r)+" +/- "+ str(error) +" cm calculate its surface area (in m2) with error limits.\n"
    ans_val = round((4*3.14*r*r)/10000,1)
    error = round(2*((ans_val*error)/r),1)
    a = str(ans_val) + "+/-" + str(error) + "\n"
    return q,a

def type2():
    F_val = random.randint(20,400)
    F_error = random.randint(1,10)
    A_val = round(random.randint(20,400)/100,2)
    A_error = round(random.randint(1,10)/100,2)
    q = "A force of "+str(F_val)+" +/- "+str(F_error)+" N is applied over an area of "+str(A_val)+" +/- "+str(A_error)+" m2. Calculate the pressure exerted over the area.\n"
    ans_val = round(F_val / A_val,2)
    ans_error = round(ans_val*(F_error/F_val+A_error/A_val),2)
    a = str(ans_val) + "+/-" + str(ans_error) + "\n"
    return q,a

def type3():
    l_val = random.randint(20,400)
    l_error = random.randint(1,10)
    t_val = round(random.randint(20,400)/100,2)
    t_error = round(random.randint(1,10)/100,2)
    q = "Find the value of g using simple pendulum, the following observations were made: length of thread l = "+str(l_val)+" +/- "+str(l_error)+" cm, time period of oscillation T = "+str(t_val)+" +/- "+str(t_error)+" s, then value of g in error limits is?\n"
    ans_val = round(4*3.14*3.14*(l_val/(t_val*t_val)),2)
    ans_error = round(ans_val*(l_error/l_val+2*(t_error/t_val)),2)
    a = str(ans_val) + "+/-" + str(ans_error) + "\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    # print(ques)
    # print(answer)
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()
