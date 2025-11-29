from instagrapi import Client
from instagrapi.exceptions import ClientError

def follow(username, password, target_username):
    print("Début de la fonction follow")
    print(username, password, target_username)
    print("Initialisation du client...")
    #input("Appuyez sur Entrée pour continuer...") user_id
    
    """Version qui évite l'erreur extract_user_gql  user_id_from_username_v1"""
    try:
        print("🔗 Connexion en cours...")
        
        # Connexion
        client = Client()
        
        try : 
            client.load_settings(f"session_{username}.json")
            print("Session loaded")
        except :
            client.login(username, password)
            client.dump_settings(f"session_{username}.json")
            print("Session created and saved")
        
        # Username cible
        print(f"👤 Recherche du compte: {target_username}")
        
        try:
            # Méthode alternative pour récupérer l'ID user_id_from_username extract_user_gql
            user_id = client.user_id_from_username(target_username)
            print(f"📱 ID trouvé: {user_id}")
        except Exception as e:
            print(f"------------------------------------------⚠️  Erreur lors de la recherche, tentative alternative...  ----------------- ")
            # Méthode de secours
            user_id = client.user_id_from_username(target_username)
            print(f"📱 ID trouvé (méthode alternative): {user_id}")
        
        # Follow
        print("➕ Envoi de la demande de follow...")
        result = client.user_follow(user_id)
        
        print(f" ----------------- 🎉 Félicitations ! Vous suivez maintenant {target_username} ! -----------------")
        return True
        
    except Exception as e:
        print(f" ----------------- ❌ Erreur: {e} -----------------")
        return False

# Lancer le follow
if __name__ == "__main__":
    username = "nant.enaina1"
    password = "nantoooo1."
    target_username = "tojonirina_photography"
    follow(username, password, target_username)
    
