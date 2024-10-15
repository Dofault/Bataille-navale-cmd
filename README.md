# Bataille Navale CMD

## Description
Ce projet est une implémentation en Python du célèbre jeu de **Bataille Navale**. Le joueur place ses bateaux sur une grille, puis tente de couler les bateaux de son adversaire en lançant des missiles sur des coordonnées spécifiques. Le but du jeu est de toucher et de couler tous les bateaux adverses.

## Fonctionnalités
- Création d'un plateau de jeu de 10x10 cases.
- Placement de bateaux avec choix de taille et de disposition (horizontale ou verticale).
- Vérification des collisions et des chevauchements lors du placement des bateaux.
- Attaque d'une position avec retour d'information (touché, coulé, ou manqué).
- Affichage dynamique de l'état du plateau de jeu.
- Détection de fin de partie lorsque tous les bateaux sont coulés.

## Instructions

1. **Création du plateau de jeu** :
   - Le plateau est une grille de 10x10 où les bateaux sont placés.
   
2. **Placement des bateaux** :
   - Les bateaux sont placés en saisissant une coordonnée (par exemple, A01 pour la première case) et en choisissant si le bateau doit être placé horizontalement ou verticalement.
   - La taille du bateau doit être spécifiée.

3. **Attaque** :
   - Pendant la partie, l'utilisateur attaque une position en saisissant une coordonnée (par exemple, A01).
   - Si un bateau est touché, la grille est mise à jour en conséquence.

4. **Fin du jeu** :
   - Le jeu se termine lorsque tous les bateaux ont été coulés.

## Exemple d'utilisation

- L'utilisateur est invité à entrer les coordonnées pour placer ses bateaux.
- Ensuite, il lance des attaques en entrant des coordonnées.


## Installation

1. Clonez le projet ou téléchargez les fichiers.
2. Exécutez le fichier principal Python avec :
   ```bash
   python bataille_navale.py