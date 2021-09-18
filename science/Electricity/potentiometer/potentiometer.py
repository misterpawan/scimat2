import random

# In a potentiometer arrangement, a cell of emf V V gives a balance point at b1 cm length of the wire. If the cell is replaced by another cell and the balance point shifts to b2 cm, what is the emf of second cell?
# A V+V1 V potentiometer used for the determination of internal resistance of V1 V cell. The balance point of the cell in the open circuit is b1+b2 cm. When a resistor of R ohm is ued in the external circuit, the balance point shifts to b1 cm, find the internal resistance of the cell.
# A potentiometer circuit is used for comparison of two resistances. The balance point with a standard resistance of R1 ohm is found to be b1 cm, while that with the unknown resistor X is b2 cm. Find the value of X?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

for i in range(no_of_samples):
    types = random.randint(1,7)
    if types <= 2:
        V = random.randint(1,200)
        b1 = random.randint(1,200)
        b2 = random.randint(1,200)
        while b2 == b1:
            b2 = random.randint(1,200)
        q = "In a potentiometer arrangement, a cell of emf "+str(V)+" V gives a balance point at "+str(b1)+" cm length of the wire. If the cell is replaced by another cell and the balance point shifts to "+str(b2)+" cm, what is the emf of second cell?\n"
        a = "{:.2e}".format((V*b2)/b1)+" volt\n"
    elif types <= 4:
        R = random.randint(1,200)
        b1 = random.randint(1,200)
        b2 = random.randint(1,200)
        q = "A potentiometer circuit is used for comparison of two resistances. The balance point with a standard resistance of "+str(R)+" ohm is found to be "+str(b1)+" cm, while that with the unknown resistor X is "+str(b2)+" cm. Find the value of X?\n"
        a = "{:.2e}".format((R*b2)/b1)+" ohm\n"
    else:
        V1 = random.randint(1,90)
        V = random.randint(1,20)
        b1 = random.randint(1,90)
        b2 = random.randint(1,20)
        R = random.randint(1,20)
        q = "A "+str(V+V1)+" V potentiometer used for the determination of internal resistance of "+str(V1)+" V cell. The balance point of the cell in the open circuit is "+str(b1+b2)+" cm. When a resistor of "+str(R)+" ohm is ued in the external circuit, the balance point shifts to "+str(b1)+" cm, find the internal resistance of the cell.\n"
        a = "{:.2e} ohm\n".format((b2/b1)*R)
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
