import os
import json
import hashlib


print("---------------")

def hash_file(path):
    """Retourne un hash unique du contenu du fichier."""
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def remove_duplicate_json():
    json_files = [f for f in os.listdir(".") if f.endswith(".json")]

    if not json_files:
        print("Aucun fichier JSON trouvé.")
        return

    seen = {}  # hash → filename
    duplicates = []

    for file in json_files:
        file_hash = hash_file(file)

        if file_hash in seen:
            print(f"[DUPLICATE] {file} == {seen[file_hash]}")
            duplicates.append(file)
        else:
            seen[file_hash] = file

    # supprimer tous les doublons
    for file in duplicates:
        os.remove(file)
        print(f"[DELETED] {file} supprimé")

    print("\nTerminé !")
    print(f"Fichiers uniques gardés : {list(seen.values())}")


remove_duplicate_json()
