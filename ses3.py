import time
import os
import random
from instagrapi import Client

cl = Client()

# Device stable (important)
cl.set_device(cl.generate_device("Samsung Galaxy S10"))

pwd = "nantoooo1."

compte = [
    "nant.enaina2","nant.enaina3","nant.enaina06","nant.enaina07","nantoooo1",
    "nant.oooo1","nant.oooo4","nant.oooo9","nant.oooo10","nant.oooo11",
    "nant.oooo12","nant.oooo13","nant.oooo14","nant.oooo15","nant.oooo16",
    "nant.oooo17","nant.oooo18","nant.oooo19","nant.oooo20",
    "mi.aaaah1","mi.aaaah2","mi.aaaah3","mi.aaaah4","mi.aaaah5",
    "mi.aaaah6","mi.aaaah7","mi.aaaah8","mi.aaaah9","mi.aaaah10",
    "tsanta.aaaa1","tsanta.aaaa2","tsanta.aaaa3","tsanta.aaaa4",
    "tsanta.aaaa5","tsanta.aaaa6","tsanta.aaaa7","tsanta.aaaa8",
    "tsanta.aaaa9","tsanta.aaaa10",
    "nant.oooo4","nant.oooo6"
]

# Sélection aléatoire d'un compte
nom = random.choice(compte)
session_file = f"{nom}.json"

print("Compte sélectionné :", nom)
print("Connexion en cours...")

# 1. Si session existe, essayer de la charger
if os.path.exists(session_file):
    print("➡ Session trouvée :", session_file)
    try:
        cl.load_settings(session_file)
        cl.login(nom, pwd)
        print("✔ Session chargée avec succès")
    except Exception as e:
        print("⚠ Erreur session :", e)
        print("➡ Suppression du fichier JSON corrompu")
        os.remove(session_file)
else:
    print("➡ Aucune session existante")

# 2. Si pas connecté → création nouvelle session
if not cl.user_id:
    try:
        # Anti-ban (429)
        time.sleep(random.randint(5, 15))

        cl.login(nom, pwd)
        cl.dump_settings(session_file)
        print("✔ Nouvelle session créée :", session_file)

    except Exception as e:
        print("❌ Erreur lors du login :", e)
        print("Connexion impossible, Instagram limite ou compte bloqué.")
        exit()

print("✔ Fin de la création des sessions")
