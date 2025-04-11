import streamlit as st
import json
import pandas as pd

st.title("🚮 Abandoned Waste Detection Log Viewer")

with open("runs/results/log.json", "r") as f:
    raw = f.read().strip().rstrip(',\n') + '\n]'
    data = json.loads(raw)

df = pd.DataFrame(data)
st.dataframe(df)

chart = df["label"].value_counts()
st.bar_chart(chart)
