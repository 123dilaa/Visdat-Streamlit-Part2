# 2. Line
import streamlit as st
import pandas as pd
import numpy as np
st.title("Area")

# Defening dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=(["C1", "C2", "C3", "C4"])
)
#Bar chart
st.line_chart(df)