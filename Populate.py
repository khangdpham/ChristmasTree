import random
ff = open("Wizards.bt",'w')

x= 0
size = (30*60+8)*5
for y in range(size):
 ff.write(str(x)+","+str(random.randint(1,254)))
 ff.write("\n")
 x+=0.1

ff.close()
