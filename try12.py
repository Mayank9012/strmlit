import streamlit as st
import re

def validate_email(email):
    # Regular expression for basic email validation
    pattern = r'^\S+@\S+\.\S+$'
    if re.match(pattern, email):
        return True
    else:
        return False
             

@st.experimental_dialog("Confirmation")
def pop():
    st.success("Your query is submitted successfully")
    st.write(f"Your Job-ID is AAAAAAA")
    st.link_button("Check Status","http://localhost:8502")
                

# Define the navigation bar HTML
navbar1 = """
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 10px;
    }
    .navigation {
        background-color: #ad3838;
        overflow: hidden;
        width: 100%;
        display: flex;
        margin: 0 auto; /* Center the navigation bar horizontally */
        position: relative; /* Fixed position at the top of the viewport */
        top: 38px; /* Distance from the top of the viewport */
        left: 50%; /* Center the navigation bar horizontally */
        transform: translateX(-50%); /* Center the navigation bar horizontally */
        z-index:1000;
    }

    .nav-list {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    .nav-item {
        float: left;
    }

    .nav-link {
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }

    .nav-link:hover {
        background-color: #57998b;
    }

    .dropdown {
        position: relative;
        display: flexbox;
    }

    .dropdown-content {
        display: none;
        position: fixed;
        top: 40px; /* adjust the top position */
        left: 50%; /* adjust the left position */
        transform: translateX(-50%); /* center the dropdown horizontally */
        background-color: #f9f9f9;
        width: 160px;
        box-shadow: 0px 8px 16px 0px rgba(15, 14, 14, 0.2);
        z-index: 1;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
    }
    .dropdown-item {
        color: rgb(241, 231, 231);
        text-align: left;
        padding: 8px 12px; /* Adjust padding */
        text-decoration: none;
        display: block;
    }

    .dropdown-item:hover {
        background-color:#57998b;
    }

    .dropdown.active .dropdown-content {
        display: block; 
    }

    .dropdown .dropbtn {
        outline: none;
    }

    .dropdown-content.active {
        display: contents;
    }

    </style>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
        const dropdownBtn = document.querySelector('.dropdown .dropbtn');
        const dropdownContent = document.querySelector('.dropdown-content');

        dropdownBtn.addEventListener('click', () => {
            dropdownContent.classList.toggle('active');
        });

        document.addEventListener('click', (event) => {
            if (!event.target.closest('.dropdown')) {
                dropdownContent.classList.remove('active');
            }
        });
    });
    </script>


    <nav class="navigation">
    <ul class="nav-list">
        <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
        <li class="nav-item"><a href="#" class="nav-link">About</a></li>
        <li class="nav-item dropdown">
        <a href="javascript:void(0)" class="nav-link dropbtn">Help</a>
        <div class="dropdown-content">
            <a href="#" class="dropdown-item">User Guide</a>
            <a href="#" class="dropdown-item">FAQ</a>
            <a href="#" class="dropdown-item">Contact</a>
        </div>
        </li>
    </ul>
    </nav>
"""
def render_navbar():
  navbar = """
  <style>
    body {
      margin: 0;
      padding: 0;
      font-family: Arial, sans-serif;
      color: white;
    }
    .navigation {
      background-color: #b6e9d9;
      overflow: hidden;
      display: inline;
      justify-content: flex-start;
      align-items: right;
      padding: 10px 20px;
      top : -40px;
      position: absolute;
      width: 100%; /* Adjusted width */
      z-index: 1000;
      color: white !important; /* Added !important */
    }

    .nav-list {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      color: white !important; /* Added !important */
    }

    .nav-item {
      float: left;
      margin-right: 20px;
      color: white !important; /* Added !important */
    }

    .nav-link {
      display: block;
      text-align: center;
      text-decoration: none;
    }

    .nav-link:hover {
      background-color: #57998b;
      border-radius: 5px;
      color:white;
    }

  </style>
   
  <nav class="navigation">
    <ul class="nav-list">
      <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
      <li class="nav-item"><a href="#" class="nav-link">About</a></li>
      <li class="nav-item"><a href="#" class="nav-link">Help</a></li>
    </ul>
  </nav>
  """
  st.markdown(navbar, unsafe_allow_html=True)

st.markdown(navbar1,unsafe_allow_html=True)
# Main function
def main():
    st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #0f4233;
        }
    </style>
    """, unsafe_allow_html=True)
    # Sidebar content
    with st.sidebar:
 
		# Define CSS styles for the progress bars
        st.markdown(
			"""
			<style>
			.stProgress {
				display: flex;
				justify-content: center; /* Center horizontally */
				align-items: center; /* Center vertically */
				height: 150px; /* Adjust height as needed */
                transform: translateX(-50%) translateY(50%);
			}

			.stProgress > div {
				display: flex;
				justify-content: space-between; /* Spread the progress circles evenly */
				align-items: center; /* Center vertically */
				width: 450px; /* Adjust width of the progress bar */
			}

			.stProgress > div > div {
				width: 1450px; /* Adjust width of each progress circle */
                transform: translateX(-165px) translateY(185px);

			}

			.stProgress > div > div > div  {
				background-color: #cac1c3;
				transform: rotate(90deg);
				justify-content: center;     
                
			}
            .stProgress > div > div > div > div {
                background-color: #c2f7e7;
            }
            .stStepCircle {
                background-color:#299776;
                width: 20px;
                height: 20px;
                border-radius: 50%;
                border: 4px solid #fff; /* Add white border */
                display:flex;
                margin-bottom:74px;
                transform: translateX(250%) translatey(-300%);
                justify-content: left;
                align-items: left;
                color: white;
                font-weight: bold;}
			""",
			unsafe_allow_html=True,)
        steps = ["Submit_query", "OGRI", "16S_Tree", "WGS_Tree","Summary"]
        progress = st.progress(0)
        # Display progress bar with step circles
        with st.container():
            for i, step in enumerate(steps):
                st.markdown(f'<div class="stStepCircle">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{step}</div>', unsafe_allow_html=True)
                if i < len(steps) - 1:
                    st.write("")
                else:
                    st.write(f"")

        st.markdown("""
            <style>
                    [data-testid=stContainer] {
                        outline: 2px solid red;
                        border-radius: 2px;
                    }
                    .stContainer {
                        background-color: grey; 
                        margin-left: 250px; /* Adjusted margin */
                    }
            </style>
        """, unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown(
            """
            <style>
            .stContainer {
                background-color: grey; 
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(""" <style>
            .heading{
                margin: 0px; 
                position: auto; 
                top: 0px; 
                left: 15%; 
                z-index: 1;
                font-family: Georgia;
            }
            hr {
                display: flex;
                border: none;
                height: 1px;
                color: #333;
                width: 100%;
                margin-top: 0px;
                background-color: grey;
                }
            </style>""", unsafe_allow_html=True)
        
        header="""
            <div class = "heading">
                <h2>Submit your query</h2>
            </div>    

            """
        st.markdown(header,unsafe_allow_html=True)  

        # Main content
        st.markdown("<hr style='margin-top: 0px; height:2px; margin-bottom:40px;'>", unsafe_allow_html=True)
        with st.form("query"):
            st.markdown("<b>Query file (.fasta)*</b>", unsafe_allow_html=True)
            query_file = st.file_uploader("", type=["fasta","fna"])

            st.markdown("<hr style='margin-bottom:1px; margin-top:1px; baclgroung-color: grey;'>", unsafe_allow_html=True)

            st.markdown("<b>Extra Features</b>", unsafe_allow_html=True)
            st.checkbox("16S Tree")
            st.checkbox("OGRI")
            st.checkbox("WGS Tree")
            st.markdown("<hr style='margin-top:3px; margin-bottom:3px; background-color: grey;'>", unsafe_allow_html=True)

            st.markdown("<b>Email Address*</b>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                email = st.text_input("", placeholder="abc@gmail.com")
            with col2:
                st.write("")    
            submit = st.form_submit_button("Submit")
            
            flag=0
            if submit:
                if not query_file or not email:
                    st.error("Please fill in all required fields")
                else:
                    if validate_email(email):
                        flag=1
                        progress.progress(25)
                        pop()
                    else:
                        st.error("Please enter a valid email address.")



if __name__ == '__main__':
    main()
