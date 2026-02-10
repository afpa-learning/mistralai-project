# openai-project
Projet réalisé en Python permettant d'interroger Mistral AI

## Installation

- Vérifier que Python est bien installé

```bash
py --version
```
- Installer les dépendances

```bash
pip install python-dotenv requests mistralai
```
- Activer le virtual environment (venv)

```bash
py -m venv venv
.\venv\Scripts\activate 
```
- Mettre une clé API dans le fichier .env

- Créer le répertoire outputs à la racine du projet

- Créer un fichier .env à la racine du projet avec comme contenu :

```bash
MISTRAL_API_KEY=!!YOUR-API-KEY!!
```

## Samples

- Sample : Simple interrogation de Mistral AI
- Sample 1 : Demande de génération de code
- Sample 2 : Demande de génération de code avec une image de rendu

>[!WARNING] 
> Attention au quota d'utilisation des API 

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/afpa-learning/mistralai-project">mistralai-project</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/afpa-learning">Afpa</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>
