import random

# In a plane electromagnetic wave, the electric field oscillates sinusoidally at a frequency of f1 Hz and amplitude A V/m.
# (a) What is the wavelength of the wave?
# (b) What is the amplitude of the oscillating magnetic field?

qns = open('./questions.txt', 'w') 
ans = open('./answers.txt','w')
no_of_samples = 1000000

for i in range(no_of_samples):
    types = random.randint(1,2)
    f = random.randint(1,2000)
    A = random.randint(1,2000)
    q = "In a plane electromagnetic wave, the electric field oscillates sinusoidally at a frequency of "+str(f)+" x 10^8 Hz and amplitude "+str(A)+" V/m. "
    if types == 1:
        q = q + "What is the wavelength of the wave?\n"
        a = "{:.2e} m\n".format(3/f)
    elif types == 2:
        q = q + "What is the amplitude of the oscillating magnetic field?\n"
        a = "{:.2e} tesla\n".format(A/(3*(10**8)))
    qns.write(q)
    ans.write(a)
    
qns.close()
ans.close()
