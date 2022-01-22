import random

# Number of significant digits in abcdefg
# Number of significant digits in 0.abcdefg
# Number of significant digits in abc.defg

'''
Rules:
1) All non-zero digits are significant. Eg: 4362 --> 4
2) All zeros occuring between non-zero digits are significant. Eg: 1005 --> 4
3) All zeros to the right of the last non-zero digit are not significant. Eg: 6250 --> 3
4) In a number less than one, all zeros to the right of decimal point and to the 
    left of a non-zero decimal point are not significant. Eg: 0.00325 --> 3
5) All zeros to the right of a non-zero digit in the decimal part are significant. Eg: 1.4750 --> 5
'''
qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 3000000
# no_of_samples = 30

def type1():
    left0 = random.randint(0,3)
    middle_non_zero = random.randint(5,9)
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
    q = "Number of significant digits in "+str(array)+"\n"
    des = str(left0)+" zeros to the left of first non zero digit are not significant, "+str(middle_non_zero)+" digits(which start and end with non zero digit) in between are significant, "+str(right0)+" digits to the right of last non-zero digits are not significant, in total "+str(middle_non_zero)+" digits are significant.\n"
    return q,des

def type2():
    left0 = random.randint(0,3)
    middle_non_zero = random.randint(5,9)
    right0 = random.randint(0,3)
    array = "0."
    for i in range(left0):
        array += "0"
    for i in range(middle_non_zero):
        if i==0 or i==middle_non_zero-1:
            array += str(random.randint(1,9))
        else:
            array += str(random.randint(0,9))
    for i in range(right0):
        array += "0"
    q = "Number of significant digits in "+str(array)+"\n"
    des = str(left0)+" zeros after the decimal point to the left of first non zero digit are not significant, "+str(middle_non_zero)+" digits(which start and end with non zero digit) in between are significant, "+str(right0)+" digits to the right of last non-zero digits are significant(as they are after decimal point), in total "+str(middle_non_zero)+" + "+str(right0)+" = "+str(middle_non_zero+right0)+" digits are significant.\n"
    return q,des

def type3():
    befdecleft0 = random.randint(0,2)
    befdecnonzero = random.randint(4,7)
    befdecright0 = random.randint(0,2)
    aftdecleft0 = random.randint(0,2)
    aftdecnonzero = random.randint(4,7)
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
    q = "Number of significant digits in "+str(array)+"\n"
    des = str(befdecleft0)+" zeros to the left of decimal and left of non zero digit are not significant, "+str(befdecnonzero+befdecright0+aftdecleft0+aftdecnonzero)+" digits in total before and after decimal between non zero digits on ends are all significant, "+str(aftdecright0)+" digits to the right of decimal, right of non zero digit are significant(as they are after decimal point), in total "+str(befdecnonzero+befdecright0+aftdecleft0+aftdecnonzero)+" + "+str(aftdecright0)+" = "+str(befdecnonzero + befdecright0 + aftdecleft0 + aftdecnonzero + aftdecright0)+" digits are significant.\n"
    return q,des

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
        ques,answer = type1()
    elif types == 2:
        ques,answer = type2()
    elif types == 3:
        ques,answer = type3()
    # print(ques)
    # print(answer)
    qns.write(ques)
    ans.write(answer)