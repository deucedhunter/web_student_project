import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

DUMMY_TEXT = """Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm. Pinnace holystone mizzenmast quarter crow's nest nipperkin grog yardarm hempen halter furl. Swab barque interloper chantey doubloon starboard grog black jack gangway rutters."""

st.header("The Best Company")
st.write(DUMMY_TEXT)
st.subheader("Our Team")

df = pd.read_csv("data.csv", sep=",")

col1, col2, col3 = st.columns(3)

with col1:
    for idx, row in df.iterrows():
        if idx % 3 == 0:
            st.subheader(f"{row["first name"]} {row["last name"]}")
            st.write(row["role"])
            st.image(f"images/{row["image"]}")
with col2:
    for idx, row in df.iterrows():
        if idx % 3 == 1:
            st.subheader(f"{row["first name"]} {row["last name"]}")
            st.write(row["role"])
            st.image(f"images/{row["image"]}")
with col3:
    for idx, row in df.iterrows():
        if idx % 3 == 2:
            st.subheader(f"{row["first name"]} {row["last name"]}")
            st.write(row["role"])
            st.image(f"images/{row["image"]}")