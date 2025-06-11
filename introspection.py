
#%%
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def saluer(self):
        return f"Bonjour, je m'appelle {self.nom}."

#%% Création d'une instance
personne = Personne("Alice", 30)

#%% Utilisation de l'introspection
print("Attributs et méthodes de l'objet :")
print(dir(personne))  # Liste des attributs et méthodes

print("\nType de l'objet :")
print(type(personne))  # Type de l'objet

print("\nVérification d'un attribut :")
print(hasattr(personne, "nom"))  # Vérifie si l'attribut 'nom' existe

print("\nValeur d'un attribut :")
print(getattr(personne, "nom"))  # Récupère la valeur de l'attribut 'nom'

print("\nDéfinir un nouvel attribut :")
setattr(personne, "profession", "Ingénieure")  # Ajoute un nouvel attribut
print(personne.profession)

# %%
