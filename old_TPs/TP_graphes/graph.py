def ajouter_noeud(graphe,noeud:str):
    if noeud not in graphe :
        graphe[noeud]=[]
    elif noeud in graphe:
        print("Un autre noeud porte deja ce nom !")
    return None

def ajouter_arete(graphe, depart:str, arrivee:str):
    if depart in graphe and arrivee in graphe:
        if arrivee not in graphe[depart]: 
            graphe[depart]+=[arrivee]
        else:
            print("L'arete existe deja !")
    else :
        print("L'un des noeuds spécifiés n'extiste pas !")
    return None

def parcours_en_profondeur(g:dict, depart:str):
    a_explorer = list(g[depart])
    deja_visites = []
    cpt = len(a_explorer)-1
    while a_explorer !=[]:
        noeud =  a_explorer.pop(cpt)
        cpt-=1
        if noeud not in deja_visites:
            deja_visites.append(noeud)
            print(f"j'ai visite : {noeud}")
            for n in g[noeud]:
                if n not in a_explorer and n not in deja_visites:
                    a_explorer.append(n)
                    print(f"nouveau noeud a explorer trouve :{n}")
            cpt=len(a_explorer)-1
    return None     

def parcours_en_largeur(g:dict, depart:str):
    a_explorer = list(g[depart])
    deja_visites = []
    cpt = 0
    while a_explorer !=[]:
        noeud =  a_explorer.pop(cpt)
        cpt+=1
        if noeud not in deja_visites:
            deja_visites.append(noeud)
            print(f"j'ai visite : {noeud}")
            for n in g[noeud]:
                if n not in a_explorer and n not in deja_visites:
                    a_explorer.append(n)
                    print(f"nouveau noeud a explorer trouve :{n}")
            cpt=0
    return None 
"""blablabla
signé : anto"""