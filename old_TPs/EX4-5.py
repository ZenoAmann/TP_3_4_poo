import math
from EX3 import*

#Testing time !!!
n1=10
print(f"Somme des {n1} entiers consecutifs :{somme_entiers(n1)}")

n2=6
print(f"factorielle de {n2}: {factorielle(n2)}")

x3=2
n3=8
print(f"On calcule {x3} a la puissance {n3}: {puissance(x3,n3)}")

x4=3
epsilon4 = 0.1
print(f"On approche exp({x4}) a {epsilon4} pres : {exponentielle(x4,epsilon4)}")

epsilon5 = 0.001
print(f"On approche pi a {epsilon5} pres : {pi_manuel(epsilon5)}")

u_0 = 23
print(f"Suite de Syracuse en commencant par u_0={u_0}")
syracuse(u_0)