import time
import streamlit as st
import streamlit.components.v1 as components
st.write("#")
st.markdown("""
<style>
            [data-testid="stAppViewContainer"] {
            background-color: #e0ece9;
            }
		
            [class="st-emotion-cache-r421ms e1f1d6gn0"]{
                background-color: white;
            }
            body,html{
            	overflow-x:hidden;
            	}
            </style>
""", unsafe_allow_html=True)
        

#The navigation bar HTML
navbar1 = """
    <style>
    body {
      margin: 10px;
      padding: 10px;
      font-family: Arial, sans-serif;
    }
    .navigation {
      background-color: black;
      overflow: hidden;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 10px 10px;
      width: 100%; /* Adjusted width */
    
      top : 0rem;
      right: 0rem;
      position: fixed;
      z-index:9999999999999999;
      margin-bottom: 80px;
	  
    }

    .nav-list {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
    width: 100%; /* Adjusted width */
      transform: translateX(0%);
    }

    .nav-item {
    display: block;
      float: left;
      margin-right: 10px;
      
    }

    .nav-link {
      display: block;
      text-align: center;
      text-decoration: none;
    }

    .nav-link:hover {
      border-radius: 5px;
      color:white;
    }
    </style>

    <nav class="navigation">
    <ul class="nav-list">
        <li class="nav-item" ><a href="#" class="nav-link" style = 'color: white; font-weight:bold;'>Home </a></li><li class="nav-item" style="color:grey; transform:translate(-50px);" >|</li>
        <li class="nav-item"><a href="#" class="nav-link" style = 'color: white; font-weight:bold;'>About</a></li><li class="nav-item" style="color:grey; transform:translate(-50px);"  >|</li>
        <li class="nav-item dropdown">
        <a href="#" class="nav-link dropbtn" style = 'color: white; font-weight:bold;'>Help</a>
        </li>
    </ul>
    </nav>
	
"""
st.markdown("""
            <style>
			.nav-list{
			display: flex;
			justify-content: center;
			
			}
			.nav-link{
			text-align:center;
			transform: translateX(-50px);
            }
            </style>
            """, unsafe_allow_html=True)
with st.container():
    st.markdown(navbar1,unsafe_allow_html=True)

scroll_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var scrollDownButton = document.querySelector('.scroll-down1 a');
    var scrollSection = document.getElementById('section2');
    var loaded = false;

    // Function to toggle visibility of scroll-down button
    function toggleScrollButton() {
        if (loaded && window.scrollY > scrollSection.offsetTop) {
            scrollDownButton.style.display = 'block';
        } else {
            scrollDownButton.style.display = 'none';
        }
    }

    // Show the scroll-down button when scrolled to the section
    window.addEventListener('scroll', toggleScrollButton);

    // Toggle visibility of scroll-down button when clicked
    scrollDownButton.addEventListener('click', function(event) {
        event.preventDefault();
        var scrollAmount = scrollSection.offsetTop - (window.innerHeight * 0); // Calculate scroll amount
        window.scrollTo({
            top: scrollAmount,
            behavior: 'smooth'
        });
        scrollDownButton.style.display = 'none';
    });

    // Set loaded to true after a brief delay to avoid immediate scroll check
    setTimeout(function() {
        loaded = true;
        toggleScrollButton();
    }, 1000); // Adjust the delay if needed
});
</script>

"""



def main():
	st.markdown("""
	<style>
		[class="st-emotion-cache-r421ms e1f1d6gn0"]{
			transform: translateX(-450px) translateY(20px);
			width: 550px;
			height:400px;
			 position:ABSOLUTE;
			 background-color: #e0ece9;
			 border:1px solid #e0ece9;
		}
		.circle-container {
            display: flex;
             justify-content: space-around;
			 width: 1500px;
			 transform: translateX(-400px);
            }

        .circle {
            width: 250px;
            height: 350px;
            border-radius: 10%;
			margin:100px;
			justify-content: space-around;
            background-color: white; /* Change the color as needed */
			
        }
        
		</style>
	""",unsafe_allow_html=True)

	st.markdown("""
	<style>
			 @import url("https://fonts.googleapis.com/css?  family=Lora:400,400i,700,700i");
		[class="st-emotion-cache-r421ms e1f1d6gn0"]{
			transform: translateX(-450px) translateY(20px);
			width: 1550px;
			height:400px;
			 background-color: none;
			 opacity: 1;
			 border:1px solid #e0ece9;
			
		}
		.circle-container {
            display: flex;
			width: 100%;
		
			transform: translateX(50px) translateY(1070px);
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 170vh; /* Adjusted height for demonstration */
            position: absolute;
			 overflow-y: hidden;
            }

        .circle {
            width: 350px;
            height: 400px;
            border-radius: 10%;
			 margin:50px;
			 margin-right: 150px;
            background-color: white; /* Change the color as needed */
			transition: transform 0.3s ease;
			position: relative;
            
            margin-bottom: 20px;

        }
			
        [class="element-container st-emotion-cache-1aege4m e1f1d6gn4"]{

        }
			
        [class="st-emotion-cache-r421ms e1f1d6gn0"] img{
            text-align: center;
            display:flex;
			transform: translateX(-160px) translateY(-180px);
			height: 918px;
			z-index:1;
			 order: 1;
			
        }
		button[title="View fullscreen"]{
            visibility: hidden;
        }
      :root {
	--cards: 4;
	--cardHeight: 350px;
	--cardTopPadding: 0.5em;
	--cardMargin: 2vw;
	}

	.containercards {
		width: 90%;
		margin: 0 auto;
		transform: translateY(300px) translateX(-40px);
	}

	#cards {
		list-style: none;
		padding-left: 20px;
		display: grid;
		grid-template-columns: 1fr;
		grid-template-rows: repeat(var(--cards), var(--cardHeight));
		gap: var(--cardMargin);
		padding-bottom: calc(var(--cards) * var(--cardTopPadding));
		margin-bottom: var(--cardMargin);
	}

	#card1 {
		--index: 1;
	}
	#card2 {
		--index: 2;
	}
	#card3 {
		--index: 3;
	}
	#card4 {
		--index: 4;
	}

	.card {
		position: sticky;
		top: 0;
		padding-top: calc(var(--index) * var(--cardTopPadding));
	}

	#card1 .card-body {
		background-color:white;
	}
	#card2 .card-body {
		/* background-color: #7EC4CF; */
		background-color: white;
	}
	#card3 .card-body {
		background-color:white;
	}
	#card4 .card-body {
		background-color: white;
	}

	.card-body {
		box-sizing: border-box;
		padding: 30px;
		border-radius: 50px;
		box-shadow: 0 0 30px 0 rgba(0,0,0,0.3);
		height: var(--cardHeight);
		display: flex;
		justify-content: center;
		align-items: center;
		transition: all 0.5s;
	}

	h2 {
		font-size: 2.5em;
	}
				

		
		</style>


	""",unsafe_allow_html=True)
	st.html(""" 
		 <style>
		 .circle:hover{
			 transform: scale(1.3);
		 opacity: 1; /* Increase opacity on hover */
        }
		 </style>""")
	with st.container(border=True):
		st.image("https://iili.io/JyabV4f.jpg", # URL of the image
                    caption='',
                    width=1900, # Width of the image
                    use_column_width=False, # Don't use full column width
                    clamp=False, # Don't clip the image if it's too large
                    channels='RGB', # Specify channels
                   )
	st.markdown("""
	<style>    
			body, html {
				background-color: #e0ece9;
				height: 100%;
				scroll-behavior: smooth; /* Add smooth scrolling behavior */
                overflow-y: hidden;
			}
			.section {
				width: 100%;
				position: relative;
				display: flex;
				justify-content: center;
				align-items: center;
				text-align: center;
			}

			.scroll-down {
				position: absolute;
				bottom: 20px;
				left: 50%;
				transform: translateX(-50%) trasnlateY(220px);
				z-index: 1; /* Ensure arrow is above section */
			}

			[class="st-emotion-cache-otc82o e16zdaao0"]{
				transform: translateX(63px) translateY(175px);
				width: 170px;
				height:45px;
				border: 2px solid #3d6154;
                position:absolute;
			}
			 .scroll-down1 {
                height: 40px;
                width: 25px;
                border: 2px solid white;
                position: absolute;
                left: 50%;
                bottom: 20px;
                border-radius: 20px;
                cursor: pointer;
                }
			 
                .scroll-down1::before,
                .scroll-down1::after {
                content: "";
                position: absolute;
                top: 20%;
                left: 50%;
                height: 7px;
                width: 7px;
                transform: translate(-50%, -100%) rotate(45deg);
                border: 2px solid white;
                border-top: transparent;
                border-left: transparent;
                animation: scroll-down1 1s ease-in-out infinite;
                }
			 
                .scroll-down1::before {
                top: 30%;
                animation-delay: 0.3s;
                /* animation: scroll-down1 1s ease-in-out infinite; */
                }

                @keyframes scroll-down1 {
                0% {
                    /* top:20%; */
                    opacity: 0;
                }
                30% {
                    opacity: 1;
                }
                60% {
                    opacity: 1;
                }
                100% {
                    top: 90%;
                    opacity: 0;
                }
                }
			 img{
			 transform: translateX(133px) translateY(-190px);
			 position:  absolute;
			 animation-delay:2s;
             }
             #welcomeText {
		      position: relative;
		      font-family: Georgia;
		      font-weight:bold;
		      font-size: 2em;
		      letter-spacing: 4px;
		      overflow: hidden;
		      color:white;
		      transform: translateX(128px) translateY(-180px);
		      
		    }
		@keyframes glow {
  0% { text-shadow: 0 0 5px rgba(255, 255, 255, 0.8); }
  50% { text-shadow: 0 0 10px rgba(255, 255, 255, 0.8); }
  100% { text-shadow: 0 0 5px rgba(255, 255, 255, 0.8); }
}

@keyframes flicker {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.8; }
}
		</style>
			 
	""",unsafe_allow_html=True)
	st.markdown("""  <p id="welcomeText" style="color:white;">--- Welcome to ---</p>""",unsafe_allow_html=True)
	st.image("https://svgshare.com/i/171i.svg", # URL of the image
                    caption='',
                    width=400, # Width of the image
                    use_column_width=False, # Don't use full column width
                    clamp=False, # Don't clip the image if it's too large
                    channels='RGB', # Specify channels
                   )
	st.markdown("""
	<div id="section1" class="section">
    <p class = "nose" style="font-family: Georgia ; color: white ; font-size: 56px; font-weight: bold; transform: translateY(70px) translateX(-10px); text-shadow: 1px 1px 2px black, 0 0 25px blue, 0 0 5px white;   animation: glow 1s ease-in-out infinite alternate, flicker 1s infinite alternate;
"> Novel Species</p>
    </div>
			 """,unsafe_allow_html=True)
	col1,col2 = st.columns([1,1])
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")
	with col1:
		st.link_button("Submit query", "http://localhost:8501")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")

		
		
	with col2:	
		st.link_button("Check status", "http://localhost:8501")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")

	st.html(scroll_script)
	
#	st.markdown(scroll_down_button, unsafe_allow_html=True)
	st.markdown("""
    <div class="scroll-down">
        <a href="#section2" ><div class="scroll-down1" src="" alt="Scroll down" style = "color:white; transform: translateX(-36px) translateY(185px);"></div></a>
    </div>
			 """,unsafe_allow_html=True)
	
	st.markdown("<hr style='transform: translateX(-500px) translateY(194px); justify-content:space-around; background-color: #3d6154; margin:0px; height:4px; width: 1700px; margin-bottom:150px;'>", unsafe_allow_html=True)
	st.write(" ")
	st.write(" ")
	st.write(" ")
	st.write(" ")

	st.markdown("""
        	<div style = "transform: translateX(240px) translateY(221px); position:relative;">
			 <h1> Features </h1>
		</div>""",unsafe_allow_html=True)

	st.markdown("""
		<div id="section2" class="section">
		</div>

	""", unsafe_allow_html=True)
	st.markdown("""<img src="https://svgshare.com/i/172P.svg" style = "transform:translateX(-600px) translateY(350px); width: 1900px;" >""", unsafe_allow_html=True)
	st.markdown("""<img src="https://svgshare.com/i/171M.svg" style = "transform:translateX(-600px) translateY(1300px); width: 1900px;" >""", unsafe_allow_html=True)
	st.markdown("""
	    <div class="containercards">
		<ul id="cards">
		    <li class="card" id="card1">
		        <div class="card-body">
		            <h2>OGRI</h2>
		        </div>
		    </li>
		    <li class="card" id="card2">
		        <div class="card-body">
		            <h2>16S Tree</h2>
		        </div>
		    </li>
		    <li class="card" id="card3">
		        <div class="card-body">
		            <h2>WGS Tree</h2>
		        </div>
		    </li>
		    <li class="card" id="card4">
		        <div class="card-body">
		            <h2>.....</h2>
		        </div>
		    </li>
		</ul>
	    </div>
			 """,unsafe_allow_html=True)

	
	st.markdown("<hr style='transform: translateX(-500px) translateY(200px) ; background-color: #3d6154; margin-top:90px; height:4px; width: 1700px; margin-bottom:150px;'>", unsafe_allow_html=True)
	st.markdown("""<img src="https://svgshare.com/i/172Q.svg" style = "transform:translateX(-600px) translateY(65px); width: 1900px; " >""", unsafe_allow_html=True)

	st.markdown("""<div id="section3" class="section" >
		</div>""", unsafe_allow_html=True)
	
	st.markdown("""""", unsafe_allow_html=True)
	st.markdown("""<footer style='transform: translateX(-550px) translateY(1600px); border-top:5px solid darkgrey; width:1800px; height: 100px;'>
				<p style='color: #3d6154; font-size: 15px;'>© .................</p>
				</footer>""", unsafe_allow_html=True)


if __name__ == '__main__':
	main()
