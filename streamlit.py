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
tabs = st.tabs(["Contexte scientifique", "Carte interactive"])


# --- Onglet 1 : Contexte scientifique ---
with tabs[0]:
    st.title("Impact des îlots de chaleur et du réchauffement climatique sur les populations sensibles")

    st.markdown("""
    ## 🎯 Objectif du projet

    Identifier le niveau d'exposition aux **risques climatiques** — vagues de chaleur, nuits tropicales et vagues de nuits tropicales —
    pour les **populations vulnérables**, aux horizons **2030** et **2050** (méthodologie TRACC).

    ---
                
    🔗 [Voir le code source sur GitHub](https://github.com/royantoine/impact-chaleur-future-population)

    ## 🧠 Problématique

    Le réchauffement climatique augmente la fréquence et l’intensité :

    - des **jours > 35°C**
    - des **nuits tropicales (>20°C)**  
    - des **vagues de chaleur**  
    - des **vagues de nuits tropicales**

    Les populations **âgées**, **précaires** et **isolées** sont les plus vulnérables.

    ---

    ## 🧬 Approche adoptée

    1. Indicateurs climatiques du modèle **CPRCM (CNRM-AROME 2,5 km)**  
    2. Calculs sur 20 ans → **maximum interannuel**
    3. Croisement avec les données **INSEE**  
    4. Projection démographique alignée TRACC  
    5. Visualisation interactive via **Streamlit**

    ---

    ## 🛰️ Données utilisées

    ### 🌡️ Climate – CPRCM (CNRM-AROME46t1)
    | Période | Scénario TRACC | Année pivot | Fenêtre |
    |--------|----------------|-------------|---------|
    | Aujourd’hui | Baseline | 2025 | 2015–2034 |
    | +2°C | TRACC 2030 | 2052 | 2042–2061 |
    | +2.7°C | TRACC 2050 | 2078 | 2068–2087 |

    ---

    ## 📊 Indicateurs retenus

    - **Nuits tropicales annuelles**
    - **Jours en vague de chaleur (min >20°C & max >35°C)**
    - **Jours en vague de nuits tropicales**
    - **Jours en vague de chaleur v0 (max >35°C)**

    ⚠️ Valeurs = **pire cas possible (max annuel)**.

    ---

    ## 🏛️ Usages attendus
    - Identification des **quartiers prioritaires exposés**
    - Appui à la lutte contre les **îlots de chaleur urbains**
    - Aide aux **PCAET**, **CRTE**, diagnostics territoriaux
    """)


# --- Onglet 2 : Carte interactive ---
with tabs[1]:
    st.header("Carte interactive des indicateurs de chaleur")

    st.markdown("### 🔎 Carte dynamique hébergée sur le site de l'équipe")
    st.markdown("*(Développée via Mapbox )*")

    # ---- Affichage de la carte via IFRAME ----
    st.components.v1.iframe(
        src="https://leplan.studio/wip/test2_hackathon_MF/",
        height=800,
        scrolling=True
    )
