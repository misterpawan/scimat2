import random
import math

# The peak voltage of an ac supply is 300 V. What is the rms voltage?
# The rms value of current in an ac circuit is 10 A. What is the peak current?

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 1000000
sqrt2 = math.sqrt(2)

for i in range(no_of_samples):
    types = random.randint(1,2)
    val = random.randint(1,2000000)
    if types == 1:
        q = "The peak voltage of an ac supply is "+str(val)+" mV. What is the rms voltage?\n"
        a = "{:.3e} volt\n".format((val*0.001)/sqrt2)
    elif types == 2:
        q = "The rms value of current in an ac circuit is "+str(val)+" microampere. What is the peak current?\n"
        a = "{:.3e} ampere\n".format(val*0.000001*sqrt2)
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()