taches = []
compteur_id = 1


def saisir_entier(prompt):
    while True:
        try:
            valeur = int(input(prompt))
            return valeur
        except:  
            print("Erreur : Veuillez saisir un nombre entier valide.")


def ajouter_tache():
    global compteur_id
    print("\n--- AJOUT D'UNE TÂCHE ---")
    
    titre = input("Titre de la tâche : ").strip()
    while not titre:
        print("Erreur : Le titre ne peut pas être vide.")
        titre = input("Titre de la tâche : ").strip()

    description = input("Description de la tâche : ").strip()

    print("Priorité : 1. Basse | 2. Moyenne | 3. Haute")
    choix_prio = saisir_entier("Choisissez la priorité (1-3) : ")
    priorites = {1: "Basse", 2: "Moyenne", 3: "Haute"}
    priorite = priorites.get(choix_prio, "Moyenne")

    tache = {
        "id": compteur_id,
        "titre": titre,
        "description": description,
        "priorite": priorite,
        "statut": "En cours"
    }

    taches.append(tache)
    compteur_id += 1
    print(f"Succès : Tâche '{titre}' ajoutée (ID : {tache['id']}).")


def afficher_taches():
    print("\n--- LISTE DES TÂCHES ---")
    if not taches:
        print("Aucune tâche à afficher.")
    else:
        for t in taches:
            print(f"ID : {t['id']} | Titre : {t['titre']} | Priorité : {t['priorite']} | Statut : {t['statut']}")
            if t['description']:
                print(f"Description : {t['description']}")
            print("-" * 40)
def afficher_menu():
    print("\n==================================")
    print("      GESTIONNAIRE DE TÂCHES      ")
    print("==================================")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("0. Quitter")
    print("==================================")


def main():
    choix = -1
    
    while choix != 0:
        afficher_menu()
        choix = saisir_entier("Choisissez une option : ")

        if choix == 1:
            ajouter_tache()
        elif choix == 2:
            afficher_taches()
        elif choix == 3:
            rechercher_tache()
        elif choix == 0:
            print("\nAu revoir !")
        else:
            print("Erreur : Option invalide. Veuillez réessayer.")


main()

