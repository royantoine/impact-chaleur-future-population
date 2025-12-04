import streamlit as st

st.set_page_config(page_title="Défi 2 - Territoires et vulnérabilités", layout="wide")

# --- Sidebar équipe (toujours visible) ---
st.sidebar.markdown("## 👥 Équipe Défi 2 : Impact des îlots de chaleur")
st.sidebar.markdown("""
### Notre équipe
- **Pauline Allée** – Data / Climat  
- **Denis Vannier** – Cartographe  
- **Antoine Roy** – Data Scientist  
- **Adrien Salem-Sermanet** – Data Scientist  
- **Marc Le Moing** – Data Scientist  

📍 *Hackathon Météo France 2025*
""")

# --- Onglets ---
tabs = st.tabs(["Visualiser l’augmentation du risque de fortes chaleurs pour les personnes âgées en France entre aujourd’hui et 2050", "Carte interactive"])


# --- Onglet 1 : Contexte scientifique ---
with tabs[0]:
    st.title("🌡️ ClimAtlas Vulnérabilité")

    st.markdown("""
    ## 🎯 Objectif du projet

    Identifier le niveau d'exposition aux **risques climatiques** — vagues de chaleur, nuits tropicales et vagues de nuits tropicales —
    pour les **populations vulnérables**, aux horizons **2030** et **2050** (méthodologie TRACC).

    ---
                
    🔗 [Voir le code source sur GitHub](https://github.com/royantoine/impact-chaleur-future-population)

    ---
                
    ## 1. Contexte : hausse des températures & croissance des populations âgées

    La France connaît déjà une multiplication des épisodes de fortes chaleurs à travers son territoire.  
    Les projections climatiques régionales montrent que cette tendance va s’accentuer d’ici 2030 puis 2050, avec :  

    - Davantage de **jours à plus de 35°C**, dangereux pour la santé  
    - Des **nuits tropicales (>20°C)**, empêchant la récupération physiologique  
    - Des **vagues de chaleur** de plus longue durée  
    - Une intensification du phénomène d’**îlots de chaleur urbains** dans les villes  

    Ces épisodes affectent particulièrement les **personnes vulnérables**, notamment les **personnes âgées**, surtout si elles vivent seules, en milieu urbain dense ou dans des zones précaires.  
    La population française vieillissante fera que la proportion de personnes de 65 ans et plus sera nettement plus élevée en 2050.  
    L’intersection entre population plus âgée et exposition croissante aux chaleurs extrêmes constitue un enjeu majeur de santé publique et d’aménagement du territoire.
    """)
    # --- Affichage de l'image après la section 1---
    st.subheader("1.1 Evolution de la population +65 ans")
    st.image(
        "image_2.webp",  # chemin relatif ou URL
        width=600  # largeur en pixels
    )

    # Ajout de la source en dessous
    st.caption("Source : [INED - Vieillissement de la population](https://www.ined.fr/fr/tout-savoir-population/memos-demo/focus/vieillissement-de-la-population-accelere-en-france-et-dans-la-plupart-des-pays-developpes/)")

    # --- Affichage de l'image après la section 1 ---
    st.subheader("1.2 Vagues de chaleur en France")
    st.image(
        "image_1.webp",  # chemin relatif ou URL
        width=600  # largeur en pixels
    )
    st.caption("Source : [DRIAS - Vagues de chaleur](https://www.drias-climat.fr/accompagnement/sections/417)")

    st.markdown("""
    ## 2. Problématique & proposition de valeur

    ### Problématique
    Comment visualiser rapidement, à **échelle spatiale fine**, l’évolution du risque de fortes chaleurs pour les personnes âgées sur l’ensemble du territoire entre aujourd’hui et 2050 ?

    ### Proposition de valeur de ClimAtlas Vulnérabilités
    Fournir une plateforme simple, interactive et autoportante permettant de croiser **données climatiques** et **données démographiques** pour repérer les territoires — jusqu’à l’échelle des quartiers — où la vulnérabilité thermique des personnes âgées va le plus augmenter.  

    L’outil vise à transmettre en quelques secondes une information précise, actionnable et territorialisée, utile aux **collectivités**, **urbanistes**, **acteurs sanitaires** et **décideurs publics**.
    """)

    # --- 3. La solution ---
    st.markdown("## 3. La solution")

    # --- Affichage de l'image après la section 3 ---
    st.subheader("3.1 Visualisation de la solution")
    st.image(
        "image.webp",  # chemin relatif ou URL
        caption="Schéma illustrant la solution ClimAtlas Vulnérabilités",
        width=600  # largeur en pixels
    )

    # --- Suite de la description ---
    st.markdown("""
    ### 3.2 Description générale
    L’application Streamlit comprend :  

    - Une **carte interactive** permettant :
      - de naviguer dans le territoire à différentes échelles (commune / EPCI / département / région)
      - d’afficher le croisement d’un indicateur représentatif de l’aléa de forte chaleur et de la démographie des populations âgées, aujourd’hui et à l’horizon 2050 (+2.7°C)
    - Une **page de documentation intégrée**, rendant la solution accessible et compréhensible sans expertise préalable  

    ➡️ Application en ligne : [ClimAtlas Vulnérabilités](https://hackaton-mf-defi2-icu-xpkqbvnjcbszzp2yzgavl3.streamlit.app/)

    ### 3.3 Usage des données
    **Données climatiques — Météo-France / CPRCM**  
    - Modèle : CNRM-AROME46t1, 2,5 km de résolution  
    - Forçage : CNRM-ESM2-1, scénario SSP3-7.0  
    - Périodes TRACC :
      - **baseline** : 2015–2034, pivot 2025
      - **+2.7°C** : 2068–2087, pivot 2078  

    **Indicateurs climatiques** :  
    - Pire cas annuel sur 20 ans pour le nombre de jours et nuits consécutifs en vague de chaleur (min > 20°C et max > 35°C)  
    - Autres indicateurs non intégrés faute de temps :  
      - Nombre de nuits tropicales (min > 20°C)  
      - Nombre de jours en vague de nuits tropicales  
      - Nombre de jours avec vagues de chaleur (max > 35°C)  

    **Données démographiques — INSEE** :  
    - Projections 2018–2070 par département  
    - Données carroyées (1 km²) pour la distribution spatiale fine  
    - Variables : population totale, personnes âgées  
    - Possibilité de croisement avec WorldPop / données IRIS envisagée mais non intégrée  

    ### 3.4 Méthode de construction de la solution
    - **Extraction et traitement des données CPRCM**
        - Calcul des indicateurs de fortes chaleurs annuels
        - Agrégation par maximum sur 20 ans
        - Construction d’un dataset consolidé par scénario (actuel et +2.7°C)
    - **Préparation des données démographiques**
    - Récupération des projections INSEE
    - Descente d’échelle (carroyage 1 km²)
    - Récupération de la part des +65 ans aujourd’hui et à 2050
    - **Croisement climat × démographie**
    - Jointure géographique des grilles
    - Calcul d’indicateurs combinés de risque
    - **Création de l’application Streamlit**
    - Affichage d’une carte interactive
    - Comparaison des scénarios
    - Intégration d’une documentation autoportante
    ---

    ## 4. Impact envisagé

    ### 4.1 Ce que permet la solution
    - Repérer les territoires à risque thermique croissant, à **résolution très fine**  
    - Observer l’évolution de l’exposition entre aujourd’hui et 2050 (+2.7°C selon la TRACC) pour les personnes âgées  
    - Identifier les quartiers prioritaires où les **politiques d’adaptation** doivent être renforcées  

    Soutien à :  
    - Urbanisme climatique  
    - Politiques de prévention sanitaire  
    - PCAET  
    - Diagnostics territoriaux (CRTE, politique de la ville)

    ### 4.2 Publics visés et bénéfices
    - **Collectivités locales** : outils d’aide à la décision pour orienter les budgets d’adaptation  
    - **Urbanistes / aménageurs** : localisation des îlots de chaleur à renforcer  
    - **Services de santé publique** : identification des zones où les personnes âgées seront les plus vulnérables  
    - **Chercheurs / analystes** : données homogènes, reproductibles, documentées

    ---

    ## 5. Ressources

    ### 5.1 Livrables
    - **Application Streamlit en ligne** : [ClimAtlas Vulnérabilités](https://hackaton-mf-defi2-icu-xpkqbvnjcbszzp2yzgavl3.streamlit.app/)  
    - **Dépôt GitHub complet** : [impact-chaleur-future-population](https://github.com/royantoine/impact-chaleur-future-population)  
    Contient :
        - Notebooks de calcul des indicateurs climatiques  
        - Code de pré-processing démographique  
        - Application Streamlit  
        - README détaillant la méthodologie
                
    ## 6. Améliorations futures

    ### Intégrer plus de données sur la vulnérabilité des populations :  
    - Intégration de données démographiques plus fines (IRIS, WorldPop)
    - prendre en compte la précarité des ménages, les conditions d’isolement des bâtiments à partir des DPEs etc.
    - Intégrer d'autres tranches de la population (enfants, personnes en situation de handicap, etc.)    
    
    ### Ilôts de chaleur : 
    - Calculer l'évolution du différentiel de température entre centres urbains et zones péri-urbaines/rurales
    
    ### Indicateurs climatiques :
    - intégrer des seuils régionalisés pour tenir compte du contexte local dans la définition des vagues de chaleur
    - ajouter une visualisation pour un niveau de réchauffement +4°C
                            
    """)


# --- Onglet 2 : Carte interactive ---
with tabs[1]:
    #st.header("Carte interactive des indicateurs de chaleur")

    # ⚠️ Warning pour le temps de chargement
    st.warning("⚠️ Le temps de chargement de la carte peut être un peu long en fonction de votre connexion et du filtrage choisi.")


    #st.markdown("### 🔎 Carte dynamique hébergée sur le site de l'équipe")
    #st.markdown("*(Développée via Mapbox )*")

    # ---- Affichage de la carte via IFRAME ----
    st.components.v1.iframe(
        src="https://leplan.studio/wip/test2_hackathon_MF/",
        height=800,
        scrolling=True
    )





