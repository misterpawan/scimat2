import random
from sympy import *

# If the position of the particle is given by r = 3t i + 2t^2 j + 4 k m, where t is in seconds, what is the velocity of particle (in vector notation), it's magnitude and direction at t = 10 sec.
# If the position of the particle is given by r = 3t i + 2t^2 j + 4 k m, where t is in seconds, what is the acceleration of particle (in vector notation), it's magnitude and direction at t = 10 sec.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 30
array = ['velocity','acceleration']

for i in range(no_of_samples):
    x_num = random.randint(1,20)
    if random.randint(0,1):
        x_num = -x_num
    y_num = random.randint(1,20)
    if random.randint(0,1):
        y_num = -y_num
    z_num = random.randint(1,20)
    if random.randint(0,1):
        z_num = -z_num
    x_pow = random.randint(0,4)
    y_pow = random.randint(0,4)
    z_pow = random.randint(0,4)
    select = random.randint(0,1)
    qtype = array[select]
    t = symbols('t')
    x_exp = x_num*(t**x_pow)
    y_exp = y_num*(t**y_pow)
    z_exp = z_num*(t**z_pow)
    q = "If the position of the particle is given by r = ("+str(x_exp)+") i + ("+str(y_exp)+") j + ("+str(z_exp)+") k m, where t is in sec, what is the "+str(qtype)+" of particle (in vector notation)?\n"
    x_der = Derivative(x_exp,t).doit()
    y_der = Derivative(y_exp,t).doit()
    z_der = Derivative(z_exp,t).doit()
    if select == 0:
        a = "("+str(x_der) + ") i + ("+str(y_der) + ") j + ("+str(z_der)+") k ms-1\n"
    else:
        x_der2 = Derivative(x_der,t).doit()
        y_der2 = Derivative(y_der,t).doit()
        z_der2 = Derivative(z_der,t).doit()
        a = "("+str(x_der2) + ") i + ("+str(y_der2) + ") j + ("+str(z_der2)+") k ms-2\n"       
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(x_exp,y_exp,z_exp,x_der,y_der,z_der)
    # print(a)
qns.close()
ans.close()