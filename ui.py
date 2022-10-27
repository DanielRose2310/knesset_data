from json import load
import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
   page_title="Knesset Tweets",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)
data = pd.read_csv('tfidf.csv',index_col='faction')
names = data.columns

if 'names' not in st.session_state:
    st.session_state.names = []

if 'filter' not in st.session_state:
    st.session_state.filter = ''


filtered = data.filter(items=st.session_state.names)

# selected_terms = st.multiselect(
#     'Select term to measure',
#     data.columns)
st.session_state.filter = st.sidebar.text_input('Label to filter')

def update_terms(_n):
    if _n not in st.session_state.names:
        st.session_state.names.append(_n)
    else:
        st.session_state.names.remove(_n)

for name in names:
    if not len(st.session_state.filter) or name in st.session_state.filter:
        st.sidebar.checkbox(name, value=name in st.session_state.names,on_change=update_terms,args=(name,))

st.bar_chart(data=filtered)
st.table(filtered)
