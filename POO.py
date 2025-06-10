#%% @Property
#En Python, les propriétés permettent de contrôler l'accès aux attributs d'un objet.

class Personne:
    def __init__(self, nom):
        self._nom = nom  # Attribut privé

    @property
    def nom(self):
        """Getter pour nom."""
        return self._nom

    @nom.setter
    def nom(self, nouveau_nom):
        """Setter pour nom."""
        if isinstance(nouveau_nom, str):
            
            self._nom = nouveau_nom
        else:
            raise ValueError("Le nom doit être une chaîne de caractères.")

#%% Test @Property
p = Personne("Hamza")
print(p.nom)  # Affiche "Hamza"
p.nom = "Ali"  # Modification du nom
print(p.nom)  # Affiche "Ali"
p.nom = "Hamza"
print(p.nom)

#%% Itérateurs
#Les itérateurs permettent de parcourir les objets de manière séquentielle.
class Compteur:
    def __init__(self, limite):
        self.limite = limite
        self.actuel = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actuel < self.limite:
            self.actuel += 1
            return self.actuel
        else:
            raise StopIteration
#%% Test Itérateurs
compteur = Compteur(5)
for nombre in compteur:
    print(nombre)  # Affiche 1 à 5


# %% Héritage multiple
#Un concept puissant mais complexe qui peut causer des conflits (diamond problem).

class A:
    def dire_bonjour(self):
        return "Bonjour de A"

class B:
    def dire_bonjour(self):
        return "Bonjour de B"

class C(A, B):  # Héritage multiple
    pass

c = C()
print(c.dire_bonjour())  # Résout selon l'ordre MRO (Method Resolution Order)


#%% Context Managers (with)
#Ils permettent de gérer des ressources comme des fichiers.

class Fichier:
    def __init__(self, nom):
        self.nom = nom

    def __enter__(self):
        self.fichier = open(self.nom, "w")
        return self.fichier

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fichier.close()

with Fichier("test.txt") as f:
    f.write("Hello, World!")


#%%  Classes et méthodes abstraites (ABC)
#Utile pour définir des interfaces.

from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def aire(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3.14 * self.rayon ** 2

c = Cercle(5)
print(c.aire())  # Affiche l'aire du cercle


#%% Métaclasses
#Les métaclasses permettent de modifier le comportement des classes au moment de leur création.
class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['nouvel_attribut'] = 'Ajouté par la métaclasse'
        return super().__new__(cls, name, bases, attrs)

class MaClasse(metaclass=Meta):
    pass

print(MaClasse.nouvel_attribut)  # "Ajouté par la métaclasse"
