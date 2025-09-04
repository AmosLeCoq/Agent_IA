# IA

[https://github.com/AmosLeCoq/Agent_IA](https://github.com/AmosLeCoq/Agent_IA)

https://pypi.org/project/openpyxl/

https://pypi.org/project/PyMuPDF/

[https://github.com/ollama/ollama-python](https://github.com/ollama/ollama-python)

<aside>
💡

model mistral:latest

</aside>

<aside>
⚠️

- [x]  Regex pour les dates
- [x]  Résumé → excel
- [x]  Suppression si v2 déjà existent
- [x]  Regex date page 1 et 2
- [x]  Github
</aside>

# Objectif

<aside>
💡

Trouver la date du document via IA

Un nouveau nom correct 

</aside>

<aside>
💡

Créer un agent IA :

Cet agent devra analyser des fichiers PDF, dans un dossier afin de les mettre dans l’ordre chronologique et de les renommer avec une nomenclature que l’utilisateur aura choisie et faire un petit récapitulatif.

Etapes

1. Constituer un jeu de données (exemple : des PV d’un conseil communal), trouver des pdf de différentes structures (pdf de mails rapport, pv, etc.), mais parlant généralement du même thème. Environs 30 documents
2. Trouver un framework pour la lecture des PDF qui puisse répondre à la suite du cahier des charges
3. Proposer et tester un modèle IA (compatible Ollama) capable de dater l’ensemble des documents
4. Proposer et tester un modèle IA (compatible Ollama) pour résumé le document en 3 lignes
5. Créer un script (si possible Python) qui pour lequel je spécifie le dossier ainsi que la nomenclature et je retrouve un dossier dans le dossier spécifié qui a les fichiers classés par ordre chronologique et renommé et un fichier Excel avec le résumé du contenu du fichier ainsi qu’un lien dessus pour l’ouvrir
6. Nice to have : sur la base du script, proposer un addon à Open Web UI qui puisse réaliser ceci dans l’interface d’OpenWeb UI

# Restrictions actuelles

PDF

Pas scanne

# Attention

## Problème lié au prompt

ex: 

```
    dateAPI = (
        "Extrait du PV ou mail :\n\n" +
        text +
        "\n\nDonne moi la date de la séance de ce pv ou mail"
        "Réponds uniquement avec la date au format YYYY-MM-DD." 
    )
```

Donne une date même si il n’y a pas de date

Solution, mais à vérifier 

```bash
    dateAPI = (
        "Extrait du PV ou mail :\n\n" +
        text +
        "\n\nDonne moi la date de la séance de ce pv ou mail"
        "Réponds uniquement avec la date au format YYYY-MM-DD."
        "Si tu ne trouves pas de date tu réponds uniquement /Erreur/" 
    )
```

<img width="1083" height="914" alt="image" src="https://github.com/user-attachments/assets/292cd8da-5259-411d-993a-df30eef7b427" />
