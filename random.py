from random import shuffle
from datetime import datetime
dev = ['Alesis', 'Mario', 'Daniel', '']
it = ['Fabian', '']
sop = ['Eva', 'Cesar']
qac = ['Jazmin', 'Martin']
apoyo = ['Fernanda', 'Diego S']
print "HOY: "+datetime.strftime(datetime.now(), '%d-%m')
print "~ ~ Almuerzo ~ ~"
print "12.30:"
shuffle(dev)
shuffle(it)
shuffle(sop)
shuffle(qac)
shuffle(apoyo)
print ', '.join(dev[-4:2]  + it[:-1] + sop[:-1] + qac[:-1]  + apoyo[:-1])
print "13.10:"
print ', '.join(dev[-2:]  + it[1:] + sop[1:] + qac[1:]  + apoyo[1:])
