
x=['Beatris: An Evil Tetris – Data Science Lab Final Project','Taskal: Intelligent Task Assistant – Personal Project (In Progress)','Automated Table Management System – The Walt Disney Company Datathon Project','TANKS Real-Time Strategy Videogame – Introduction to Embedded Systems Final Project','Chatroom Software – Software Engineering II Final Project']

y=['11/2020-12/2020','05/2019-Present','06/2019-07/2019','03/2018-05/2018','2018']

z=["Augmented existing Tetris AI implementation to improve average score by over 840%. <br> Designed Deep-Q Network based AI that gives players the least optimal piece, reducing player score by over 85%. <br> Medium blog post published at [bit.ly/BeatrisAI].","Designing platform that ingests calendar and Todoist activity to prescribe an effective daily schedule. <br> Applying machine learning to continuously adjust expectations according to user preferences and habits.", "Prototyped an interactive dashboard to service real-time reservations and walk-ins. (Python, Dash) <br> Designed algorithm to optimize waiter load balancing and reduce wasted seats, lowering Guest wait-times by 62%. (Python)","Designed a chatroom program in Java supporting individual and group messaging among multiple users across a network.<br> Applied asynchronous processing, networking protocols, frontend interface design, backend server routing mechanisms.","Developed hardware & software systems for videogame on the TI TM4C123 microcontroller. (C++, Assembly) <br> Implemented physics engine, graphics framework, procedural stage generation, and UART communication protocol."]

for i in range(len(x)):
    html='<section id="proj1" class="gallerysec leftgal">    <div class="row">        <div class="contents gallery"><!--contents sets the flexbox, gallery styles image+headers-->            <div class="project">                <img src="Images/kaweah.JPG" alt="Avatar" class="image">                <div class="overlay">                    <div class="gall-text">                        <h2>PROJNAME</h2>                        <p> PROJDESCR </p>                    </div>                </div>            </div>            <h1>Embedded Systems Development</h1>            <h2>TI M123 Hardware and Software</h2>        </div>    </div></section>'
    html=html.replace("PROJNAME",x[i])
    html=html.replace("PROJDESCR",z[i])
    print(html)
    