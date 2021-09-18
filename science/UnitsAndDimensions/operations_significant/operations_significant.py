import random


# Two gold pieces of masses are 20.15 g and 20.17 g respectively. What is the sum of the masses of the pieces to correct significant figures?
# Two gold pieces of masses are 20.15 g and 20.17 g respectively. What is the difference in the masses of the pieces to correct significant figures?
# The length and breadth of a rectangular sheet of metal are 4.234 m, 1.005 m respectively. Give the area of the sheet to correct significant figures.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
#no_of_samples = 30

def type_number1():
    left0 = random.randint(0,0)
    middle_non_zero = random.randint(2,4)
    right0 = random.randint(0,3)
    array = ""
    for i in range(left0):
        array += "0"
    for i in range(middle_non_zero):
        if i==0 or i==middle_non_zero-1:
            array += str(random.randint(1,9))
        else:
            array += str(random.randint(0,9))
    for i in range(right0):
        array += "0"
    q = int(array)
    a = middle_non_zero
    return q,a

def type_number2():
    befdecleft0 = random.randint(0,0)
    befdecnonzero = random.randint(1,3)
    befdecright0 = random.randint(0,2)
    aftdecleft0 = random.randint(0,2)
    aftdecnonzero = random.randint(1,3)
    aftdecright0 = random.randint(0,2)
    array = ""
    for i in range(befdecleft0):
        array += "0"
    for i in range(befdecnonzero):
        if i==0 or i==befdecnonzero-1:
            array += str(random.randint(1,9))
        else:
            array += str(random.randint(0,9))
    for i in range(befdecright0):
        array += "0"
    array += "."
    for i in range(aftdecleft0):
        array += "0"
    for i in range(aftdecnonzero):
        if i==0 or i==aftdecnonzero-1:
            array += str(random.randint(1,9))
        else:
            array += str(random.randint(0,9))
    for i in range(aftdecright0):
        array += "0"
    q = float(array)
    a = befdecnonzero + befdecright0 + aftdecleft0 + aftdecnonzero
    return q,a

def type1() :
    temp = random.randint(1,2)
    if temp == 1 :
        number1,a1 = type_number1()
        number2,a2 = type_number1()
    elif temp == 2 :
        number1,a1 = type_number2()
        number2,a2 = type_number2()
    q = "Two gold pieces of masses are " + str(number1) + " g and " + str(number2) + " g respectively. What is the difference of the masses of the pieces to correct significant figures?\n"
    if number1 > number2 :     
        diff = number1 - number2
    else :
        diff = number2 - number1
    number_of_signi = min(a1,a2)
    #print(q, diff, a1, a2 , number_of_signi)
    diff = "{:e}".format(diff)
    diff = str(diff)
    p = diff.split('e')
   # print(p[0])
    ans = str(diff[0]) + "."
    i = 0
    j = 1
    while i < number_of_signi-1 :
        if diff[j] != '.' :
            ans += diff[j]
            i = i+1
        j = j+1
    if ans[len(ans)-1] == '0' :
        ans = ans[:len(ans)-1]
        ans = ans + "1"
    ans = ans + "e" + p[1] + "\n"
    return q, ans
    
def type2() :
    temp = random.randint(1,2)
    if temp == 1 :
        number1,a1 = type_number1()
        number2,a2 = type_number1()
    elif temp == 2 :
        number1,a1 = type_number2()
        number2,a2 = type_number2()
    q = "Two gold pieces of masses are " + str(number1) + " g and " + str(number2) + " g respectively. What is the sum of the masses of the pieces to correct significant figures?\n"
    su = number1 + number2
    number_of_signi = min(a1,a2)
    su = "{:e}".format(su)
    su = str(su)
    p = su.split('e')
    ans = su[0] + "." 
    i = 0
    j = 1
    while i < number_of_signi-1 :
        if su[j] != '.' :
            ans += su[j]
            i = i+1
        j = j+1
    if ans[len(ans)-1] == '0' :
        ans = ans[:len(ans)-1]
        ans = ans + "1"
    ans = ans + "e" + p[1] + "\n"
    return q, ans
    
def type3() :
    temp = random.randint(1,2)
    if temp == 1 :
        l,a1 = type_number1()
        b,a2 = type_number1()
    elif temp == 2 :
        l,a1 = type_number2()
        b,a2 = type_number2()
    q = "The length and breadth of a rectangular sheet of metal are " + str(l) + " cm, " + str(b) + " cm respectively. Give the area of the sheet to correct significant figures.\n"
    pro = round(l*b,15)
    number_of_signi = min(a1,a2)
    pro = "{:e}".format(pro)
    pro = str(pro)
    p = pro.split('e')
    ans = pro[0] + "."
    i = 0
    j = 1
    while i < number_of_signi-1 :
        if pro[j] != '.' :
            ans += pro[j]
            i = i+1
        j = j+1
    if ans[len(ans)-1] == '0' :
        ans = ans[:len(ans)-1]
        ans = ans + "1"
    ans = ans + "e" + p[1] + "\n"
    return q, ans
    
for i in range(no_of_samples):
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