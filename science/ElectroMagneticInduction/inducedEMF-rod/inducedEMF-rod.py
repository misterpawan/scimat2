import random

# A l m long metallic rod is rotated with an angular frequency of f rad s-1 about an axis normal to rod passing through one of its end. The other end of rod is in contact with a circular mettalic ring. A uniform magnetic field is B T parallel to axis exists everywhere. Find emf developed between the centre and the ring.

ques = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 500000

for i in range(no_of_samples):
    B = random.randint(1,200)
    l = random.randint(10,210)
    w = random.randint(1,200)
    q = "A "+str(l)+" cm long metallic rod is rotated with an angular frequency of "+str(w)+" rad s-1 about an axis normal to rod passing through one of its end. The other end of rod is in contact with a circular mettalic ring. A uniform magnetic field is "+str(B)+" T parallel to axis exists everywhere. Find emf developed between the centre and the ring.\n"
    a = "{:.2e} volt\n".format((B*l*w*w)/2)

    ques.write(q)
    ans.write(a)

ques.close()
ans.close()