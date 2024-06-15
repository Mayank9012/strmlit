import time
import streamlit as st
import streamlit.components.v1 as components

st.write("#")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
            scroll-behavior: smooth;
    }

    [class="st-emotion-cache-r421ms e1f1d6gn0"]{
        background-color: white;
    }

    body, html {
        overflow-x:hidden;
    }
</style>
""", unsafe_allow_html=True)
navbar1 = """
    <style>
    body {
      margin: 10px;
      padding: 10px;
      font-family: Arial, sans-serif;
    }
    .navigation {
      overflow: hidden;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 10px 10px;      
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
        <li class="nav-item" ><a href="#" class="nav-link" style = 'color: #1c3b29; font-weight:bold; font-size:20px;'>Home </a></li><li class="nav-item" style="color:#034620; font-weight:bold; font-size:20px; justify-content: center;" >|</li>
        <li class="nav-item"><a href="#" class="nav-link" style = 'color:#1c3b29; font-weight:bold; font-size:20px;'>About</a></li><li class="nav-item" style="color:#034620; font-weight:bold; font-size:20px; justify-content: center;"  >|</li>
        <li class="nav-item dropdown">
        	<a href="#" class="nav-link dropbtn" style = 'color: #1c3b29; font-weight:bold; font-size:20px;'>Help</a>
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
				justify-content: center;
                -webkit-text-stroke: 0.3px #fff; 

            }
            .navigation{
            border-bottom: 0.5px solid lightgrey;
            left: 0rem;
			background-color:white;
            width:100vw;
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



st.markdown("""
<style>
    .circle-container {
        display: flex;
        justify-content: space-around;
        width: 100%;
    }

    .circle {
        width: 350px;
        height: 400px;
        border-radius: 10%;
        margin: 50px;
        margin-right: 150px;
        background-color: white;
        transition: transform 0.3s ease;
        position: relative;
        margin-bottom: 20px;
    }

    .circle:hover {
        transform: scale(1.3);
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown(navbar1, unsafe_allow_html=True)

scroll_script = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var scrollDownButton = document.querySelector('.scroll-down1 a');
    var scrollSection = document.getElementById('section2');
    var loaded = false;

    function toggleScrollButton() {
        if (loaded && window.scrollY > scrollSection.offsetTop) {
            scrollDownButton.style.display = 'block';
        } else {
            scrollDownButton.style.display = 'none';
        }
    }

    window.addEventListener('scroll', toggleScrollButton);

    scrollDownButton.addEventListener('click', function(event) {
        event.preventDefault();
        var scrollAmount = scrollSection.offsetTop - (window.innerHeight * 0);
        window.scrollTo({
            top: scrollAmount,
            behavior: 'smooth'
        });
        scrollDownButton.style.display = 'none';
    });

    setTimeout(function() {
        loaded = true;
        toggleScrollButton();
    }, 1000);
});
</script>
"""

st.markdown(scroll_script, unsafe_allow_html=True)

st.markdown("""
	<style>
		.container1{
           transform: translateY(-290px) translateX(-560px);
			background-color: white;
            width: 1900px;
            height: 100vh;
            display: flex;
            position: relative;
            justify-content: left;
            align-items: left;
            text-align: left;
           
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
			
      
		button[title="View fullscreen"]{
            visibility: hidden;
        }
        :root {
            --cards: 4;
            --cardHeight: 50vh;
            --cardTopPadding: 0.5em;
            --cardMargin: 4vw;
        }

        .containercards {
            width: 50%;
            height: 100%;
            transform: translateY(200px) translateX(30px);

        }

        #cards {
            list-style: none;
            padding-left: 20px;
            transform: translateY(0px) translateX(525px);
            display: grid;
            width:700px;
            
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
            top: 50px;
            padding-top: calc(var(--index) * var(--cardTopPadding));

        }

        #card1 .card-body {
            background-color: #1c3b29;
            color: white;
        }
        #card2 .card-body {
            /* background-color: #7EC4CF; */
            background-color: #1c3b29;
            color: white;
        }
        #card3 .card-body {
           background-color: #1c3b29;
              color: white;
        }
        #card4 .card-body {
           background-color: #1c3b29;
                color: white;
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
            flex-direction: column;
            transition: all 0.5s;     
            
        }

        h2 {
            font-size: 2.5em;
            color: white;
        }
			body, html {
				background-color: #e0ece9;
				height: 100%;
				scroll-behavior: smooth; /* Add smooth scrolling behavior */
                overflow: hidden;
			}
			.section {
				width: 100%;
				position: 
				display: flex;
				justify-content: center;
				align-items: center;
				text-align: center;
			}

			.scroll-down {
				position: absolute;
				bottom: 20px;
				left: 50%;
			
			}
        			[class="st-emotion-cache-otc82o e16zdaao0"]{
				transform: translateX(-300%) translateY(150%);
				width: 170px;
				height:45px;
				border: 2px solid #3d6154;
                position:absolute;
			}
			 .scroll-down1 {
                height: 40px;
                width: 25px;
                border: 2px solid #1c3b29;
                left: 50%;
            	position: absolute;
                border-radius: 20px;
                cursor: pointer;
                transform: translateY(285px) translateX(15px);
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
                border: 2px solid #1c3b29;
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
             #welcomeText{
                position: relative;
                font-family: Ubuntu;
                font-weight:bold;
                font-size: 1.5em;
                letter-spacing: 4px;
                overflow: hidden;
                color:#1c3b29;       
                transform: translateY(-180px) translateX(35px);
		    }

		.logo {
            position: relative;
            width: 500px;
            transform: translateX(479px) translateY(-30px);
            }
        .nose {
            position: absolute;
            width:450px;
            transform: translateY(-150px) translateX(-465px);
            font-family: Sans;
            font-size: 18px; 
            font-weight: bold;  
            color:#1c3b29;
            }
        .container23{
           
            width: 1900px;
            transform: translateX(-570px);
        }
        [data-testid="stIFrame"]{
            position: absolute;
            transform: translateX(-60%) translateY(-180%);
            z-index: 99999;
            }
        .card-content {
            font-size: 1.2em;
            display: flex;
            background-color: white;
            color: #1c3b29;
            padding: 10px;
            border-radius: 100px 100px 50px 50px;
            margin: 0px;
            font-family: Ubuntu;
            width:650px;
            height: 540px;
            overflow: hidden;
            text-align: center;
            }

        @media screen and (max-width: 500px) {
             #welcomeText{
                position: absolute;
                font-family: Ubuntu;
                font-weight:bold;
                font-size: 1.5em;
                letter-spacing: 4px;
                overflow: hidden;
                color:white;       
                transform: translateY(-40px) translateX(-70%);
                top: 160px;
		    }
            .logoclass {
            position: absolute;
            }
            .logo {
                position: fixed;
                width: 250px; 
                margin: 20px;
                padding: 20px;
                transform: translateX(360px);
            }
            .nose {
                position: absolute;
                transform: translateY(50%) translateX(-60%);
                -webkit-text-stroke: 1px #000; 
                font-family: Calibri ; font-size: 45px; font-weight: bold;  color:#ffffff;
            }
            [class="st-emotion-cache-otc82o e16zdaao0"]{
				transform: translateX(70%) translateY(-495px);
				width: 120px;
				height:25px;
				border: 2px solid #3d6154;
                position: relative;
			}
            .scroll-down {
				position: absolute;
				bottom: 20px;
			    transform: transalteX(-650px) translateY(-20px) ;
			}
            .scroll-down1 {
                height: 40px;
                width: 25px;
                border: 2px solid white;                
            	position: absolute;
                border-radius: 20px;
                cursor: pointer;
                transform: transalteX(-650px) translateY(-20px) ;
                }

            }
            [data-testid="baseLinkButton-secondary"]{
                background-color: #1c3b29;
                color: white;
                font-size: 20px;
                font-weight: bold;
               
            }
            [class="st-emotion-cache-j6qv4b e1nzilvr4"]{
            color: white;}
		</style>


	""",unsafe_allow_html=True)
	
st.markdown("""
        <div id="section1" class="section">
            	<p id="welcomeText" style="color:#1c3b29;">  Welcome to  </p>
            <img class = "logo" src="https://svgshare.com/i/17BS.svg" >
             <p class = "nose">Lorem ipsum dolo. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
            <div class="scroll-down">
				<a href="#section2"><div class="scroll-down1"></div></a>
			</div>
        </div>

            

""", unsafe_allow_html=True )
col1,col2 = st.columns([1,1])

with col1:
	st.link_button("Submit query", "http://localhost:8502")
				
with col2:	
	st.link_button("Check status", "http://localhost:8503")			

st.markdown("<hr style='position:absolute; background-color: #3d6154; margin: 0; height: 4px; width: 1900px; opacity:0.8; transform: translateX(-568px) translateY(339px);'>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
components.html("""
<style>
@import url("https://fonts.googleapis.com/css?family=Raleway:900&display=swap");


#container456 {
    position: fixed;
    width: 50%;
    height: 40%;
    bacground-color: grey;
    filter: url(#threshold) blur(0px);
    top: 30px;
    left: 0;
}

#text1,
#text2 {
    position: fixed;
    width: 100%;
    display: inline-block;
    font-family: "Raleway", sans-serif;
    font-size: 4em;
    text-align: center;
    color:#1c3b29;
    user-select: none;
}
</style>
<div id="container456">
    <span id="text1"></span>
    <span id="text2"></span>
</div>

<svg id="filters">
    <defs>
        <filter id="threshold">
            <feColorMatrix in="SourceGraphic" type="matrix" values="1 0 0 0 0
									0 1 0 0 0
									0 0 1 0 0
									0 0 0 255 -140" />
        </filter>
    </defs>
</svg>
<script>
const elts = {
    text1: document.getElementById("text1"),
    text2: document.getElementById("text2")
};

const texts = [
    "NoSE",
    "Novel Species"
];

const morphTime = 10;
const cooldownTime = 5;

let textIndex = texts.length - 1;
let time = new Date();
let morph = 10;
let cooldown = cooldownTime;

elts.text1.textContent = texts[textIndex % texts.length];
elts.text2.textContent = texts[(textIndex + 1) % texts.length];

function doMorph() {
    morph -= cooldown;
    cooldown = 0;

    let fraction = morph / morphTime;

    if (fraction > 1) {
        cooldown = cooldownTime;
        fraction = 1;
    }

    setMorph(fraction);
}

function setMorph(fraction) {
    elts.text2.style.filter = `blur(${Math.min(8 / fraction - 8, 100)}px)`;
    elts.text2.style.opacity = `${Math.pow(fraction, 0.4) * 100}%`;

    fraction = 1 - fraction;
    elts.text1.style.filter = `blur(${Math.min(8 / fraction - 8, 100)}px)`;
    elts.text1.style.opacity = `${Math.pow(fraction, 0.4) * 100}%`;

    elts.text1.textContent = texts[textIndex % texts.length];
    elts.text2.textContent = texts[(textIndex + 1) % texts.length];
}

function doCooldown() {
    morph = 0;

    elts.text2.style.filter = "";
    elts.text2.style.opacity = "100%";

    elts.text1.style.filter = "";
    elts.text1.style.opacity = "0%";
}

function animate() {
    requestAnimationFrame(animate);

    let newTime = new Date();
    let shouldIncrementIndex = cooldown > 0;
    let dt = (newTime - time) / 1000;
    time = newTime;

    cooldown -= dt;

    if (cooldown <= 0) {
        if (shouldIncrementIndex) {
            textIndex++;
        }

        doMorph();
    } else {
        doCooldown();
    }
}

animate();

</script>


""",height = 400)
st.markdown("<div style='text-align: center; margin-top: 50px;  transform: translateY(95px) translateX(40px);'><h1 style='color:#1c3b29;'>Features</h1></div>", unsafe_allow_html=True)



st.markdown("""
    <div class="container23">
     <div id="section2" class="section" style=" transform: translateY(-50px); background-color:grey;"></div>
        <div class="containercards">
            <ul id="cards">
                <li class="card" id="card1">
                    <div class="card-body">
                        <h2 style="disply:inline-block;">OGRI</h2><br>
                        <div class="card-content">
                            <p><br><br><br>OGRI is a tool to predict the novel species from the given 16S rRNA gene sequences.</p>
                        </div>
                    </div>
                </li>
                <li class="card" id="card2">
                    <div class="card-body">
                        <h2>16S Tree</h2>
                        <div class="card-content">
                            <p><br><br><br>16S Tree is a tool to predict the novel species from the given 16S rRNA gene sequences.</p>
                        </div>
                    </div>
                </li>
                <li class="card" id="card3">
                    <div class="card-body">
                        <h2>WGS Tree</h2>
                        <div class="card-content">
                            <p><br><br><br>WGS Tree is a tool to predict the novel species from the given 16S rRNA gene sequences.</p>
                        </div>
                    </div>
                </li>
                <li class="card" id="card4">
                    <div class="card-body">
                        <h2>.....</h2>
                    </div>
                </li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<hr style='background-color: #3d6154; margin: 0; height: 4px; width: 100%; margin-top: 100px;'>", unsafe_allow_html=True)

st.markdown("""
<footer style='border-top: 5px solid darkgrey; text-align: center; margin-top: 20px;transform: translateY(600px);'>
    <p style='color: #3d6154; font-size: 15px; '>© .................</p>
</footer>
""", unsafe_allow_html=True)
