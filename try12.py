import streamlit as st

st.markdown("<h1 style='text-align: center;'> Streamlit Prac </h1>",unsafe_allow_html=True)
st.write("Details")
Gender = ['Male','Female','Others']

def main():
  with st.form("Enter details:"):
    name = st.text_input("Enter Name: ",)
    gen = st.radio("Option:", options=Gender,)
    Age = st.slider("Age",1,99,value=0,format="%d")
    submit = st.form_submit_button("Submit")

  if submit:
    st.write("Name : ",name)
    st.write("Gender : ",gen)
    st.write("Group : ")
    if Age<18:
      st.write("K")
    elif Age>=18 and Age<=30:
      st.write("A")
    else:
      st.write("O")

  html = "<a href="#">Link</a>"
  st.markdown(html,unfollow_allow_html=True)
      
if __name__ == '__main__':
   main()
