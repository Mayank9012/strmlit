import streamlit as st

st.title("""Streamlit demo""")
st.write("Details")
option = ['A','B','C','D','']

def main():
  with st.form("Enter details:"):
    st.text_input("Enter Name: ")
    st.selectbox("Option:", options=option)
    st.slider("Age",1,99,value=0,format="%d")
    submit = st.form_submit_button("Submit")

  if submit:
    if (Age<18):
      print("K")
    elif (Age>=18 and Age<30):
      print("A")
    else:
      print("O")
      
if __name__ == '__main__':
   main()
