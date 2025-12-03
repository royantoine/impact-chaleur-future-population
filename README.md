# Description du project
### Equipe


- Pauline Allée – Data / Economiste ([Observatoire de l'énergie et des GES de Nouvelle-Aquitaine](https://oreges.arec-nouvelleaquitaine.com/))
- Denis Vannier – Cartographe / Data Journaliste ([RésO Villes](https://resovilles.com/))
- Antoine Roy – Data Scientist ([Human Adaptation Insitute](https://adaptation-institute.com/))
- Adrien Salem-Sermanet – Data Scientist ([celest.science](https://www.celest.science/))
- Marc Le Moing – Data Scientist ([Agence d'Urbanisme des Pyrénées Atlantiques](https://www.audap.org/))

### Objectif du projet et problématique résolue
Identifier le niveau d'exposition aux risques climatiques (vagues de chaleurs, nuits tropicales, vagues de nuits tropicales) auxquels seront affectés les populations vulnérables selon leur localisation à horizon 2030 et 2050 (TRACC)

### Approche adoptée
Calcul des risques climatiques sur le dataset issu de la descente d'échelle CPRCM suivant les scénarios de la TRACC (uniquement +2°C et +2.7°C sont disponibles), fusion avec les données de l'Insee pour identifier les populations vulnérables à une échelle fine et projection des évolutions de population sur les mêmes perspectives que la TRACC
Les données seront ensuite exposées sur une plateforme web accessible

### Usages pressentis et bénéfices
Utilisation en politique de ville (par les collectivités locales) pour identifier des quartiers prioritaires qui seront le plus affectés par le réchauffement climatique

# Données socio démo

# Données climatiques 
Données produites par le notebook Climate_data_analysis.ipynb

### Données utilisées

Projection climatique régionale issue du **modèle kilométrique à convection résolue (CPRCM)** CNRM-AROME46t1 à 2,5 km de résolution, forcé par la simulation CNRM-ALADIN64E1 / CNRM-ESM2-1 pour le scénario « SSP37.0 ».

### Périodes étudiées
-	Scenario aujourd’hui : année pivot 2025 (période 2015-2034)
-	Scenario **+2°C** (TRACC 2030) : année pivot 2052 (période 2042-2061)
-	Scenario **+2.7°C** (TRACC 2050) : année pivot 2078 (période 2068-2087)

Le modèle climatique n’atteint pas un réchauffement de +4°C pour la France métropolitaine donc il ne nous permet d’étudier ce scénario.

### Indicateurs

Pour chaque scénario, nous avons calculés des indicateurs annuels pour chaque année comprise dans la période de 20 ans du scénario. Nous avons ensuite choisi de prendre pour chaque coordonnées géographique **la valeur maximum sur ces 20 années**. Cela nous permet d’obtenir pour chaque coordonnée du modèle, les aléas climatiques annuels les plus dangereux qui pourraient arriver pour chaque scénario.

Liste des indicateurs :
-	**Nombre de nuits tropicales annuelles** ('sc_[scenario]_n_tropical_nights_min20') : Nombre total de jour sur l’année avec une température minimale supérieur à 20°C
-	**Nombre annuel de jours de vague de chaleur** ('sc_[scenario]_n_heatwaves_days_min20_max35'): Nombre total de jours se trouvant dans une vague de chaleur dans l’année, une vague de chaleur est défini comme une suite d’au moins 3 jours avec une température minimale supérieure à 20°C et une température maximale de 35°C
-	**Nombre annuel de jours de vagues de nuits tropicales** ('sc_[scenario]_n_heatwaves_days_min20'): Nombre total de jours se trouvant dans une vague de nuits tropicales dans l’année, une vague de nuits tropicales est défini comme une suite d’au moins 3 jours avec une température minimale supérieure à 20°C
-	**Nombre annuel de jours de vague de chaleur v0** ('sc_[scenario]_n_heatwaves_days_max35') : Nombre total de jours se trouvant dans une vague de chaleur dans l’année, une vague de chaleur est défini comme une suite d’au moins 3 jours avec une température maximale de 35°C

Les seuils de 20°C pour la température minimale et 35°C pour la température maximale ont été choisis en accord avec les méthodologie du DRIAS pour décrire le climat futur de la France selon la TRACC ([source](https://www.drias-climat.fr/accompagnement/sections/402)). Ce sont ces seuils qui sont utilisés pour calculer les jours caniculaires et les nuits tropicales.

Météo France définit ces niveaux de risques canicules en se basant à la fois sur la température minimale et la maximale ([source](https://meteofrance.com/comprendre-la-meteo/temperatures/vigilance-canicule)).

### Limites des indicateurs et améliorations potentielles

Une piste d'amélioration pourrait être l'utilisation de seuil régionalisé pour considérer les jours caniculaires et les nuits tropicales selon le contexte local.

### output

Les données sont présentées dans un fichier csv où les lignes représentent les observations pour une coordonnée donnée. En colonne, sont disponibles les 4 indicateurs mentionnés ci-dessus pour chaque scénario (aujourd’hui, +2°C et +2,7°C)
