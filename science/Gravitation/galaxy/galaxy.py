import random
import math

# Let us assume that our galaxy consists of 2.5 x 1011 stars each of one solar mass. How long will a star at a distance of 50,000 ly from the galactic centre take to complete one revolution? Take the diameter of the Milky way to be 10^5 ly.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000
# no_of_samples = 30
g = 10

for i in range(no_of_samples):
    no_of_stars = random.randint(1,300)
    distance = random.randint(30000,70000)
    q = "Let us assume that our galaxy consists of "+str(no_of_stars)+" * 10^9 stars each of one solar mass. How long will a star at a distance of "+str(distance)+" ly from the galactic centre take to complete one revolution? Take the diameter of the Milky way to be 10^5 ly.\n"
    distm = distance * 9.46 * (10**15)
    num = 4*((math.pi)**2)*(distm)
    den = 6.67*(10**(-11))*(5*(10**(41)))
    time = math.sqrt((num/den))
    a = "{:.3e}".format(time)+" s\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()