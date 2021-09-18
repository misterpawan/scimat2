import random

# Light enters from air to glass having refractive index r. If the speed of light in vacuum is 3 x 10e8 ms-1, What is the speed of light in the glass ?
# Light enters from air to glass. If the speed of light in vacuum is 3 x 10e8 ms-1 and in glass is v m/s, what is the refractive index of the glass ?  
# Light enters from a material-1 having refractive index r1 to material-2 having refractive index r2. If the speed of the light in material-1 is v1 m/s, what is the speed of light in material-2 ?
# Light enters from a material-1 to material-2 having refractive index r2. If the speed of ight in material-1 and material-2 is v1 m/s and v2 m/s respectively. What is the refractive index of material-1 ?
# Light enters from a material-1 having refractive index r1 to material-2 having refractive index r2. If the speed of the light in material-2 is v2 m/s, what is the speed of light in material-1 ?
# Light enters from a material-1 having refractive index r1 to material-2. If the speed of ight in material-1 and material-2 is v1 m/s and v2 m/s respectively. What is the refractive index of material-2 ?
# r1/r2 = v2/v1

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2500000

def calculation_r1(r2, v1, v2):
    return round((r2*v2)/v1,1) 

def calculation_v1(r1, r2, v2):
    return round((r2*v2)/r1, 1)

def type1():
    v2 = 300000000
    r1 = random.randint(1,500000)
    r1 = round(r1/100,2)
    r2 = 1
    v1 = str(calculation_v1(r1,r2,v2)) + " m/s\n"
    q = "Light enters from air to glass having refractive index " + str(r1) +". If the speed of light in vacuum is 3 x 10e8 ms-1, What is the speed of light in the glass ?\n"
    return q,v1

def type2():
    v2 = 300000000
    v1 = random.randint(1,300000)
    v1 = v1*1000
    r2 = 1
    r1 = str(calculation_r1(r2,v1,v2)) + "\n"
    q = "Light enters from air to glass. If the speed of light in vacuum is 3 x 10e8 ms-1 and in glass is " + str(v1) + " m/s, what is the refractive index of the glass ?\n"
    return q,r1

def type3():
    r1 = random.randint(1,100)
    r1 = round(r1/10,1)
    r2 = random.randint(1,100)
    r2 = round(r2/10,1)
    v1 = random.randint(1,3000)
    v1 = v1*100000
    v2 = str(calculation_v1(r2,r1,v1)) + " m/s\n"
    q = "Light enters from a material-1 having refractive index " + str(r1) + " to material-2 having refractive index " + str(r2) + ". If the speed of the light in material-1 is " + str(v1) + " m/s, what is the speed of light in material-2 ?\n"
    return q,v2

def type4():
    r2 = random.randint(1,100)
    r2 = round(r2/10,1)
    v1 = random.randint(1,300)
    v1 = v1*1000000
    v2 = random.randint(1,300)
    v2 = v2*1000000
    r1 = str(calculation_r1(r2,v1,v2)) + "\n"
    q = "Light enters from a material-1 to material-2 having refractive index " + str(r2) + ". If the speed of light in material-1 and material-2 is " + str(v1) + " m/s and " + str(v2) + " m/s respectively. What is the refractive index of material-1 ?\n"
    return q,r1

def type5():
    r1 = random.randint(1,100)
    r1 = round(r1/10,1)
    r2 = random.randint(1,100)
    r2 = round(r2/10,1)
    v2 = random.randint(1,3000)
    v2 = v2*100000
    v1 = str(calculation_v1(r1,r2,v2)) + " m/s\n"
    q = "Light enters from a material-1 having refractive index " + str(r1) + " to material-2 having refractive index " + str(r2) + ". If the speed of the light in material-2 is" + str(v2) + " m/s, what is the speed of light in material-1 ?\n"
    return q,v1

def type6():
    r2 = random.randint(1,100)
    r2 = round(r2/10,1)
    v1 = random.randint(1,300)
    v1 = v1*1000000
    v2 = random.randint(1,300)
    v2 = v2*1000000
    r1 = str(calculation_r1(r2,v1,v2)) + "\n"
    q = "Light enters from a material-1 having refractive index " + str(r2) + " to material-2. If the speed of light in material-1 and material-2 is " + str(v2) + " m/s and " + str(v1) + " m/s respectively. What is the refractive index of material-2 ?\n"
    return q,r1


for i in range(no_of_samples):
    types = random.randint(1,10)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3 or types == 4:
        ques,answer = type3()
    elif types == 5 or types == 6:
        ques,answer = type4()
    elif types == 7 or types == 8:
        ques,answer = type5()
    elif types == 9 or types == 10:
        ques,answer = type6()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()