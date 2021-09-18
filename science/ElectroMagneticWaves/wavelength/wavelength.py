import random

# A plane electromagnetic wave travels in vacuum along z-direction. If the frequency of the wave is f Hz, what is its wavelength?
# A radio can tune in to any station in the f1 kHz to f2 kHz band. What is the corresponding wavelength band?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    types = random.randint(1,2)
    if types == 1:
        f = random.randint(1,2000000)*100
        q = "A plane electromagnetic wave travels in vacuum along z-direction. If the frequency of the wave is "+str(f)+" Hz, what is its wavelength?\n"
        lamda = (3*(10**8))/(f)
        a = str(round(lamda,2)) + " m\n"
    else:
        f1 = random.randint(1,2000)
        f2 = random.randint(f1+1,f1+2000)
        q = "A radio can tune in to any station in the "+str(f1)+" kHz to "+str(f1+f2)+" kHz band. What is the corresponding wavelength band?\n" 
        lamda1 = (3*(10**5))/(f1)
        lamda2 = (3*(10**5))/(f1+f2)
        a = str(round(lamda2,2)) + " m to "+str(round(lamda1,2)) + " m\n"
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
