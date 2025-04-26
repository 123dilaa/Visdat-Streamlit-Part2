# Visualisasi


# 1. Bar

import streamlit as st
import pandas as pd
import numpy as np

st.write("Kelompok 3")
st.write("Dila")
st.write("Wulan")
st.write("Zahra 3")

st.title('Area')


# Defininf dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=(["C1", "C2", "C3", "C4"])
)
#Bar chart
st.bar_chart(df)

# 2. Line
st.title("Area")

# Defening dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=(["C1", "C2", "C3", "C4"])
)
#Bar chart
st.line_chart(df)

# 3. Area
st.title('Area')

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=(["C1", "C2", "C3", "C4"])
)
#Bar chart
st.area_chart(df)

# Map
