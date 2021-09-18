import random
import math

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 30

for i in range(no_of_samples):
    
    u_x = random.randint(1,10)
    u_y = random.randint(1,10)
    a_x = random.randint(1,10)
    a_y = random.randint(1,10)
    
    for i in range(4):
        temp = random.randint(1,2)
        if temp == 2:
            if i == 0:
                u_x = -u_x
            elif i == 1:
                u_y = -u_y
            elif i == 2:
                a_x = -a_x
            elif i == 3:
                a_y = -a_y
    
    t = random.randint(1,100)
    
    q = "A particle starts from origin at t = 0 s with a velocity of ("+str(u_x)+") i + ("+str(u_y)+") j ms-1 and moves in x-y plane with a constant acceleration of ("+str(a_x)+") i + ("+str(a_y)+") j ms-2, then "
    
    types = random.randint(1,6)
    
    if types == 1 or types == 2 or types == 6:
        q = q + "what is the speed of the particle at t = "+str(t) + " s"
        v_x = u_x + a_x*t
        v_y = u_y + a_y*t
        v_mag = math.sqrt(v_x**2+v_y**2)
    
        if types == 1:
            q = q + " (in vector notation) \n"
            a = "("+str(v_x) + ") i + ("+str(v_y) + ") j ms-1\n"
    
        else:
            q = q + "\n"
            a = str(round(v_mag,1)) + " ms-1\n"
    
    elif types == 3:
        v_x = u_x + a_x*t
        v_y = u_y + a_y*t
        q = q + "what is the time taken to reach final velocity of "+str(v_x)+" i + "+str(v_y)+" j ms-1\n"
        a = str(t) + " s\n"
    
    elif types == 4:
        q = q + "what is the x-coordinate after t = "+str(t) + " s\n"
        s_x = u_x*t + (1/2)*a_x*t*t
        a = str(round(s_x,1)) + " m\n"
    
    elif types == 5:
        q = q + "what is the y-coordinate after t = "+str(t) + " s\n"
        s_y = u_y*t + (1/2)*a_y*t*t
        a = str(round(s_y,1)) + " m\n"
    
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)

qns.close()
ans.close()
