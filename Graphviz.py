import streamlit as st
import pandas as pd

st.title('Graphviz')

# Creating graph object
st.graphviz_chart('''
                diagraph {
                "Training Data" -> "ML Algorithm"
                "ML Algorithm" -> "Model"
                "Model" -> "Result Forecasting"
                "New Data" -> "Model"
                }
                ''')


import graphviz as graphviz
st.title('Graphviz')
graph = graphviz.Digraph()
graph.edge("Training Data", 'Ml Algorthm')
graph.edge('ML Algorthm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)