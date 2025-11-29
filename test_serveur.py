from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError
import json

app = FastAPI(title="Instagram Like API", version="1.0.0")

class LikeRequest(BaseModel):
    username: str
    password: str
    post_url: str

class LikeResponse(BaseModel):
    success: bool
    message: str

def like_alternative(cl, post_url):
    """Méthode alternative en cas d'erreur de validation"""
    try:
        # Utiliser l'API bas niveau
        media_pk = cl.media_pk_from_url(post_url)
        
        # Appel direct à l'endpoint API
        cl.private_request(f"media/{media_pk}/like/")
        
        print("✅ Like réussi avec méthode alternative !")
        return True
    except Exception as e:
        print(f"❌ L'alternative a échoué: {e}")
        return False

@app.post("/like", response_model=LikeResponse)
async def like_post(request: LikeRequest):
    print("Début de la fonction like")
    print(f"Username: {request.username}, Post URL: {request.post_url}")
    print("Initialisation du client...")
    
    try:
        print("🔗 Connexion à Instagram...")
        
        # Client avec configuration réduite
        cl = Client()
        
        try: 
            cl.load_settings(f"session_{request.username}.json")
            print("Session loaded")
        except:
            cl.login(request.username, request.password)
            cl.dump_settings(f"session_{request.username}.json")
            print("Session created and saved")

        print("✅ Connecté avec succès")
        
        # Récupérer le media_pk
        print("📱 Récupération des informations du post...")
        media_pk = cl.media_pk_from_url(request.post_url)
        print(f"Media PK: {media_pk}")
        
        # Liker directement avec media_pk (évite la conversion en media_id)
        print("❤️  Tentative de like...")
        result = cl.media_like(media_pk)
        
        print("✅ Publication likée avec succès !")
        return LikeResponse(success=True, message="Publication likée avec succès !")
        
    except LoginRequired:
        error_msg = "❌ Erreur de connexion - vérifiez vos identifiants"
        print(error_msg)
        return LikeResponse(success=False, message=error_msg)
    except ClientError as e:
        error_msg = f"❌ Erreur Instagram: {e}"
        print(error_msg)
        return LikeResponse(success=False, message=error_msg)
    except Exception as e:
        error_msg = f"⚠️  Erreur technique: {e}"
        print(error_msg)
        print("Tentative avec une approche alternative...")
        
        # Tenter la méthode alternative
        success = like_alternative(cl, request.post_url)
        if success:
            return LikeResponse(success=True, message="Like réussi avec méthode alternative !")
        else:
            return LikeResponse(success=False, message=f"Échec du like: {error_msg}")

@app.get("/")
async def root():
    return {"message": "Instagram Like API - Utilisez POST /like pour liker une publication"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)