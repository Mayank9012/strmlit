import time
import streamlit as st
import streamlit.components.v1 as components
import webbrowser

st.write("#")
#confirmation dialog
@st.experimental_dialog("Check Status")
def pop():
    task_id = st.text_input("Enter the task id")
    st.markdown("""
                <style>
                .btn {
                    background-color: #1c3b29;
                    border: #3d6154;
                    color: white;
                    padding: 10px 24px;
                    text-align: center;
                    text-decoration: none;
                    display: inline-block;
                    font-size: 16px;
                    margin: 4px 2px;
                    cursor: pointer;
                    border-radius: 12px;
                }
                </style>

    <a href="#?task_id={task_id}" class="btn1">
    <button type="button" class="btn" >Check Status</button></a>
                
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
      padding: 5px 5px 5px;      
      top : 0rem;
      right: 0rem;
      position: fixed;
      z-index:9999999999999999;

	  
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
        <li class="nav-item" ><a href="#" class="nav-link" style = 'color: #1c3b29; font-weight:bold; font-size:1em;'>Home </a></li><li class="nav-item" style="color:#034620; font-weight:bold; font-size:1em; justify-content: center;" >|</li>
        <li class="nav-item"><a href="#" class="nav-link" style = 'color:#1c3b29; font-weight:bold; font-size:1em;'>About</a></li><li class="nav-item" style="color:#034620; font-weight:bold; font-size:1em; justify-content: center;"  >|</li>
        <li class="nav-item dropdown">
        	<a href="#" class="nav-link dropbtn" style = 'color: #1c3b29; font-weight:bold; font-size:1em;'>Help</a>
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
            height: 5vh;
            position: fixed;
            			}
            [class="stDeployButton"]
            {
                visibility: hidden;
                display: none;


            }
            [class="st-emotion-cache-czk5ss e16jpq800"]
            {   
                visibility: hidden;
            }
            </style>
            """, unsafe_allow_html=True)
with st.container():
    st.markdown(navbar1,unsafe_allow_html=True)


with st.container():	
    st.markdown("""
            <div id="section1" class="section"></div>
                    <p id="welcomeText" style="color:#1c3b29;">  Welcome to NoSE </p>
                <img class = "logo" src="https://svgshare.com/i/17BS.svg" >
                <p class = "nose">Lorem ipsum dolo. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>

    """, unsafe_allow_html=True )

    components.html("""
    <style>
    @import url("https://fonts.googleapis.com/css?family=Raleway:900&display=swap");


    #container456 {
        position: fixed;
        width: 300px;
        height: 200px;
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
        font-size: 3em;
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
    col1,col2,col3 = st.columns([1,1,1])

    with col1:
        butn1= st.button("Submit Query")
        if butn1:
            url=f'http://localhost:8501/'
            webbrowser.open_new_tab(url)
                    
    with col2:	
        butn= st.button("Check Status")
        if butn:
            pop()

    st.markdown("""
 <div class="scroll-down">
                    <a href="#section2"><div class="scroll-down1"></div></a>
                </div>
""", unsafe_allow_html=True)



st.markdown("""
     <div id="section2" class="section"></div>
""", unsafe_allow_html=True)


st.markdown("""

             <div class="containercards">
            <ul id="cards">
                <li class="card" id="card1">
                    <div class="card-body">
                        <p style="font-size:2.5em; font-weight: bold; top:0;">OGRI</p><br>
                        <div class="card-content">
                            <p><br><br><br>OGRI is a tool to predict the novel species from the given 16S rRNA gene sequences.</p>
                        </div>
                    </div>
                </li>
                <li class="card" id="card2">
                    <div class="card-body">
                        <p style="font-size:2.5em; font-weight: bold; top:0;">16S Tree</p>
                        <div class="card-content">
                            <p><br><br><br>16S Tree is a tool to predict the novel species from the given 16S rRNA gene sequences.</p>
                        </div>
                    </div>
                </li>
                <li class="card" id="card3">
                    <div class="card-body">
                        <p style="font-size:2.5em; font-weight: bold; top:0;">WGS Tree</p>
                        <div class="card-content">
                            <p><br><br><br>WGS Tree is a tool to predict the novel species from the given 16S rRNA gene sequences.</p>
                        </div>
                    </div>
                </li>
                <li class="card" id="card4">
                    <div class="card-body">
                        <p style="font-size:2.5em; font-weight: bold; top: 0;">.....</p>
                    </div>
                </li>
            </ul>
        </div>

""", unsafe_allow_html=True)


st.markdown("<hr style='background-color: #3d6154; margin: 0; height: 4px; width: 100%; margin-top: 100px;'>", unsafe_allow_html=True)


st.markdown("""
<footer style='border-top: 5px solid darkgrey; text-align: center; margin-top: 20px;transform: translateX(-577px) translateY(600px); width:100vw;'>
    <p style='color: #3d6154; font-size: 15px; '>© .................</p> 
</footer>
""", unsafe_allow_html=True)
st.markdown("""
	<style>
		
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
            transform: translateX(-10%);

        }

        #cards {
            list-style: none;
            padding-left: 20px;
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
            top: 250px;
            padding-top: calc(var(--index) * var(--cardTopPadding));
            
        }
        @keyframes fadeInOut {
                0% { opacity: 0.1; }
                 100% { opacity: 1; }
            }
        #card1 .card-body {
            background-color: #1c3b29;
            color: white;
            scroll-margin-top: 250px; /* Adjust based on card position */

        }
        #card2 .card-body {
            /* background-color: #7EC4CF; */
            background-color: #1c3b29;
            color: white;
            scroll-margin-top: 250px; /* Adjust based on card position */

        }
        #card3 .card-body {
           background-color: #1c3b29;
              color: white;
            scroll-margin-top: 250px; /* Adjust based on card position */

        }
        #card4 .card-body {
           background-color: #1c3b29;
                color: white;
            scroll-margin-top: 250px; /* Adjust based on card position */

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
             opacity: 1; /* Initially set opacity */
      animation: fadeIn 3s forwards; /* Animation to fade in */
      animation-play-state: paused; /* Pause animation initially */
        }
            .card-body:hover {
            transform: scale(1.1);
        }
          .card.in-view {
      animation-play-state: running; /* Start animation when in view */
    }
            

        h2 {
            position: relative;
            font-size: 2.5em;
            color: white;
        }
			body, html {
				
				height: 100%;
				scroll-behavior: smooth;
                overflow: hidden;
			}
			.section {
				width: 100%;
				display: flex;
				flex-direction: columm;
				justify-content: center;
				align-items: center;
				text-align: center;
			}

			.scroll-down {
				position: absolute;
				bottom: 20px;
				left: 50%;
			
			}

          
            [data-testid="baseButton-secondary"]{
            transform: translateX(-225%) translateY(-900%);
				width: 170px;
				height:45px;
				border: 2px solid #3d6154;
                background-color: #1c3b29;
                position:relative;
            }
            
	.scroll-down1 {
                height: 40px;
                width: 25px;
                border: 2px solid #1c3b29;
                left: 50%;
            	position: absolute;
                border-radius: 20px;
                cursor: pointer;
                transform: translateY(-490%) translateX(15%);
                
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
                top: 0rem;
                left:35%;
                transform: translateY(-60px);
		    }
        .logo {
            position: relative;
            width: 25vw;
            transform: translateX(140%) translateY(50%);
            }
        .nose {
            position: relative;
            max-height: 300px;
            width:25vw;
            transform:translateX(-88%)  translateY(-50%) ;
            font-family: Sans;
            font-size: 1.2em; 
            font-weight: bold;  
            color:#1c3b29;
            text-align:center;
            }

        [data-testid="stIFrame"]{
            position: relative;
            width: 40%;
            transform: translateX(-115%) translateY(-115%);
 
            }
        .card-content {
            font-size: 1.2em;
            display: flex;
            color: white;
            padding: 10px;
            border-radius: 100px 100px 50px 50px;
            margin: 0px;
            font-family: Ubuntu;
            width:650px;
            height: 440px;
            overflow: hidden;
            text-align: center;
            }

        @media screen and (max-width: 490px) {
             #welcomeText{
                position: relative;               
                font-family: Ubuntu;
                font-weight:bold;
                font-size: 1.2em;
                letter-spacing: 4px;
                overflow: hidden;
                color:#1c3b29;          
                top: 0rem;
                left: 16%;
                transform: translateY(-90px);
		    }
          
            .logo {
                position: relative;
            width: 200px;
            transform: translateX(29%) translateY(-25%);
            }
            .nose {
            position: relative;
            max-height: 200px;
            width:75vw;
            transform:translateX(0%)  translateY(160%) ;
            font-family: Sans;
            font-size: 1em; 
            font-weight: bold;  
            color:#1c3b29;
            text-align:center;
            }
            [data-testid="stButton"]{
                margin:10%;
            }

            [data-testid="baseButton-secondary"]{
                display:inline-block;
                transform: translateX(28%) translateY(-693%);
				width: 135px;
				height:35px;
				border: 2px solid #3d6154;
                background-color: #1c3b29;
                position:absolute;
                margin:5%;
            }
        
            [data-testid="stIFrame"]{
                position: relative;
                width: 100%;
                transform: translateX(0%) translateY(-38%);
            }
            .scroll-down {
				position: absolute;
				bottom: 20px;
			}
            .scroll-down1 {
               display: none;
                }
            
            .containercards {
                width: 50%;
                transform: translateX(-35%) translateY(-10%);
            }
            #cards {
                width: 300px;
            }
            .card-content {
                font-size: 1em;
                width: 250px;
                height: 200px;
            }
            .card{
                    position: sticky;
            top: 300px;
            padding-top: calc(var(--index) * var(--cardTopPadding));
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

            [data-testid="stHeadingWithActionElements"]
            {   
             display: none;
            }
            [data-testid="stToolbar"]{
                display: none;
            }
            [data-testid="stHeader"]{
                display: none;
            }

            

    @media screen  and (min-width: 1135px) and (max-width: 1630px){
            #welcomeText{
                position: relative;                
                font-family: Ubuntu;
                font-weight:bold;
                font-size: 1.5em;
                letter-spacing: 4px;
                overflow: hidden;
                color:#1c3b29;          
                top: 0rem;
                left:41%;
                transform: translateY(-60px);
		    }
          
       .logo {
            position: relative;
            width: 25em;
            transform: translateX(140%) translateY(50%);
            
            }
        .nose {
            position: relative;
            max-height: 300px;
            width: 50%;
            margin-top:30px;
            transform:translateX(-50%)  translateY(-30%) ;
            font-family: Sans;
            font-size: 1em; 
            font-weight: bold;  
            color:#1c3b29;
            text-align:center;
            margin-left:2%;
            }

            [data-testid="baseButton-secondary"]{
            transform: translateX(-88%) translateY(-850%);
				width: 170px;
				height:45px;
				border: 2px solid #3d6154;
                background-color: #1c3b29;
                position:relative;
            }
            
	.scroll-down1 {
                height: 40px;
                width: 25px;
                border: 2px solid #1c3b29;
                left: 50%;
            	position: absolute;
                border-radius: 20px;
                cursor: pointer;
                transform: translateY(-600%) translateX(15%);
                
                }
			 
           
            [data-testid="stIFrame"]{
                position: relative;
                width: 40%;
                transform: translateX(-75%) translateY(-80%);
                margin-left:18%;
            }
            
            
            .containercards {
                width: 100%;
                transform: translateX(10%);
            }
            #cards {
                width: 500px;
            }
            .card-content {
                font-size: 1em;
                width: 450px;
                height: 200px;
            }


            }

    @media screen  and (min-width: 491px) and (max-width: 1134px){
            #welcomeText{
                position: relative;                
                font-family: Ubuntu;
                font-weight:bold;
                font-size: 1.5em;
                letter-spacing: 4px;
                overflow: hidden;
                color:#1c3b29;          
                top: 0rem;
                left:41%;
                transform: translateY(-60px);
		    }
          
       .logo {
            position: relative;
            width: 25vw;
            transform: translateX(180%) translateY(50%);
            left: 25%;
            }
        .nose {
            position: relative;
            max-height: 300px;
            width:30vw;
            margin-top:30px;
            transform:translateX(-83%)  translateY(30%) ;
            font-family: Sans;
            font-size: 0.9em; 
            font-weight: bold;  
            color:#1c3b29;
            text-align:center;
            left:30%;
            }
          
            [data-testid="baseButton-secondary"]{
            transform: translateX(-60%) translateY(-850%);
				width: 150px;
				height:38px;
				border: 2px solid #3d6154;
                background-color: #1c3b29;
                position:relative;
            margin-left: 20%;
            }
            
	    .scroll-down1 {
                height: 40px;
                width: 25px;
                border: 2px solid #1c3b29;
                left: 50%;
            	position: absolute;
                border-radius: 20px;
                cursor: pointer;
                transform: translateY(-600%) translateX(15%);
                
                }
			 
           
            [data-testid="stIFrame"]{
                position: sticky;
                width: 40%;
                transform: translateX(-70%) translateY(-70%);
             
            left: 30%;
            }
            
            
            .containercards {
                width: 100%;
                transform: translateX(-2%);
            }
            #cards {
                width: 60vw;
            }
            .card-content {
                font-size: 1em;
                width: 50vw;
                height: 200px;
            }


            }
		</style>


	""",unsafe_allow_html=True)

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
st.markdown("""
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)
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
  <script>
    // Script to handle adding 'in-view' class based on scroll position
    document.addEventListener('scroll', function() {
      const cards = document.querySelectorAll('.card');
      cards.forEach(card => {
        const top = card.getBoundingClientRect().top;
        if (top <= 250) {
          card.classList.add('in-view');
        } else {
          card.classList.remove('in-view');
        }
      });
    });
  </script>

"""

st.markdown(scroll_script, unsafe_allow_html=True)

