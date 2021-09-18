import random

# Two objects of masses m1 g and m2 g are moving along the same line and direction with velocities of u1 m/s and u2 m/s respectively. They collide and after the collision the first object moves at
# a velocity of v1 m/s. Determine the velocity of the second object.
# Two objects of masses m1 g and m2 g are moving along the same line and direction with velocities of u1 m/s and u2 m/s respectively. They collide and after the collision the second object moves at
# a velocity of v2 m/s. Determine the velocity of the first object. 
# Two objects of masses m1 g and m2 g are moving along the same line. They collide and after collision their velocities are v1 m/s and v2 m/s respectively. If the velocity of first 
# body before collision is u1 m/s, then determine the velocity of second object before collision.
# Two objects of masses m1 g and m2 g are moving along the same line. They collide and after collision their velocities are v1 m/s and v2 m/s respectively. If the velocity of second 
# body before collision is u2 m/s, then determine the velocity of first object before collision.
# Two objects are moving along the same line and direction with velocities of u1 m/s and u2 m/s respectively. They collide and after the collision their velocities are v1 m/s abd v2 m/s respectively.
# If the mass of first object is m1 g, then determine the mass of second object.
# Two objects are moving along the same line and direction with velocities of u1 m/s and u2 m/s respectively. They collide and after the collision their velocities are v1 m/s abd v2 m/s respectively.
# If the mass of second object is m2 g, then determine the mass of first object.

  
qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000

def calculation_v1(m1, m2, u1, u2, v2): 
    return round(((m1*u1)+(m2*u2)-(m2*v2))/m1,1)

def calculation_v2(m1, m2, u1, u2, v1): 
    return round(((m1*u1)+(m2*u2)-(m1*v1))/m2,1)

def calculation_u1(m1, m2, u2, v1, v2): 
    return round(((m1*v1)+(m2*v2)-(m2*u2))/m1,1)

def calculation_u2(m1, m2, u1, v1, v2): 
    return round(((m1*v1)+(m2*v2)-(m1*u1))/m2,1)

def calculation_m1(m2, u1, u2, v1, v2):
    return round((m2*(v2-u2))/(u1-v1),1)

def calculation_m2(m1, u1, u2, v1, v2):
    return round((m1*(v1-u1))/(u2-v2),1)

def type1():
    m1 = random.randint(1,15)
    m2 = random.randint(1,15)
    u1 = random.randint(1,30)
    u2 = random.randint(1,30)
    v1 = random.randint(1,30)
    q = "Two objects of masses " + str(m1) + " g and " + str(m2) + " g are moving along the same line and direction with velocities of " + str(u1) + " m/s and " + str(u2) + " m/s respectively. They collide and after the collision the first object moves at a velocity of " + str(v1) + " m/s. Determine the velocity of the second object.\n"
    v2 = str(calculation_v2(m1, m2, u1, u2, v1)) + " m/s\n"
    return q,v2

def type2():
    m1 = random.randint(1,15)
    m2 = random.randint(1,15)
    u1 = random.randint(1,30)
    u2 = random.randint(1,30)
    v2 = random.randint(1,30)
    q = "Two objects of masses " + str(m1) + " g and " + str(m2) + " g are moving along the same line and direction with velocities of " + str(u1) + " m/s and " + str(u2) + " m/s respectively. They collide and after the collision the second object moves at a velocity of " + str(v2) + " m/s. Determine the velocity of the first object.\n"
    v1 = str(calculation_v1(m1, m2, u1, u2, v2)) + " m/s\n"
    return q,v1

def type3():
    m1 = random.randint(1,15)
    m2 = random.randint(1,15)
    u1 = random.randint(1,30)
    v1 = random.randint(1,30)
    v2 = random.randint(1,30)
    q = "Two objects of masses " + str(m1) + " g and " + str(m2) + " g are moving along the same line. They collide and after collision their velocities are " + str(v1) + " m/s and " + str(v2) + " m/s respectively. If the velocity of first object before collision is " + str(u1) + " m/s, then determine the velocity of second object before collision.\n"
    u2 = str(calculation_u2(m1, m2, u1, v1, v2)) + " m/s\n"
    return q,u2

def type4():
    m1 = random.randint(1,15)
    m2 = random.randint(1,15)
    u2 = random.randint(1,30)
    v1 = random.randint(1,30)
    v2 = random.randint(1,30)
    q = "Two objects of masses " + str(m1) + " g and " + str(m2) + " g are moving along the same line. They collide and after collision their velocities are " + str(v1) + " m/s and " + str(v2) + " m/s respectively. If the velocity of second object before collision is " + str(u2) + " m/s, then determine the velocity of first object before collision.\n"
    u1 = str(calculation_u1(m1, m2, u2, v1, v2)) + " m/s\n"
    return q,u1

def type5():
    m1 = random.randint(1,10)
    u2 = random.randint(1,30)
    v1 = random.randint(1,30)
    u1 = random.randint(v1+1,v1+30)
    v2 = random.randint(u2+1,u2+30)
    q = "Two objects are moving along the same line and direction with velocities of " + str(u1) + " m/s and " + str(u2) + " m/s respectively. They collide and after the collision their velocities are " + str(v1) + " m/s and " + str(v2) + " m/s respectively. If the mass of first object is " + str(m1) + " g, then determine the mass of second object.\n"
    m2 = str(calculation_m2(m1, u1, u2, v1, v2)) + " g\n"
    return q,m2

def type6():
    m2 = random.randint(1,10)
    v2 = random.randint(1,30)
    u1 = random.randint(1,30)
    v1 = random.randint(u1+1,u1+30)
    u2 = random.randint(v2+1,v2+30)
    q = "Two objects are moving along the same line and direction with velocities of " + str(u1) + " m/s and " + str(u2) + " m/s respectively. They collide and after the collision their velocities are " + str(v1) + " m/s and " + str(v2) + " m/s respectively. If the mass of second object is " + str(m2) + " g, then determine the mass of first object.\n"
    m1 = str(calculation_m1(m2, u1, u2, v1, v2)) + " g\n"
    return q,m1

for i in range(no_of_samples):
    types = random.randint(0,5)
    if types == 0:
        ques,answer = type1()
    elif types == 1:
        ques,answer = type2()
    elif types == 2:
        ques,answer = type3()
    elif types == 3 :
        ques,answer = type4()
    elif types == 4 :
        ques,answer = type5()
    elif types == 5 :
        ques,answer = type6()
    qns.write(ques)
    ans.write(answer)
    
qns.close()
ans.close()

