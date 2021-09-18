import random

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    types = random.randint(1,5)
    balance_pt = random.randint(0,1000)
    R1 = random.randint(1,4000)
    q = "In a metre bridge, the balance point is found to be at "+str(balance_pt)+" mm from end A, when the resistor Y is of "+str(R1)+" ohm. "
    if types != 1:
        q = q + "Determine the resistance of X.\n"
        a = str(round(((1000-balance_pt)/balance_pt)*R1,1))+" ohm\n"
    else:
        q = q + "Determine the balance point of the bridge above if X and Y are interchanged.\n"
        a = str(1000-balance_pt)+ " mm\n"
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
