import random

# A wire of material-1 of length 4.7 m and cross-sectional area 3.0 x 10-5 m2 stretches by the same amount as a wire of material-2 of length 3.5 m and cross-sectional area of 4.0 x 10-5 m2 under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2?

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000
# no_of_samples = 20

for i in range(no_of_samples):
    l1 = random.randint(1,200)
    l2 = random.randint(1,200)
    A1 = random.randint(1,20)
    A2 = random.randint(1,20)
    types = random.randint(1,4)
    if types == 1:
        ratio = str(A1)+"/"+str(A2)
        q = "A wire of material-1 of length "+str(l1)+" m stretches by the same amount as a wire of material-2 of length "+str(l2)+" m under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2 assuming ratio of their cross-sectional areas is "+ratio+" ?\n"
    elif types == 2:
        ratio = str(l1)+"/"+str(l2)
        q = "A wire of material-1 of cross-sectional area "+str(A1)+" x 10-6 m2 stretches by the same amount as a wire of material-2 of cross-sectional area "+str(A2)+" x 10-6 m2 under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2 assuming ratio of their lengths is "+ratio+" ?\n"
    else:
        q = "A wire of material-1 of length "+str(l1)+" m and cross-sectional area "+str(A1)+" x 10-6 m2 stretches by the same amount as a wire of material-2 of length "+str(l2)+" m and cross-sectional area of "+str(A2)+" x 10-6 m2 under a given load. What is the ratio of the Young’s modulus of material-1 to that of material-2?\n"
    num = l1*A2
    den = l2*A1
    a = str(num)+"/"+str(den)+"\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()
