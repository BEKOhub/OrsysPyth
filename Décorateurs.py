
#%% define decorator
def mon_decorateur(fonction):
    def wrapper(*args, **kwargs):
        print("Avant l'exécution de la fonction.")
        resultat = fonction(*args, **kwargs)
        print("Après l'exécution de la fonction.")
        return resultat
    return wrapper

#%% apply decorator
@mon_decorateur
def dire_bonjour(arg):
    print("Bonjour!")

dire_bonjour("Hello")

# %%
