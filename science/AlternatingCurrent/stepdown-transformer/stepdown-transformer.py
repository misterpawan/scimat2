import random
import math

# A power transformer line feeds input power at 2300 V to a stepdown transformer with its primary windings having 4000 turns. What should be the number of turns in the secondary in order to get output at 230 V?
# A small town with a demand of 800 kW of electric power at 220 V is situated 15 km away from an electric plant generating power at 440 V. The resistance of two wire carrying power is 0.5 ohm per km. The town gets power from the line through 4000 - 220 V step down transformer at a sub-station in the town.
# (a) Estimate the power loss in the form of heat.
# (b) How much power does the plant supply, assuming there is negligible power loss due to leakage?
# (c) Characterise the step up transformer at the plant.

qns = open('./questions.txt','w')
ans = open('./answers.txt','w')
no_of_samples = 2000000

for i in range(no_of_samples):
    types = random.randint(1,4)
    if types == 1:
        V = random.randint(220,240)
        turns = random.randint(10,500)
        scale = random.randint(10,500)
        q = "A power transformer line feeds input power at "+str(scale*V)+" V to a stepdown transformer with its primary windings having "+str(turns*scale)+" turns. What should be the number of turns in the secondary in order to get output at "+str(V)+" V?\n"
        a = str(turns)+" turns\n"
    else:
        demand = random.randint(50,100)*10
        distance = random.randint(10,30)
        resistance_drop = round(random.randint(10,90)/100,2)
        bigger_voltage = random.randint(300,500)*10
        q = "A small town with a demand of "+str(demand)+" kW of electric power at 220 V is situated "+str(distance)+" km away from an electric plant generating power at 440 V. The resistance of each of the two wires carrying power is "+str(resistance_drop)+" ohm per km. The town gets power from the line through "+str(bigger_voltage)+" - 220 V step down transformer at a sub-station in the town. "
        I = (demand*1000)/bigger_voltage
        power_loss = I*I*resistance_drop*distance*2
        if types == 2:
            q = q + "Estimate the power loss in the form of heat?\n"
            a = "{:.2e} watt\n".format(power_loss)
        elif types == 3:
            q = q + "How much power does the plant supply, assuming there is negligible power loss due to leakage?\n"
            a = "{:.2e} watt\n".format(power_loss+demand)
        else:
            q = q + "Characterise the step up transformer at the plant.\n"
            voltage_drop = I*resistance_drop*2*distance
            a = "rating is 440 volt -- "+str(round(bigger_voltage+voltage_drop,2)) + " volt\n"
    qns.write(q)
    ans.write(a)

qns.close()
ans.close()