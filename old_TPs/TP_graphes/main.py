from utils import* 
from graph import*

dico1={
    "A":["B"],
    "B":[],
    "C":["A","B"],
    "D":["C"],
    "E":["C","D"],
}

ajouter_noeud(dico1, "F")
ajouter_arete(dico1,"F","A")
ajouter_arete(dico1,"F","C")

display_graph_from_dict(dico1)

print("Test de : parcours_en_profondeur")
parcours_en_profondeur(dico1,"F")

print("Test de : parcours_en_largeur")
parcours_en_largeur(dico1,"F")