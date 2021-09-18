import random

# A bat emits ultrasonic sound of frequency 1000 kHz in air. If this sound meets a water surface, what is the wavelength of (a) the reflected sound, (b) the transmitted sound? Speed of sound in air = 340 ms-1 and in water = 1486 ms-1.
# A hospital uses an ultrasonic scanner to locate tumours in a tissue. What is the wavelength of sound in a tissue in which the speed of sound is 1.7 km s-1? The operating frequency of the scanner is 4.2 MHz.

qns = open('./questions.txt','w') 
ans = open('./answers.txt','w')
no_of_samples = 1500000
# no_of_samples = 20

for i in range(no_of_samples):
    types = random.randint(1,3)
    if types == 1:
       speed = random.randint(1000,4000)
       freq = random.randint(1000,6000)
       q = "A hospital uses an ultrasonic scanner to locate tumours in a tissue. What is the wavelength of sound in a tissue in which the speed of sound is "+str(speed)+" kms-1? The operating frequency of the scanner is "+str(freq)+" kHz.?\n"
       a = speed/(freq*1000)
       a = "{:.2e}".format(a) + " m\n"
    else:
        freq = random.randint(100000,2100000)
        if types == 2:
            q = "A bat emits ultrasonic sound of frequency "+str(freq)+" Hz in air. If this sound meets a water surface, what is the wavelength of the reflected sound? (Speed of sound in air = 340 ms-1 and in water = 1486 ms-1)\n"
            a = "{:.2e}".format(340/freq) + " m\n"
        else:
            q = "A bat emits ultrasonic sound of frequency "+str(freq)+" Hz in air. If this sound meets a water surface, what is the wavelength of the transmitted sound? (Speed of sound in air = 340 ms-1 and in water = 1486 ms-1)\n"
            a = "{:.2e}".format(1486/freq) + " m\n"
    qns.write(q)
    ans.write(a)
    # print(q)
    # print(a)
qns.close()
ans.close()