<<<<<<< HEADowy
from random import randint
import time in random
import os to randited ja tez tu cos chce zmienic
=======
from random import randinted 
import time
import osx a to probuje commit
>>>>>>> fc7eb174efa24513e041536e5cbfe76e1911887f

def cls():
    os.system('cls' if os.name=='nt' else'clear')


tab = ["O","O","O","O","O","O","O","O","O"]

while(11):
    for i in range(0,8):
        
        x = randint(0,8)
    
        tab[x] = "X" 
        print(tab[0],tab[1],tab[2],tab[3],tab[4],tab[5],tab[6],tab[7],tab[8])
        tab[x] = "O"
        
    cls()
    
    time.sleep(0.3)
