import random

# The volume of 50 g of a substance is 20 cm3. If the density of water is 1 g/cm 3, 
# will the substance float or sink?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 2000000

for i in range(no_of_samples):
    mass = random.randint(1,2000)
    volume = random.randint(1,200)
    density_another = random.randint(1,10)
    ques = "The volume of " + str(mass) + " g of a substance is " + str(volume) + " cm3. If the density of liquid in which substance is placed is " + str(density_another) + " g/cm3, will the substance float or sink ?\n"
    qns.write(ques)
    answer = ""
    if mass/volume == density_another:
        answer = "just sink\n"
    elif mass/volume > density_another:
        answer = "sink\n"
    else:
        answer = "float\n" 
    ans.write(answer)
    # print(ques)
    # print(answer)
    
qns.close()
ans.close()
