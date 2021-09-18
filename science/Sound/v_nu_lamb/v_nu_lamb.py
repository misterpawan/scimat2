import random

# Calculate the wavelength of a sound wave whose frequency is f hz and speed is v m/s in a given medium. 
# Calculate the frequency of a sound wave whose wavelength is lamb m and speed is v m/s in a given medium. 
# Calculate the speed of a sound wave whose frequency is f hz and wavelength is lamb m in a given medium. 

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 8

def calculation_lamb(f, v): 
    return v // f

def calculation_f(lamb, v):
    return v // lamb

def calculation_v(f , lamb):
    return f*lamb

def type1():
    f = random.randint(1,1000)
    v = (random.randint(1,1000))*f
    lamb = str(calculation_lamb(f,v)) + " m\n"
    q = "Calculate the wavelength of a sound wave whose frequency is "+str(f)+" hz and speed is "+str(v)+" m/s in a given medium ?\n"
    return q,lamb

def type2():
    lamb = random.randint(1,1000)
    v = (random.randint(1,1000))*lamb
    f = str(calculation_f(lamb,v)) + " hz\n"
    q = "Calculate the frequency of a sound wave whose wavelength is "+str(lamb)+" m and speed is "+str(v)+" m/s in a given medium ?\n"
    return q,f

def type3():
    f = random.randint(1,2000)
    lamb = random.randint(1,1000)
    v = str(calculation_v(f,lamb)) + " m/s\n"
    q = "Calculate the speed of a sound wave whose frequency is "+str(f)+" hz and wavelength is "+str(lamb)+" m in a given medium ?\n"
    return q,v

for i in range(no_of_samples):
    types = random.randint(0,3)
    if types == 0:
        ques,answer = type1()
    if types == 1:
        ques,answer = type2()
    if types == 2 or types == 3:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
