from json import load
import streamlit as st
import pandas as pd
import numpy as np

st.title('Knesset Tweets')
data = pd.read_csv('tfidf.csv',index_col='faction')
names = data.columns

if 'names' not in st.session_state:
    st.session_state.names = []


filtered = data.filter(items=st.session_state.names)

# selected_terms = st.multiselect(
#     'Select term to measure',
#     data.columns)

def update_terms(_n):
    print(st.session_state.names,_n)
    if _n not in st.session_state.names:
        st.session_state.names.append(_n)
    else:
        st.session_state.names.remove(_n)

for name in names:
    st.sidebar.checkbox(name,on_change=update_terms,args=(name,))

st.bar_chart(data=filtered)
st.write(filtered)
