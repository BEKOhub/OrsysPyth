#%% Installation et importation des modules


import tensorflow_datasets as tfds

#%% Chargement des données MNIST
# On récupère les données MNIST depuis TensorFlow Datasets
mnist_data = tfds.load("mnist")

#%% Séparation en ensembles d'entraînement et de test
# On divise les données en deux groupes : entraînement et test
mnist_train, mnist_test = mnist_data["train"], mnist_data["test"]

batch_size = 32

# On calcule la taille de chaque ensemble
train_size = mnist_train.cardinality().numpy() * batch_size
test_size = mnist_test.cardinality().numpy() * batch_size

print(f"Taille du jeu d'entraînement : {train_size} échantillons")
print(f"Taille du jeu de test : {test_size} échantillons")
