import random

# A copper block of mass 2.5 kg is heated in a furnace to a temperature of 500°C and then placed on a large ice block. What is the maximum amount of ice that can melt? Specific heat of copper is 0.39 Jg-1°C-1. Heat of fusion of water = 335 Jg-1.
# A alluminium block of mass 2.5 kg is heated in a furnace to a temperature of 500°C and then placed on a large ice block. What is the maximum amount of ice that can melt? Specific heat of alluminium is 0.91 Jg-1°C-1. Heat of fusion of water = 335 Jg-1.

qns = open('./questions.txt', 'w')
ans = open('./answers.txt','w')

no_of_samples = 1000000

def cal1(m, t1, s) :
    return round((m*t1*s)/(335),1)

def type1() :
    m = random.randint(1000,4000)
    t1 = random.randint(500,1000)
    t = random.randint(1,2)
    if t == 1 :
        q = "A copper block of mass " + str(m) + " g is heated in a furnace to a temperature of " + str(t) + " degree C and then placed on a large ice block. What is the maximum amount of ice that can melt? Specific heat of copper is 0.39 Jg-1°C-1. Heat of fusion of water = 335 Jg-1.\n"
    else :
        q = "A alluminium block of mass " + str(m) + " g is heated in a furnace to a temperature of " + str(t) + " degree C and then placed on a large ice block. What is the maximum amount of ice that can melt? Specific heat of alluminium is 0.39 Jg-1°C-1. Heat of fusion of water = 335 Jg-1.\n"
    if t == 1 :
        w = str(cal1(m, t1, 0.39)) + " g\n"
    elif t == 2 :
        w = str(cal1(m, t1, 0.91)) + " g\n"
    return q,w

for i in range(no_of_samples):
    ques, answer = type1()
    qns.write(ques)
    ans.write(answer)

qns.close()
ans.close()
