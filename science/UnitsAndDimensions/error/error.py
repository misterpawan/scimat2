import random

# If a physical quantity P=(a^1)*(b^2)*(c^3), the percentage errors of measurement in a,b,c are pa,pb,pc respectively. If the calculated value of P is act_p then what is maximum error possible.

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 10
for i in range(no_of_samples):
    pow_a = round(random.randint(-6,6)/2,1)
    pow_b = round(random.randint(-6,6)/2,1)
    pow_c = round(random.randint(-6,6)/2,1)
    error_a = random.randint(1,5)
    error_b = random.randint(1,5)
    error_c = random.randint(1,5)
    value = random.randint(1,40)
    expr = '(a^'+str(pow_a)+')*(b^'+str(pow_b)+')*(c^'+str(pow_c)+')'
    ques = "If a physical quantity P="+expr+", the percentage errors of measurement in a,b,c are "+str(error_a)+"%,"+str(error_b)+"%,"+str(error_c)+"% respectively. If the calculated value of P is "+str(value)+" then what is maximum error possible.\n"
    answer = str(round(((abs(pow_a)*error_a+abs(pow_b)*error_b+abs(pow_c)*error_c)*value)/100,2)) + '\n'
    # print(ques,answer)
    qns.write(ques)
    ans.write(answer)
qns.close()
ans.close()