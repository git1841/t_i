
import time
from instagrapi import Client

cl = Client()


nom = "nant.enaina1"
pwd = "nantoooo1."



compte = ["nant.enaina2","nant.enaina3","nant.enaina06","nant.enaina07","nantoooo1","nant.oooo1","nant.oooo4","nant.oooo9","nant.oooo10","nant.oooo11","nant.oooo12","nant.oooo13","nant.oooo14",
"nant.oooo15",
"nant.oooo16",
"nant.oooo17",
"nant.oooo18",
"nant.oooo19",
"nant.oooo20",
"mi.aaaah1",
"mi.aaaah2",
"mi.aaaah3",
"mi.aaaah4",
"mi.aaaah5",
"mi.aaaah6",
"mi.aaaah7",
"mi.aaaah8",
"mi.aaaah9",
"mi.aaaah10",
"tsanta.aaaa1",
"tsanta.aaaa2",
"tsanta.aaaa3",
"tsanta.aaaa4",
"tsanta.aaaa5",
"tsanta.aaaa6",
"tsanta.aaaa7",
"tsanta.aaaa8",
"tsanta.aaaa9",
"tsanta.aaaa10",
"nant.oooo4",
"nant.oooo6"
]

import random
i = random.randint(0, len(compte)-1)

# nom = compte[i]
# print("Compte sélectionné :", nom)
# print("Connexion en cours...")



j = random.randint(0,len(compte)-1)
nom = compte[j]
print("Compte sélectionné :", nom)
print("Connexion en cours...")
try : 
    cl.load_settings(f"session_{nom}.json")
    print("Session loaded")
except :
    cl.login(nom, pwd)
    cl.dump_settings(f"session_{nom}.json")
    print(f"session_{nom}.json")

print("Fin de la création des sessions")



