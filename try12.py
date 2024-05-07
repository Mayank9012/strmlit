import streamlit as st
import streamlit_folium as st_folium

css="""<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">"""
st.markdown(css,unsaf_allow_html=True)
html1="<nav class=\"navbar navbar-expand-lg bg-body-tertiary\"><div class=\"container-fluid\"><a class=\"navbar-brand\" href=\"\\#\">Navbar</a><button class=\"navbar-toggler\" type=\"button\" data-bs-toggle=\"collapse\" data-bs-target=\"\\#navbarSupportedContent\" aria-controls=\"navbarSupportedContent\" aria-expanded=\"false\" aria-label=\"Toggle navigation\"><span class=\"navbar-toggler-icon\"></span></button><div class=\"collapse navbar-collapse\" id=\"navbarSupportedContent\"><ul class=\"navbar-nav me-auto mb-2 mb-lg-0\"><li class=\"nav-item\"><a class=\"nav-link active\" aria-current=\"page\" href=\"\\#\">Home</a></li><li class=\"nav-item\"><a class=\"nav-link\" href=\"\\#\">Link</a></li><li class=\"nav-item dropdown\"><a class=\"nav-link dropdown-toggle\" href=\"\\#\" role=\"button\" data-bs-toggle=\"dropdown\" aria-expanded=\"false\">Dropdown</a><ul class=\"dropdown-menu\"><li><a class=\"dropdown-item\" href=\"\\#\">Action</a></li><li><a class=\"dropdown-item\" href=\"\\#\">Another action</a></li><li><hr class=\"dropdown-divider\"></li><li><a class=\"dropdown-item\" href=\"\\#\">Something else here</a></li></ul></li><li class=\"nav-item\"><a class=\"nav-link disabled\" aria-disabled=\"true\">Disabled</a></li></ul><form class=\"d-flex\" role=\"search\"><input class=\"form-control me-2\" type=\"search\" placeholder=\"Search\" aria-label=\"Search\"><button class=\"btn btn-outline-success\" type=\"submit\">Search</button></form></div></div></nav>"
st.html(html1)



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

 
      
if __name__ == '__main__':
   main()
