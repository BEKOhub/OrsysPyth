#%% Def subscriber
subscribers = {}

def subscribe(event_name):
    """Décorateur pour enregistrer une fonction comme abonné à un événement."""
    def decorator(func):
        if event_name not in subscribers:
            subscribers[event_name] = []
        subscribers[event_name].append(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
#%% Def Notifier
def notify(event_name, *args, **kwargs):
    """Déclenche l'événement et envoie des notifications aux abonnés."""
    if event_name in subscribers:
        for func in subscribers[event_name]:
            func(*args, **kwargs)
    else:
        print(f"Aucun abonné pour l'événement '{event_name}'")

#%% Test d'abonnement
@subscribe("news")
def send_email(user):
    print(f"Envoi d'un email à {user}")

@subscribe("news")
def send_sms(user):
    print(f"Envoi d'un SMS à {user}")

@subscribe("promotion")
def send_promo_email(user):
    print(f"Envoi d'un email promotionnel à {user}")

#%% Notification des abonnés
notify("news", "Hamza")
notify("promotion", "Hamza")
notify("event", "Hamza")  



# %% Métaclass

class MetaAbonnement(type):
    _subscribers = {}

    def __new__(cls, name, bases, attrs):
        #Créer la classe avec la métaclasse
        new_class = super().__new__(cls, name, bases, attrs)

        # Vérifie si la classe a un attribut 'event_name'
        if 'event_name' in attrs:
            cls._subscribers.setdefault(attrs['event_name'], []).append(new_class)

        return new_class

    @classmethod
    def notify(cls, event_name, *args, **kwargs):
        """Notifie tous les abonnés d'un événement."""
        if event_name in cls._subscribers:
            for subscriber in cls._subscribers[event_name]:
                subscriber().update(*args, **kwargs)
        else:
            print(f"Aucun abonné pour l'événement '{event_name}'")

# CLASSES ABONNÉS
# %%
class NewsSubscriber(metaclass=MetaAbonnement):
    event_name = "news"

    def update(self, user):
        print(f"Envoi d'un email à {user} pour les news.")

class PromoSubscriber(metaclass=MetaAbonnement):
    event_name = "promotion"

    def update(self, user):
        print(f"Envoi d'un email promotionnel à {user}.")

# TESTT
# %% Envoi d'une notification aux abonnés
MetaAbonnement.notify("news", "Hamza")
MetaAbonnement.notify("promotion", "Hamza")
MetaAbonnement.notify("event inconnu", "Hamza")


# %%
