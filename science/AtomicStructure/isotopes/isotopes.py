import random

# If an atom X is available in the form of say, two isotopes having atomic masses 79u (49.7%) and 81u (50.3%), calculate the average atomic mass of the atom.
# If an atom X is available in the form of say, three isotopes having atomic masses 79u (10%), 80u (40%) and 81u (50%), calculate the average atomic mass of the atom.
# The average atomic mass of a sample of an element X is 16.2 u. What are the percentages of isotopes of X having atomic masses 16 and 18 in the sample?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000

def calculation_1(a1, p1, a2, p2) :
    return round(((a1*p1)+(a2*p2))/100,1)
def calculation_2(a1, p1, a2, p2, a3, p3) :
    return round(((a1*p1)+(a2*p2)+(a3*p3))/100,1)
def calculation_3(a1, a, a2) :
    p1 = round(((a-a2)*100)/(a1-a2),1)
    p2 = 100.0 - p1
    return p1, round(p2,1)

def type1() :
    p1 = random.randint(1,999)
    p1 = round(p1/10,1)
    p2 = round(100.0 - p1,1)
    a1 = random.randint(1,300)
    a2 = 0
    while a2 == a1 or a2 == 0 :
        if a1 - 5 > 0 :
            a2 = random.randint(a1-5,a1+5)
        else :
            a2 = random.randint(1,a1+5)
    q = "If an atom X is available in the form of say, two isotopes having atomic masses " + str(a1) + " u (" + str(p1) + "%) and " + str(a2) + " u (" + str(p2) + "%), calculate the average atomic mass of the atom.\n"
    avg_mass = str(calculation_1(a1, p1, a2, p2)) + "u\n"
    return q, avg_mass

def type2() :
    p1 = random.randint(1,970)
    p1 = round(p1/10,1)
    remain = round(100.0 - p1)
    p2 = random.randint(1,10*(int(remain)-1))
    p2 = round(p2/10,1)
    p3 = remain - p2
    a1 = random.randint(1,300)
    a2 = 0
    while a2 == 0 or a2 == a1 :
        if a1 - 5 > 0 :
            a2 = random.randint(a1-5,a1-1)
            a3 = random.randint(a1+1,a1+5)
        else :
            a2 = random.randint(1,a1+2)
            a3 = random.randint(a2+1,a2+5)
    q = "If an atom X is available in the form of say, three isotopes having atomic masses " + str(a1) + " u (" + str(p1) + "%), " + str(a2) + " u (" + str(p2) + "%) and " + str(a3) + " u (" + str(p3) + "%), calculate the average atomic mass of the atom.\n"
    avg_mass = str(calculation_2(a1, p1, a2, p2, a3, p3)) + "u\n"
    return q, avg_mass

def type3() :
    avg_mass = random.randint(600,30000)
    avg_mass = round(avg_mass/100,2)
    temp = int(avg_mass)
    a1 = random.randint(temp-5,temp-1)
    a2 = random.randint(temp+1,temp+5)
    q = "The average atomic mass of a sample of an element X is " + str(avg_mass) + " u. What are the percentages of isotopes of X having atomic masses " + str(a1) + " and " + str(a2) + " in the sample?\n"
    p1,p2 = calculation_3(a1, avg_mass, a2)
    percentages = str(p1) + "%" + " and" + str(p2) + "%\n"
    return q, percentages

for i in range(no_of_samples) :
    types = random.randint(1,3)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()



