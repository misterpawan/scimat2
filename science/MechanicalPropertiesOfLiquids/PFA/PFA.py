import random
import math

# A 50 kg girl wearing high heel shoes balances on a single heel. The heel is circular with a diameter 1.0 cm. What is the pressure exerted by the heel on the horizontal floor?
# A 50 kg girl wearing high heel shoes. The heels are circular with a diameter 1.0 cm. What is the pressure exerted by each of the heel on the horizontal floor?
# A hydraulic automobile lift is designed to lift cars with a maximum mass of 3000 kg. The area of cross-section of the piston carrying the load is 425 cm2. What maximum pressure would the piston have to bear? 

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1 or types == 2:
        m = random.randint(1000,5000)
        area = random.randint(1000,5000)*10
        q = "A hydraulic automobile lift is designed to lift cars with a maximum mass of "+str(m)+" kg. The area of cross-section of the piston carrying the load is "+str(area)+" mm2. What maximum pressure would the piston have to bear?"
        if types == 1:
            q = q + " (in pascal)\n"
            p = (m*9.8/(area*(10**(-6))))
            a = "{:.2e}".format(p) + " pascal\n"
        else:
            q = q + " (in atmosphere)\n"
            p = (m*9.8/(area*(10**(-6))))/(1.013*(10**5))
            a = str(round(p,1)) + " atmosphere\n"
    else:
        m = random.randint(40,110)
        diameter = random.randint(5000,35000)
        q = "A "+str(m)+" kg girl wearing high heel shoes balances on a single heel. The heel is circular with a diameter "+str(diameter)+" micrometer. What is the pressure exerted by the heel on the horizontal floor?\n"
        area = (math.pi*diameter*diameter*(10**(-12)))/4
        if types == 3:
            p = (m*9.8)/(area)
            a = "{:.2e}".format(p) + " newton\n"
        else:
            q = "A "+str(m)+" kg girl wearing high heel shoes. The heels are circular with a diameter "+str(diameter)+" micrometer. What is the pressure exerted by each of the heel on the horizontal floor?\n"
            p = (m*4.9)/(area)
            a = "{:.2e}".format(p) + " newton\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()