# Clothes Detector - Procédure à suivre pour le démarrage

## Tout d'abord, téléchargez le fichier img.zip disponible sur le lien ci-dessous :
*(Archive trop lourde pour Git...)*
https://drive.google.com/file/d/0B7EVK8r0v71pS2YxRE1QTFZzekU/view?usp=sharing
 
## Extraire le fichier, le renommer en 'dataset-retr', le placer dans 'api/media'

Une fois le fichier .zip décompressé, vous pouvez le supprimer !

## Extraire le fichier featureCNN.zip qui se trouve dans 'api/cnn'

Vous trouverez un fichier feature.CNN.h5 <br/>
Une fois le fichier .zip décompressé, vous pouvez le supprimer !

## Init du projet, veuillez lancer la commande :

```
- pip install virtualenv
- virtualenv venv
- venv\Scripts\activate
- pip install -r requirements.txt
```

## Démarrer le serveur, veuillez lancer la commande :

```
cd api

python manage.py runserver 0.0.0.0:8000
```

## Autres informations

Si vous souhaitez relancer l'entraînement de l'IA, déplacez-vous d'abord dans le sous-dossier 'api/cnn' et lancez : ```python create_h5.py```
