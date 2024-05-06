import streamlit as st
import mymodel as m

st.write("""
# Streamlit demo
first
""")
st.write(m.run(window=15))
