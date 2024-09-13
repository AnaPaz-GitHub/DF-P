import plotly.express as px
df = px.data.gapminder()

import streamlit as st

st.write(df)

import plotly.express as px
import streamlit as st

df = px.data.gapminder()
paises = df['country'].unique()
pais = st.selectbox(label='Seleccione pais', options=paises)
mask = df['country'] == pais
dff = df[mask]

fig = px.line(data_frame=dff, x='year', y='lifeExp')

st.plotly_chart(fig)








