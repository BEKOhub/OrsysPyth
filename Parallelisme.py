#%% 
from multiprocessing import Pool

def carre(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as p:  # 4 processus parallèles
        result = p.map(carre, range(10))
    print(result)  # Affiche les carrés des nombres de 0 à 9

# %%
