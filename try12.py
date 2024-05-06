import streamlit as st

st.write("""
# Streamlit demo
first
""")
option = ['A','B','C','D','']

def main():
  with st.form("Enter details:"):
    st.selectbox("Option:", options=option)
    st.slider("Age",10,99,value=0,format="%d")
    submit = st.form_submit_button("Submit")
if __name__ == '__main__':
   main()
