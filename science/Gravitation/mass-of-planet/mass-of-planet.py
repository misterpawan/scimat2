import random

# Assume an unknown planet of orbital period 1.7 days is rotating around the sun with orbit of radius r m. What is the ratio of mass of the sun to mass of the unknown planet.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 30
g = 10

for i in range(no_of_samples):
    days = random.randint(200,2000)
    r = random.randint(1,2000)
    q = "Assume an unknown planet of orbital period "+str(days)+" days is rotating around the sun with orbit of radius "+str(r)+" *10^(8)m. What is the ratio of mass of the sun to mass of the unknown planet.\n"
    days_earth = 365.25
    rad_earth = 1496 * (10**8)
    a = ((rad_earth**3)*(days**2))/((r**3*(10**24))*(days_earth**2))
    a = str(round(a,1)) + "\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()