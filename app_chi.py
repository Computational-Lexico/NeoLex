import streamlit as st
import pandas as pd

# Charger la liste des néologismes depuis le fichier JSON
df = pd.read_json("/Users/lianchen/Desktop/CNRS/Stage-CNRS-ANR/STage5月-9月/实习报告/可视化/neo_chi.json")

st.set_page_config(page_title="Dictionnaire des néologismes", layout="wide")

st.title("Petit dictionnaire des néologismes du chinois moderne")

# Barre de recherche
query = st.text_input(" Entrez un mot à rechercher :")

if query:
    results = df[df["Néologisme"].str.contains(query, case=False, na=False)]
    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(f"### {row['Néologisme']}")
            st.write(f"Pinyin : {row['Pinyin']}")
            st.write(f"Signification : {row['Signification']}")
            st.write(f"Thématique : {row['Thématique']}")
            st.markdown("---")
    else:
        st.warning("Aucun néologisme trouvé.")
else:
    st.dataframe(df, use_container_width=True)
