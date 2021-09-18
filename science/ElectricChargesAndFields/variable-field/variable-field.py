import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 20

for i in range(no_of_samples):
    rate = random.randint(1,2000)*100
    dipole_moment = random.randint(1,2000)
    q = "If in a space electric field is along z-axis, increases uniformly along +ve z-direction, at the rate of "+str(rate)+" NC-1 per metre. What are the values of force and torque experienced by a system having total dipole moment of "+str(dipole_moment)+" x 10^(-9) Cm in negative z-direction?\n"
    a = "force is "+"{:.2e}".format(rate*dipole_moment*(10**(-9)))+" newton, torque is 0 newton-m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
