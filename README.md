# **Robot-assistant sur rail**

L'objectif de ce projet est de créer un robot assistant mobile sur rail qui peut aider les utilisateurs dans leur travail. Ce robot peut être utilisé comme une troisième main, un support d'outils ou un dispositif de rangement. Son utilisation est très simple : il suffit à l'utilisateur de choisir le poste de travail où il souhaite travailler, et le robot se déplace automatiquement vers le poste sélectionné.


# **Sommaire:**

- [Réalisation](#réalisation)
    - [Programmation](#programmation)
    - [Electronique](#electronique)
    - [Mécanique](#mécanique)
- [Composants](#composants)
- [Notice](#notice)
- [Amélioration](#amélioration)

---

## **Réalisations:**

#### <u>**Programmation:**</u>

- [Poste](/Code/rail.py)


#### <u>**Electronique:**</u>
- [Schéma de câblage](/Electronique/poste.kicad_sch)


#### <u>**Mécanique:**</u>
- [Modélisation projet](/Mod%C3%A9lisation_3D/robot_sur_rail.f3z)

---
## **Composants:**

- [Profilé 20X40](/Datasheet/DS_Profil%C3%A9.pdf) (quantité au choix)
- [Moteur à courant continu](/Datasheet/DS_moteurDC.pdf) (X1)
- [Capteur de proximité inductif](/Datasheet/DS_capteurInductif.pdf) (X1)
- [ESP32-WROOM 32](/Datasheet/DS_ESP32-WROOM32.pdf) (X1)
- [L298N](/Datasheet/DS_L298N.pdf) (X1)
- boutons poussoires (X3)
- [roues pour imprimantes 3D](https://www.amazon.fr/Imprimante-Roulement-Linéaire-Plastique-Roulements/dp/B0BD8XQ4Y4/ref=sr_1_22?keywords=roue+imprimante+3d&qid=1686215897&sr=8-22) (X3)

---
## **Notice:**

- *Montage* <br>
    1. Mettre le [code](/Code/rail.py) sur l'ESP32.
    2. Faire le câblage électrique et l'ajouter dans le compartiment dédié.
    3. Fixer le moteur DC ainsi que le capteur inductif dans les emplacements prévus à ces effets.
    4. Fixer les équerres plates aux profiléx au niveau des postes de travail souhaités. 
    5. Enfiler l'extrémité du rail (profilé) dans le premier support.
    6. Faire coulisser le robot sur le rail.
    7. Enfiler le deuxième support de l'autre côté du rail
       travail.
- *Utilisation*
    1. Appuyer sur le bouton du poste souhaité.

---

## **Améliorations:**

Plusieurs choses peuvent-être envisagées afin d'améliorer le système : <br>
    - Terminer la modélisation 3D afin d'avoir des pièces imprimables et fonctionnelles. <br>
    - Ajouter des pinces croco sur le côté gauche pour permettre au robot de servir de 3e main.
    