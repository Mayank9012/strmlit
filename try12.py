import streamlit as st

st.title("""Streamlit demo""")
st.write("Details")
option = ['A','B','C','D','']

def main():
  with st.form("Enter details:"):
    name = st.text_input("Enter Name: ",label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,)
    st.selectbox("Option:", options=option)
    Age = st.slider("Age",1,99,value=0,format="%d")
    submit = st.form_submit_button("Submit")

  if submit:
    st.write("Name : ",name)
    st.write("Group : ")
    if Age<18:
      st.write("K")
    elif Age>=18 and Age<=30:
      st.write("A")
    else:
      st.write("O")
      
if __name__ == '__main__':
   main()
