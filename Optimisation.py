
# %% Importation des modules
import time


#%%
def find_common_elements(list1, list2):

    # Trouver les éléments communs
    common_elements = [element for element in list2 if element in list1]
    return common_elements

#%% common elements
liste1 = range(0,100000)
liste2 = range(900,200000)


start_time1 = time.time()


result = find_common_elements(liste1, liste2)

end_time1 = time.time()

print("Éléments communs :", result)
# %% Temps d'exécution
execution_time1 = end_time1 - start_time1
print(f"Temps d'exécution: {execution_time1:.6f} secondes")

# %% Méthode Sets 

def elements_communs(liste1, liste2):
    set1 = set(liste1)  # Conversion de la première liste en ensemble (O(n))
    set2 = set(liste2)  # Conversion de la deuxième liste en ensemble (O(m))
    return list(set1 & set2)  # Intersection des ensembles (O(min(n, m)))

liste1 = range(0,100000)
liste2 = range(900,200000)

print(elements_communs(liste1, liste2))  # Output: [5, 6, 7]




# %% Début de la mesure du temps
start_time2 = time.time()

#  Calcul d'intersection opération sur les ensembles
intersection = set1 & set2

# Fin de la mesure du temps
end_time2 = time.time()

# %% Affichage des résultats
print(f"Intersection: {intersection}")

# %% Temps d'exécution
execution_time2 = end_time2 - start_time2
print(f"Temps d'exécution: {execution_time2:.6f} secondes")

# %%
