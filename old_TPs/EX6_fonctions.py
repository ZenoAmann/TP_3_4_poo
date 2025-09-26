
def echange_positions(t,i,j):
    t[i],t[j]=t[j],t[i]
    return t

def position_plus_petite(t,p):
    if not t or p < 0 or p >= len(t): #test de validité de l'indice p
        raise ValueError("Indice p invalide ou liste vide")
    smallest=p
    for i in range((p+1),(len(t))):
        if t[i]<t[smallest]:
            smallest = i
    return smallest

def tri_par_selection(t):
    for i in range(0,len(t)-1):
        echange_positions(t,i,position_plus_petite(t,i))
    return t

def bubblesort(t):
    for j in range(len(t)-1):
        travailTermine = True
        for i in range(len(t)-1-j):
            if t[i+1]<t[i]:
                echange_positions(t,i,i+1)
                travailTermine=False
        if travailTermine:
            break
    return t