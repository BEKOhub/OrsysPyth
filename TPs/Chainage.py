#%% Décorateurs :
def add_prefix(prefix):
    """Ajoute un préfixe au texte."""
    def decorator(func):
        def wrapper(text):
            return prefix + func(text)
        return wrapper
    return decorator

def uppercase(func):
    """Met le texte en majuscules."""
    def wrapper(text):
        return func(text).upper()
    return wrapper

def replace_spaces(replacement):
    """Remplace les espaces par un autre caractère."""
    def decorator(func):
        def wrapper(text):
            return func(text).replace(" ", replacement)
        return wrapper
    return decorator
#%% Test :
@add_prefix("Message: ")
@uppercase
@replace_spaces("-")
def process_text(text):
    return text

# Simulation d'un flux de données
data_stream = ["Bonjour monde", "Test décorateurs", "Python est puissant"]

# Traitement du flux avec les décorateurs
processed_stream = [process_text(data) for data in data_stream]

# Affichage des résultats
for result in processed_stream:
    print(result)

# %%
