import random

# Two bodies A and B of masses m1 kg and m2 kg are in contact with each other rest on a table against a rigid wall (such that B is attached to the wall). The coefficient of friction between the bodies and the table is mu. A force of F N is applied horizontally to A. Then what is the reaction of the partition.
# Two bodies A and B of masses m1 kg and m2 kg are in contact with each other rest on a table against a rigid wall (such that B is attached to the wall). The coefficient of friction between the bodies and the table is mu. A force of F N is applied horizontally to A. Then what is the value of action-reaction forces between A and B.
# Two bodies A and B of masses m1 kg and m2 kg are in contact with each other rest on a table. The coefficient of friction between the bodies and the table is mu. A force of F N is applied horizontally to A. Then what is the value of action-reaction forces between A and B.
# Two bodies A and B of masses m1 kg and m2 kg are in contact with each other rest on a table. The coefficient of friction between the bodies and the table is mu. A force of F N is applied horizontally to A. Then what is the value of acceleration.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20
for i in range(no_of_samples):
    m1 = random.randint(1,20)
    m2 = random.randint(1,20)
    mu = round(random.randint(0,100)/100,2)
    F = random.randint(1,270)
    g = 10
    type = random.randint(1,6)
    if type == 1:
        q = "Two bodies A and B of masses "+str(m1)+" kg and "+str(m2)+" kg are in contact with each other rest on a table against a rigid wall (such that B is attached to the wall). The coefficient of friction between the bodies and the table is "+str(mu)+". A force of "+str(F)+" N is applied horizontally to A. Then what is the reaction of the partition.\n"
        a = str(F)+" newton\n"
    elif type == 2:
        q = "Two bodies A and B of masses "+str(m1)+" kg and "+str(m2)+" kg are in contact with each other rest on a table against a rigid wall (such that B is attached to the wall). The coefficient of friction between the bodies and the table is "+str(mu)+". A force of "+str(F)+" N is applied horizontally to A. Then what is the value of action-reaction forces between A and B.\n"
        a = str(F)+" newton\n"
    elif type == 3 or type == 4:
        q = "Two bodies A and B of masses "+str(m1)+" kg and "+str(m2)+" kg are in contact with each other rest on a table. The coefficient of friction between the bodies and the table is "+str(mu)+". A force of "+str(F)+" N is applied horizontally to A. Then what is the value of action-reaction forces between A and B.\n"
        if F <= mu*m1*g:
            a = "0 newton\n"
        elif F <= mu*(m1+m2)*g:
            a = str(round(F-mu*m1*g,1))+" newton\n"
        else:
            a = str(round(mu*m2*g,1))+" newton\n"
    else:
        q = "Two bodies A and B of masses "+str(m1)+" kg and "+str(m2)+" kg are in contact with each other rest on a table. The coefficient of friction between the bodies and the table is "+str(mu)+". A force of "+str(F)+" N is applied horizontally to A. Then what is the value of acceleration.\n"
        if F <= mu*(m1+m2)*g:
            a = "0 ms-2\n"
        else:
            expr = (F - mu*(m1+m2)*g)/(m1+m2)
            a = str(round(expr,1)) + " ms-2\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()