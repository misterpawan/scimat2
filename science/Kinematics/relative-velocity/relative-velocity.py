import random


# A jet airplane travelling at the speed of 500 kmph ejects its combustion products at the speed of 1500 kmph relative to the jet plane. What is the speed of the combustion products with respect to an observer on the ground?
# A jet airplane travelling at the speed of 500 kmph ejects its combustion products. If the speed of the combustion products with respect to an observer on the ground is v2, then what is the speed of combustion products with respect to plane?
# A jet airplane ejects its combustion products at the speed of v1 kmph with respect to jet plane. If the speed of combustion products with respect to an observer on the ground is v2, then what is the speed of plane?
# A police van moving on a highway with a speed of 30 ms-1 fires a bullet at a thief s car speeding away in the same direction with a speed of 192 ms-1 . If the muzzle speed of the bullet is 150 ms-1 , with what speed does the bullet hit the thief s car?\n

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000
# no_of_samples = 30

def type1():
    v1 = random.randint(1,2000)
    v2 = random.randint(1,2000)
    q = "A jet airplane travelling at the speed of "+str(v1)+" ms-1 ejects its combustion products at the speed of "+str(v2)+" ms-1 relative to the jet plane. What is the speed of the combustion products with respect to an observer on the ground?\n"
    a = str(v1-v2) + " ms-1\n"
    return q,a

def type2():
    v1 = random.randint(1,2000)
    v2 = random.randint(1,2000)
    q = "A jet airplane travelling at the speed of "+str(v1)+" ms-1 ejects its combustion products. If the speed of the combustion products with respect to an observer on the ground is "+str(v2)+" ms-1, then what is the speed of combustion products with respect to plane?\n"
    a = str(v1-v2) + " ms-1\n"
    return q,a

def type3():
    v1 = random.randint(1,2000)
    v2 = random.randint(1,2000)
    q = "A jet airplane ejects its combustion products at the speed of "+str(v1)+" ms-1 with respect to jet plane. If the speed of combustion products with respect to an observer on the ground is "+str(v2)+" ms-1, then what is the speed of plane?\n"
    a = str(v1+v2) + " ms-1\n"
    return q,a

def type4():
    v1 = random.randint(50,250)
    v2 = random.randint(300,500)
    v3 = random.randint(1000,1200)
    q = "A police van moving on a highway with a speed of "+str(v1)+" ms-1 fires a bullet at a thief s car speeding away in the same direction with a speed of "+str(v2)+" ms-1. If the muzzle speed of the bullet is "+str(v3)+" ms-1, with what speed does the bullet hit the thief's car?\n"
    a = "speed of bullet is "+str(v1+v3)+" ms-1, relative speed of bullet w.r.t to thief's car is "+str(v1+v3-v2)+" ms-1\n"
    return q,a

for i in range(no_of_samples):
    types = random.randint(1,5)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    elif types == 4 or types == 5:
        ques,answer = type4()
    # print(ques)
    # print(answer)
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()