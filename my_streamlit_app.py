import streamlit as st
import pandas as pd
import seaborn as sns

st.title('Hello Wilders, welcome to my application!')

st.write("I enjoy to discover streamlit possibilities")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"
df_weather = pd.read_csv(link)
df_weather


st.line_chart(df_weather['MAX_TEMPERATURE_C'])


numeric_columns = df_weather.select_dtypes(include=['float64', 'int64'])

# Créer la heatmap de la corrélation
viz_correlation = sns.heatmap(numeric_columns.corr(), center=0, cmap="vlag")

# Afficher la heatmap à l'aide de Streamlit
st.pyplot(viz_correlation.figure)



name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")