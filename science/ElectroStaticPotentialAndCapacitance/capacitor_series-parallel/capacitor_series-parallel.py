import random

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

for i in range(no_of_samples):
    n = random.randint(1,20)
    c = random.randint(1,500)
    v = random.randint(1,500)
    if random.randint(0,1):
        if random.randint(0,1):
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in series. What is the total capacitance of the combination when the system is connected to a "+str(v) +" V supply?\n"
            a = "{:.2e}".format(c/n) + " pico-farad\n"
        else:
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in series. What is the potential difference across each capacitor if the combination is connected to a "+str(v) +" V supply?\n"
            a = "{:.2e}".format(v/n) + " volt\n"
    else:
        if random.randint(0,1):
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in parallel. What is the total capacitance of the combination when the system is connected to a "+str(v) +" V supply?\n"
            a = "{:.2e}".format(c*n) + " pico-farad\n"
        else:
            q = str(n)+" capacitors each of capacitance "+str(c)+ "pF are connected in parallel. What is the charge on each capacitor if the combination is connected to a "+str(v) +" V supply?\n"
            a = "{:.2e}".format(c*v) + " pico-coulomb\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close() 