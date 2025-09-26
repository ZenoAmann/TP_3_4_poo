from math import exp, pi

def est_positif(nombre):
    if nombre < 0:
        return False
    else : 
        return True
    
def affichage_signe(nombre):
    if nombre == 0 :
        print("Nul")
    elif nombre < 0:
        print("Négatif")
    else:
        print("Positif")
    return None

def est_bissextile(nombre):
    if nombre%400 == 0:
        return True 
    elif (nombre%4==0) and (nombre%100!=0):
        return True
    else:
        return False 
    
def somme_entiers(n):
    p,res=0,0
    while p<=n:
        res+=p
        p+=1
    return res

def factorielle(n):
    p,res=1,1
    while p<=n:
        res*=p
        p+=1
    return res

def puissance(x,n):
    p,res=1,1
    while p<=n:
        res*=x
        p+=1
    return res

def exponentielle(x,epsilon):
    n,res=0,0
    while abs(exp(x)-res)>epsilon:
        res += puissance(x,n)/factorielle(n)
        n +=1
    return res 

def pi_manuel(epsilon):
    n,res=0,0
    while abs(pi-res)>epsilon:
        res += 4*((puissance(-1,n))/(2*n+1))
        n+=1
    return res 

def syracuse(u_0):
    i=0
    if (u_0>=1)and(type(u_0)==int):
        while u_0!=1:
            if u_0%2==0:
                u_1=u_0//2
            else :
                u_1=(3*u_0)+1 
            u_0=u_1
            i+=1
            print(f"u_{i}={u_0}")
    else :
        print("u_0 a ete mal defini")
    print(f"Convergence apres {i} iterations")
    return None