import random

# A force of F N acts on an object. The displacement is s m in the direction of the force,
#  then what is the work done by this force?
# A force applied on a subject causes s m displacement in the direction of the force, If 
# work done is equal to W J then what is the value of force ?
# A force of F N acts on an object causes displacement in the direction of the force, If 
# work done is equal to W J then what is the displacement ?
# W = F*S

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
# no_of_samples = 8
no_of_samples = 1500000

def calculation_W(F, s): 
    return F * s

def calculation_F(W, s):
    return round(W / s, 1)

def calculation_s(W, F):
    return round(W / F, 1)

def type1():
    F = random.randint(1,1000)
    s = random.randint(1,1000)
    W = str(calculation_W(F,s)) + " J\n"
    q = "A force of " + str(F) + " N acts on an object. The displacement is " + str(s) + " m in the direction of the force, then what is the work done by this force ?\n"
    return q,W

def type2():
    W = random.randint(9000,10000)
    s = random.randint(1,1000)
    F = str(calculation_F(W,s)) + " N\n"
    q = "A force applied on a subject causes " + str(s) + " m displacement in the direction of the force, If work done is equal to " + str(W) + " J then what is the value of force ?\n"
    return q,F

def type3():
    W = random.randint(9000,10000)
    F = random.randint(1,1000)
    s = str(calculation_s(W,F)) + " m\n"
    q = "A force of " + str(F) + " N acts on an object causes displacement in the direction of the force, If work done is equal to " + str(W) + " J then what is the displacement ?\n"
    return q,s

for i in range(no_of_samples):
    types = random.randint(0,2)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
