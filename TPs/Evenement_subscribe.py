#%%décorateurs listners
event_listeners = {}

def event_listener(event_name):
    """Décorateur pour enregistrer une fonction comme gestionnaire d'événements."""
    def decorator(func):
        event_listeners[event_name] = func
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

def trigger_event(event_name, *args, **kwargs):
    """Déclenche un événement en appelant le gestionnaire associé."""
    if event_name in event_listeners:
        return event_listeners[event_name](*args, **kwargs)
    else:
        print(f"Aucun gestionnaire pour l'événement '{event_name}'")
#%% Test
@event_listener("login")
def on_login(username):
    print(f"Bienvenue, {username} !")

@event_listener("logout")
def on_logout(username):
    print(f"A bientôt, {username} !")

@event_listener("signup")
def on_signup(username):
    print(f"Bienvenue ! signup in 1 seconds ;) !, {username} !")
#%% Déclencher les événements
trigger_event("login", "Hamza")
trigger_event("logout", "Hamza")
trigger_event("signup", "Hamza")
trigger_event("subscribe","Hamza")
