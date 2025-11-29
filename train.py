
from fastapi import FastAPI
import threading
import time

from instagrapi import Client
import follow_use

import random


app = FastAPI()

def boucle():
    




    cl = Client()


    pwd = "nantoooo1."



    

    compte = ["nant.enaina2","nant.enaina3","nant.enaina06","nant.enaina07","nantoooo1","nant.oooo1","nant.oooo9","nant.oooo10","nant.oooo11","nant.oooo12","nant.oooo13","nant.oooo14",
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
    "nant.oooo6"
    ]


    while True:
        print("debut ....")
        
        with open("history.csv", "r") as f:
            history = f.read()
            nombre_lignes = sum(1 for line in f)
        if nombre_lignes >= 1225: # 1260 si 3 compte ne marche pas 
            break


        followed = False
        compte1 = random.choice(compte)
        compte2 = random.choice(compte)

        while compte1 == compte2:
            compte2 = random.choice(compte)

        follow_pair = f"{compte1}:{compte2}"
        if follow_pair not in history:
            nbr = random.randint(1,5)
            for ii in range(nbr):
                print(compte1 , 'va faire de ',nbr, 'abonment ...' , "num : ", ii)
                print('debut follow ....')
                with open("history.csv", "r") as f:
                    history = f.read()
                follow_use.follow(compte1, pwd, compte2)
                compte2 = random.choice(compte)
                while compte1 == compte2:
                    compte2 = random.choice(compte)
                follow_pair = f"{compte1}:{compte2}"
                
                if follow_pair not in history:
                    with open("history.csv", "a") as f:
                        f.write(follow_pair + "\n")
                    followed = True
                
                print("follow de ", compte1 , "a ", compte2, " ,  .....")
                temp = random.randint(80,160)
                print("fin ",temp, "s .....")
                time.sleep(temp)
        
        temp = random.randint(100,120)
        print("fin ",temp, "s .....")
        time.sleep(temp)

    

@app.on_event("startup")
def start_loop():
    thread = threading.Thread(target=boucle, daemon=True)
    thread.start()

@app.get("/")
def home():
    return {"message": "Bienvenue 🚀"}
