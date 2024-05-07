import streamlit as st

css = """
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
"""

st.markdown(css, unsafe_allow_html=True)

dark = """
<style>
body {
    background-color: #1e1e1e; /* Dark gray */
    color: #ffffff; /* White text */
}
</style>
"""

light = """
<style>
body {
    background-color: #f0f0f0; /* Light gray */
    color: #000000; /* Black text */
}
</style>
"""

mode = st.sidebar.selectbox(
    "Choose Mode",
    ("Dark", "Light"),
    index=None,
    placeholder="Select",
)

if mode == "Dark":
    st.markdown(dark, unsafe_allow_html=True)
elif mode == "Light":
    st.markdown(light, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'> Streamlit Prac </h1>", unsafe_allow_html=True)
st.write("Details")
Gender = ['Male', 'Female', 'Others']


def main():
    with st.form("Enter details:"):
        name = st.text_input("Enter Name:")
        gen = st.radio("Option:", options=Gender)
        Age = st.slider("Age", 1, 99, value=0, format="%d")
        submit = st.form_submit_button("Submit")

    if submit:
        st.write("Name:", name)
        st.write("Gender:", gen)
        st.write("Group:")
        if Age < 18:
            st.write("K")
        elif 18 <= Age <= 30:
            st.write("A")
        else:
            st.write("O")


if __name__ == '__main__':
    main()
