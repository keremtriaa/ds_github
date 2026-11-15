# Gestionnaire de Tâches (Application Console Python)

Ce projet consiste en une application Python simple en ligne de commande (console) permettant de gérer des tâches quotidiennes. Il a été réalisé dans le cadre du module **Outils collaboratifs avec Git / GitHub (Licence 1, S1)**.

## Fonctionnalités

L'application repose sur un menu interactif en boucle et propose les fonctionnalités suivantes :

- **1. Ajouter une tâche** : Permet de créer une tâche avec un identifiant unique (`id`), un titre obligatoire (les saisies vides sont refusées), une description facultative, un niveau de priorité (*Basse*, *Moyenne* ou *Haute*) et un statut initial (*En cours*).
- **2. Afficher les tâches** : Liste l'ensemble des tâches enregistrées avec leurs détails complets, ou affiche un message d'information si la liste est vide.
- **3. Rechercher une tâche** : Permet de filtrer et d'afficher les tâches correspondant à un mot-clé saisi par l'utilisateur *(en cours d'implémentation / à compléter dans `main.py`)*.
- **0. Quitter** : Ferme proprement l'application.

## Étapes Réalisées

1. **Conception de la structure des données** : Utilisation d'une liste de dictionnaires pour stocker les propriétés détaillées de chaque tâche (`id`, `titre`, `description`, `priorite`, `statut`).
2. **Développement des fonctions de base** : Création des fonctions modulaires `saisir_entier()`, `ajouter_tache()`, `afficher_taches()`, `afficher_menu()` et `main()`.
3. **Gestion de versions locale (Git)** : Initialisation du dépôt Git et création de commits réguliers documentant l'avancement du code.
4. **Hébergement distant (GitHub)** : Liaison avec un dépôt distant `origin` et publication du code source et de la documentation sur la branche `main`.

## Méthode d'Exécution

Pour lancer le programme depuis **Visual Studio Code** :

1. Ouvrir le dossier contenant le projet dans **VS Code**.
2. Sélectionner et ouvrir le fichier `main.py` dans l'éditeur.
3. Cliquer sur le bouton **« Run Python File »** (icône de lecture ▶️ en haut à droite de la fenêtre) pour exécuter le script dans le terminal intégré.