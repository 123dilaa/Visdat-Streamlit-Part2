import streamlit as st

#defining Columns
col1, col2 = st.columns(2)

#interesting Elements in column 1
col1.write("First Column")
col1.image('Foto/bb2.jpg')

# Interesting Elements column 2
col2.write('Second Column')
col2.image('Foto/capybara.jpg')

#▪ Spaced-Out Columns