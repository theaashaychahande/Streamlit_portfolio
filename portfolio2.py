import streamlit as st
import requests
import io
import PyPDF2
import openai
import pandas as pd

st.set_page_config(page_title="Aashay Chahande Portfolio", layout="wide")

import streamlit.components.v1 as components


components.html("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YOUR_ID_HERE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-YOUR_ID_HERE');
</script>
""", height=0)

st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YOUR_ID_HERE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-YOUR_ID_HERE');
</script>
""", unsafe_allow_html=True)


st.markdown("""
<style>
body, .main-content {
  padding-top: 50px;
}
.block-container {
    padding-top: 5 !important;
    margin-top: 5 !important;
}
body {
    margin-top: 5 !important;
    padding-top: 5 !important;
}
.navbar-container {
    position: fixed;    
    top: 3rem;
    left: 0;
    width: 100%;
    height: 50px;
    z-index: 1000;
    background: #1F2A44;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    background: #ffffff;
    padding: 0 0 0 0;
    border-radius: 0 0 18px 18px;
    display: flex;
    padding-top: 100px;
    flex-direction: column;
    justify-content: flex-end;
}

.navbar {
    display: flex;
    gap: 28px;
    justify-content: center;
    padding: 12px 0 10px 0;
    border-radius: 0 0 18px 18px;
    margin-bottom: 20px;
    position: sticky;
    top: 0;
    z-index: 100;
}

.navbar a {
    color: #ffd166;
    font-weight: bold;
    font-size: 1.08rem;
    text-decoration: none;
    padding: 7px 22px;
    border-radius: 8px;
    transition: color 0.18s, background 0.18s;
}
.navbar a:hover {
    background: #ffd16633;
    color: #fff;
}

.sticky-spacer {
    height: 10px;
}

.navbar {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    background: #1F2A44;
    padding: 12px 0 10px 0;
    border-radius: 0 0 18px 18px;
    margin-bottom: 20px;
    position: sticky;
    top: 0;
    z-index: 100;
    gap: 28px;
}

.navbar a {
    color: #ffd166;
    font-weight: bold;
    font-size: 1.08rem;
    text-decoration: none;
    padding: 7px 18px;
    border-radius: 8px;
    transition: color 0.18s, background 0.18s;
    white-space: nowrap;
}

@media screen and (max-width: 768px) {
    .navbar {
        flex-direction: column;
        align-items: center;
        gap: 14px;
        display: none;
        width: 100%;
        background: #1F2A44;
        padding: 10px 0;
        margin-bottom: 10px;
        border-radius: 0 0 18px 18px;
    }
    .navbar.show {
        display: flex;
    }
    .navbar a {
        width: 100%;
        text-align: center;
        padding: 10px 0;
        font-size: 1rem;
    }
    .mobile-nav-toggle {
        display: block;
        background: #1F2A44;
        color: #ffd166;
        font-weight: bold;
        font-size: 1.5rem;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        border: none;
        margin-bottom: 10px;
        width: 100%;
        text-align: center;
    }
}

@media screen and (min-width: 769px) {
    .mobile-nav-toggle {
        display: none;
    }
}

@media screen and (max-width: 768px) {
    .navbar-container {
        display: none !important;
    }
      .block-container {
    padding-top: 0 !important;
    margin-top: 0 !important;
  }
  body {
    margin-top: 0 !important;
    padding-top: 0 !important;
  }
  .sticky-spacer {
    height: 0 !important;
  }
}

</style>

<div class="navbar-container">
  <button class="mobile-nav-toggle" onclick="toggleMenu()">☰ Menu</button>
  <div class="navbar" id="navbarLinks">
    <a href="#about">About Me</a>
    <a href="#education">Education</a>
    <a href="#experience">Experience</a>
    <a href="#projects">Projects Gallery</a>
    <a href="#skills">Skills</a>
    <a href="#publications">Publications</a>
    <a href="#contact">Contact</a>
  </div>
</div>

<div class="sticky-spacer"></div>

<script>
function toggleMenu() {
  const navbar = document.getElementById("navbarLinks");
  if (navbar.classList.contains("show")) {
    navbar.classList.remove("show");
  } else {
    navbar.classList.add("show");
  }
}
</script>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
  background: url('YOUR_BACKGROUND_IMAGE_URL') center/cover no-repeat;
  background-attachment: fixed;
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
}
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    border-bottom: 3px solid #22304A;
}
.stTabs [data-baseweb="tab"] {
    background: linear-gradient(135deg, #1F2A44 0%, #324665 100%);
    color: #ffd166 !important;
    border-radius: 12px 12px 0 0 !important;
    padding: 16px 36px !important;
    font-size: 1.14rem;
    font-weight: bold;
    margin-bottom: -3px !important;
    transition: all .25s;
}
.stTabs [data-baseweb="tab"]:hover {
    color: #fff !important;
    background: linear-gradient(135deg, #406496 0%, #22304A 100%);
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #22304A 0%, #ffd166 150%) !important;
    color: #222 !important;
    border-bottom: 4px solid #ffd166 !important;
    transform: scale(1.06) translateY(-2px);
    box-shadow: 0 6px 22px rgba(44,62,80,0.13);
}
.card {
  width: 100% !important;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 16px;
  background: linear-gradient(135deg, #1F2A44 0%, #324665 100%);
  transition: transform .3s cubic-bezier(.4,1.6,.6,1), box-shadow .3s;
  text-align: center;
}
.card:hover, .card.hover-zoom:hover {
  transform: translateY(-5px) scale(1.04);
  box-shadow: 0 8px 16px rgba(0,0,0,0.24);
}
.section-title {
  font-size: 1.6rem;
  font-weight: bold;
  margin-bottom: 12px;
  padding: 8px;
  border-radius: 6px;
}
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-bottom: 32px;
}
.project-item {
  position: relative;
  aspect-ratio: 1/1;
  overflow: hidden;
  border-radius: 12px;
  transition: transform .3s cubic-bezier(.4,1.6,.6,1), box-shadow .3s;
}
.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .3s cubic-bezier(.4,1.6,.6,1);
}
.project-item:hover .card-img {
  transform: scale(1.05);
}
.overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity .3s ease;
  font-size: 1.2rem;
  color: #ffffff;
}
.project-item:hover .overlay {
  opacity: 1;
}
.profile-pic-popout {
  width: 160px;
  height: 200px;
  object-fit: cover;
  border-radius: 0%;
  border: 2px solid #fff;
  box-shadow: 0 2px 8px rgba(44, 62, 80, 0.18);
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 20px;
  z-index: 10;
}
.profile-card-container {
  position: relative;
  width: 100%;
  margin-bottom: 20px;
}
.profile-card-content {
  padding-top: 200px;
}
.contact-icon {
  width: 32px;
  height: 32px;
  filter: invert(100%);
  color:#ADD8E6;
  margin: 0 8px;
  vertical-align: middle;
}
.edu-cards-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
  margin-top: 20px;
  margin-bottom: 18px;
}
.edu-card {
  background: linear-gradient(135deg, #34495E 0%, #406496 100%);
  border-radius: 15px;
  padding: 22px 14px 16px 14px;
  box-shadow: 0 2px 10px rgba(30,50,80,0.13);
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 170px;
  transition: transform .3s cubic-bezier(.4,1.6,.6,1), box-shadow .3s;
  border: 2px solid #40649622;
}
.edu-card:hover {
  transform: translateY(-7px) scale(1.03);
  box-shadow: 0 8px 18px rgba(20,40,80,0.19);
  background: linear-gradient(135deg, #406496 0%, #34495E 100%);
}
.edu-card-logo {
  width: 56px;
  height: 56px;
  object-fit: contain;
  border-radius: 11px;
  background: #fff;
  margin-bottom: 10px;
  box-shadow: 0 1px 8px rgba(44,62,80,0.09);
  border: 1.5px solid #eee;
}
.edu-card-degree { font-weight: 700; font-size: 1.12rem; margin-bottom: 3px; color: #ffd166;}
.edu-card-univ { color: #ADD8E6; font-size: 1.01rem; margin-bottom: 4px;}
.edu-card-date { color: #fff; font-size: 0.98rem;}
.awards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-top: 18px;
  margin-bottom: 2px;
}
.award-card {
  background: linear-gradient(135deg, #34495E 0%, #406496 100%);
  border-radius: 12px;
  box-shadow: 0 4px 18px rgba(60,100,160,0.07);
  padding: 18px 18px 14px 18px;
  min-height: 80px;
  transition: transform .17s, box-shadow .17s;
  border: 1.5px solid #40649644;
  text-align: left;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.award-card:hover {
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 8px 24px rgba(20,60,120,0.15);
  background: linear-gradient(135deg, #22304A 0%, #406496 88%);
}
.award-title { font-weight: bold; font-size: 1.07rem; color: #ffd166; margin-bottom: 2px; margin-top: 0;}
.award-sub { font-size: 0.99rem; color: #ADD8E6; margin-bottom: 2px;}
.award-year { font-size: 0.97rem; color: #fff; opacity: 0.8;}
.award-year {margin-bottom: 2px;}
.exp-cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 18px;
  margin-top: 20px;
  margin-bottom: 20px;
}
.exp-card {
  background: linear-gradient(135deg, #34495E 0%, #406496 100%);
  border-radius: 15px;
  padding: 22px 14px 16px 14px;
  box-shadow: 0 2px 10px rgba(30,50,80,0.13);
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 215px;
  transition: transform .3s cubic-bezier(.4,1.6,.6,1), box-shadow .3s;
  border: 2px solid #40649622;
}
.exp-card:hover {
  transform: translateY(-7px) scale(1.03);
  box-shadow: 0 8px 18px rgba(20,40,80,0.19);
  background: linear-gradient(135deg, #406496 0%, #34495E 100%);
}
.exp-card-logo {
  width: 56px;
  height: 56px;
  object-fit: contain;
  border-radius: 11px;
  background: #fff;
  margin-bottom: 10px;
  box-shadow: 0 1px 8px rgba(44,62,80,0.09);
  border: 1.5px solid #eee;
}
.exp-card a.toggle-link {
      display: block;
      color: #ffd166;
      margin-top: 10px;
      font-weight: 500;
      cursor: pointer;
      text-align: right;
}
.exp-card-title { font-weight: 700; font-size: 1.12rem; margin-bottom: 3px;}
.exp-card-company { color: #ADD8E6; font-size: 1.01rem; margin-bottom: 6px;}
.exp-card-date { color: #ffd166; font-size: 0.98rem;}
.skills-category {
  margin-bottom: 14px;
}
.skills-header {
  font-size: 1.04rem;
  color: #ffd166;
  font-weight: 600;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.skill-icon {
  width: 20px;
  height: 20px;
  vertical-align: middle;
  filter: brightness(0.95) invert(0.09) sepia(1) hue-rotate(165deg) saturate(6);
}
.skills-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 2px;
}
.section-anchor {
  scroll-margin-top: 160px;
}
.skill-chip {
  background: rgba(255,255,255,0.12);
  padding: 6px 14px;
  border-radius: 16px;
  font-size: 0.97rem;
  color: #fff;
  font-weight: 500;
  border: 1.5px solid #40649633;
}
.profile-row {
  display: flex;
  gap: 32px;
  justify-content: center;
  align-items: stretch;
  margin-bottom: 30px;
}
.profile-card, .about-card {
  flex: 1 1 0px;
  min-width: 250px;
  background: linear-gradient(135deg, #1F2A44 0%, #324665 100%);
  border-radius: 16px;
  padding: 32px 18px 24px 18px;
  box-shadow: 0 3px 16px rgba(44,62,80,0.16);
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: fadeUpCard .85s cubic-bezier(.5,1.6,.4,1) both;
}
.profile-card {
  max-width: 340px;
  justify-content: flex-start;
}
.profile-pic-square {
  width: 130px;
  height: 130px;
  object-fit: cover;
  border-radius: 24px;
  border: 2.5px solid #fff;
  margin-bottom: 18px;
  box-shadow: 0 2px 10px rgba(44,62,80,0.17);
}
.about-card {
  align-items: flex-start;
  justify-content: flex-start;
}
@media (max-width: 900px) {
  .profile-row {
    flex-direction: column;
    gap: 18px;
  }
  .about-card, .profile-card {
    min-width: 0;
    width: 100%;
  }
}
.exp-responsibilities-box {    
    padding: 12px 16px;
    border-radius: 10px;
    margin-top: 14px;    
    font-size: 13px;
    font-style: italic;
    line-height: 1.6;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

def load_resume_df(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        reader = PyPDF2.PdfReader(io.BytesIO(r.content))
        records = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            sentences = [s.strip() for s in text.split('.') if s.strip()]
            for sent in sentences:
                records.append({"page": i+1, "sentence": sent})
        return pd.DataFrame(records)
    except:
        return pd.DataFrame(columns=["page", "sentence"])


resume_url = "YOUR_RESUME_PDF_URL_HERE"
resume_df = load_resume_df(resume_url)
resume_json = resume_df.to_json(orient='records')


projects = [
    {
        "title": "Smart Traffic Management AI 'Traffix'",
        "url": "https://github.com/theaashaychahande",
        "image": "https://via.placeholder.com/150/1F2A44/FFFFFF?text=Traffix",
        "tools": ["Python", "OpenCV", "TensorFlow"],
        "desc": "AI system for vehicle detection and adaptive signal timing, reducing simulated congestion by 25%."
    },
    {
        "title": "AI-Powered HR Recruitment System 'Hive Minds'",
        "url": "https://github.com/theaashaychahande",
        "image": "https://via.placeholder.com/150/1F2A44/FFFFFF?text=Hive+Minds",
        "tools": ["Python", "NLP", "scikit-learn"],
        "desc": "NLP tool for automated resume screening and ranking, improving shortlisting speed by 30%."
    },
    {
        "title": "Sign Language Detection System",
        "url": "https://github.com/theaashaychahande",
        "image": "https://via.placeholder.com/150/1F2A44/FFFFFF?text=ASL",
        "tools": ["Python", "OpenCV", "MediaPipe"],
        "desc": "Real-time ASL gesture recognition with 95% accuracy, translating signs to text/speech."
    },
    {
        "title": "Financial Portfolio Analyzer",
        "url": "https://github.com/theaashaychahande",
        "image": "https://via.placeholder.com/150/1F2A44/FFFFFF?text=Finance",
        "tools": ["Python", "Streamlit", "pandas"],
        "desc": "Financial portfolio analysis tool that provides investment recommendations and portfolio optimization."
    }
]

gif_url = "profile.jpg"
st.markdown(
    f"""
    <style>
      .welcome-card {{
        background: url("{gif_url}") center/cover no-repeat;
        border-radius: 16px;
        padding: 3rem;
        color: white;
        min-height: 180px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-bottom:24px;
        margin-top:-168px;
        box-shadow: 0 6px 30px 0 rgba(60,100,180,0.11), 0 1.5px 8px 0 rgba(60,60,90,0.08);
        transition: transform .35s cubic-bezier(.33,1.6,.66,1), box-shadow .33s;
        position: relative;
        cursor: pointer;
      }}
      .welcome-card:hover {{
        transform: scale(1.035) translateY(-7px);
        box-shadow: 0 14px 44px 0 #ffd16638, 0 2px 18px rgba(44,62,80,0.17);
        z-index: 4;
      }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="welcome-card">
      <div>
        <h1>Hello and Welcome...</h1>
        <p>Explore my portfolio to learn more about my work and projects. Let's connect and create something impactful together.</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown('<a name="about" class="section-anchor"></a>', unsafe_allow_html=True)
st.markdown("""
<style>
.hero-card {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  gap: 0;
  background: linear-gradient(135deg, #253451 0%, #324665 100%);
  border-radius: 24px;
  box-shadow: 0 6px 26px rgba(20,30,55,0.18), 0 2px 14px rgba(44,62,80,0.08);
  margin-bottom: 32px;
  min-height: 330px;
  position: relative;
  overflow: hidden;
  transition: transform .33s cubic-bezier(.37,1.7,.7,1), box-shadow .33s;
}
.hero-card:hover {
  transform: translateY(-7px) scale(1.02);
  box-shadow: 0 14px 38px 0 #ffd16630, 0 2px 18px rgba(44,62,80,0.12);
}
.hero-left {
  flex: 1 1 0px;
  min-width: 500px;
  max-width: 600px;
  background: linear-gradient(135deg, #253451 70%, #ffd16610 100%);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 38px 0 26px 0;
  box-shadow: 2px 0 18px 0 #ffd16609;
  z-index: 1;
}
.hero-pic-glow {
  display: flex !important;
  justify-content: center !important;
  margin-bottom: 20px !important;
}
.hero-pic-glow img {
  width: 400px !important;
  height: 250px !important;
  border-radius: 24px !important;
  border: none !important;
  background: none !important;
  box-shadow: none !important;
  object-fit: contain !important;
  object-position: center !important;
}
.hero-name {
  color: #fff;
  font-size: 2.44rem;
  font-weight: 800;
  text-align: center;
  margin: 6px 0 0 0;
  line-height: 1.17;
  letter-spacing: 0.01em;
}
.hero-role {
  color: #ADD8E6;
  font-size: 1.03rem;
  margin-top: 3px;
  margin-bottom: 0px;
  text-align: center;
}
.hero-location {
  color: #FFFFE0;
  font-weight: 600;
  margin-top: 8px;
  font-size: 1.01rem;
  text-align: center;
}

.hero-right {
  flex: 2 1 0px;
  padding: 38px 38px 16px 38px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  background: none;
}
.hero-about-title {
  font-size: 1.13rem;
  color: #ffd166;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: .01em;
}
.hero-about-body {
  font-size: 1.09rem;
  color: #fff;
  line-height: 1.7;
  margin-bottom: 26px;
}
.hero-contact-bar {
  width: 100%;
  margin-top: 6px;
  background: rgba(90, 130, 160, 0.12);
  border-radius: 13px;
  padding: 12px 0 6px 0;
  text-align: center;
  box-shadow: 0 2px 14px rgba(255,209,102,0.04);
}
.hero-contact-bar-title {
  color: #fff;
  font-weight: 600;
  font-size: 1.10rem;
  margin-bottom: 5px;
  letter-spacing: 0.01em;
}
.hero-contact-icons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  margin-top: 7px;
  margin-bottom: 3px;
}
.hero-contact-icons a {
  display: inline-block;
  border-radius: 8px;
  padding: 3px;
  transition: background 0.15s, transform 0.15s;
}
.hero-contact-icons a:hover {
  background: #ffd16633;
  transform: translateY(-2px) scale(1.11);
}
.hero-contact-icons img {
  width: 30px;
  height: 30px;
  filter: invert(100%);
}

@media (max-width: 900px) {
  .hero-card {flex-direction: column;align-items: center;}
  .hero-right, .hero-left {max-width:100%;padding:28px 8vw 12px;}
}
</style>

<div class="hero-card">
  <div class="hero-left">
    <div class="hero-pic-glow">
      <img src="YOUR_PROFILE_PICTURE_URL"/>
    </div>
    <div class="hero-name">Aashay Chahande</div>
    <div class="hero-role">AI & Machine Learning Practitioner<br>Deep Learning & Data Science Enthusiast</div>
    <div class="hero-location">Maharashtra, India</div>
  </div>
  <div class="hero-right">
    <div class="hero-about-title">About Me</div>
    <div class="hero-about-body">
      AI & Machine learning Practitioner with expertise in Python, Java, and deep learning frameworks, 
      proficient in libraries such as TensorFlow, PyTorch, scikit-learn, OpenCV, pandas, and NumPy. 
      Pursuing dual degrees in Mechanical Engineering (SVPCET) and Data Science (IIT Madras). 
      Experienced in developing AI-powered applications, optimizing neural networks, prompt engineering 
      and applying statistical modeling. Proven track record as a technology educator, project leader, 
      and AI community contributor.
    </div>
    <div class="hero-contact-bar">
      <div class="hero-contact-bar-title">Contact</div>
      <div class="hero-contact-icons">
        <a href="mailto:aashaychahande1717@gmail.com" target="_blank"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/gmail.svg"/></a>
        <a href="https://www.linkedin.com/in/aashay-chahande-6928b1310" target="_blank"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg"/></a>
        <a href="https://github.com/theaashaychahande" target="_blank"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/github.svg"/></a>
        <a href="https://theaashaychahande.netlify.app" target="_blank"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/globe.svg"/></a>
      </div>
    </div>
    <div style="text-align: center; margin-top: 20px;">
  <button style="
    background: #FFFFE0; 
    color: #FFF9C4; 
    font-weight: 700; 
    border-radius: 14px; 
    padding: 14px 36px; 
    font-size: 1.1rem; 
    border: none; 
    cursor: pointer;      
    transition: background 0.25s ease;">
  <a href="YOUR_RESUME_URL" 
     target="_blank" 
     style="color: #22304A; text-decoration: none;">
    View Resume
  </a>
</button>
</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Education Section
st.markdown('<a name="education" class="section-anchor"></a>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card hover-zoom">
      <div class="section-title" style="background:#34495E;">Education</div>
      <div class="edu-cards-grid">
        <div class="edu-card">
          <img src="https://upload.wikimedia.org/wikipedia/en/thumb/6/69/IIT_Madras_Logo.svg/1200px-IIT_Madras_Logo.svg.png" class="edu-card-logo"/>
          <div class="edu-card-degree">BS in Data Science and Programming</div>
          <div class="edu-card-univ">Indian Institute of Technology, Madras</div>
          <div class="edu-card-date">June 2023 – June 2027 (9.5 GPA)</div>
        </div>
        <div class="edu-card">
          <img src="https://via.placeholder.com/150/1F2A44/FFFFFF?text=SVPCET" class="edu-card-logo"/>
          <div class="edu-card-degree">BTech in Mechanical Engineering</div>
          <div class="edu-card-univ">St. Vincent Pallotti College of Engineering & Technology, Nagpur</div>
          <div class="edu-card-date">July 2024 – July 2028 (7.6 GPA)</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Experience Section
st.markdown('<a name="experience" class="section-anchor"></a>', unsafe_allow_html=True)
st.markdown(
    """  
    <div class="card hover-zoom">
      <div class="section-title" style="background:#34495E;">Professional Experience</div>
      <div class="exp-cards-grid">
        <div class="exp-card">
          <img src="https://via.placeholder.com/150/1F2A44/FFFFFF?text=Phoenix+Algo" class="exp-card-logo"/>
          <div class="exp-card-title">Founder</div>
          <div class="exp-card-company">Phoenix Algo</div>
          <div class="exp-card-date">Feb 2025 – Present</div>
          <div class="exp-responsibilities-box">
            • Lead vision, strategy, and operations of student-driven technical education initiative<br>
            • Deliver training in Python, Java, C/C++, AI/ML, and full-stack development<br>
            • Design and deliver AI/ML workshops with TensorFlow, PyTorch, scikit-learn, and OpenCV<br>
            • Help students gain hands-on industry skills
          </div>          
        </div>
        <div class="exp-card">
          <img src="https://via.placeholder.com/150/1F2A44/FFFFFF?text=Microsoft" class="exp-card-logo"/>
          <div class="exp-card-title">AI Developer</div>
          <div class="exp-card-company">Microsoft Community Project</div>
          <div class="exp-card-date">Nov 2024 – Dec 2024</div>
          <div class="exp-responsibilities-box">
            • Integrated TensorFlow for model building and pandas/NumPy for data preprocessing<br>
            • Improved prediction accuracy by 15%<br>
            • Enhanced user engagement through responsive, intelligent interface powered by Python and OpenCV
          </div>
        </div>
        <div class="exp-card">
          <img src="https://via.placeholder.com/150/1F2A44/FFFFFF?text=Upwork" class="exp-card-logo"/>
          <div class="exp-card-title">UI Developer</div>
          <div class="exp-card-company">Upwork</div>
          <div class="exp-card-date">Jul 2021 – Aug 2022</div>
          <div class="exp-responsibilities-box">
            • Designed intuitive UI layouts using Figma<br>
            • Ensured seamless integration of AI-driven features for client applications
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Activities Section
st.markdown('<a name="activities" class="section-anchor"></a>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card hover-zoom">
      <div class="section-title" style="background:#34495E;">Activities & Leadership</div>
      <div class="awards-grid">
        <div class="award-card">
          <div class="award-title">Operation Management</div>
          <div class="award-year">Feb 2025 – Present</div>
          <div class="award-sub">E-cell SVPCET</div>
        </div>
        <div class="award-card">
          <div class="award-title">Internshala Student Partner (ISP)</div>
          <div class="award-year">Feb 2025 – Present</div>
          <div class="award-sub">Internshala</div>
        </div>
      </div>
    </div>    
    """,
    unsafe_allow_html=True
)

# Publications Section
st.markdown('<a name="publications" class="section-anchor"></a>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card hover-zoom">
      <div class="section-title" style="background:#34495E;">Publications & Research</div>
      <div class="awards-grid">
        <div class="award-card">
          <div class="award-title">Evaluating Adversarial Training as a Defense Mechanism Against FGSM Attacks on ResNet50 for CIFAR-10 Classification</div>
          <div class="award-year">Feb 20, 2025</div>
          <div class="award-sub">Research Gate</div>
          <div class="award-sub" style="margin-top: 8px; font-size: 0.95rem; color: #fff; line-height: 1.4;">
            This review paper systematically examines the effectiveness of adversarial training as a defense mechanism against Fast Gradient Sign Method (FGSM) attacks on ResNet 50, a widely used convolutional neural network (CNN)
          </div>
        </div>
      </div>
    </div>    
    """,
    unsafe_allow_html=True
)

# Projects Section
st.markdown('<a name="projects" class="section-anchor"></a>', unsafe_allow_html=True)
st.markdown("""
<style>
.card.projects-gallery-pane {
  background: linear-gradient(135deg, #1F2A44 0%, #324665 100%);
  border-radius: 18px;
  box-shadow: 0 4px 28px rgba(20,30,55,0.14);
  padding: 22px 18px 28px 18px;
  margin-bottom: 22px;
}
.section-title {
  font-size: 1.35rem;
  font-weight: bold;
  margin-bottom: 22px;
  color: #ffd166;
  background:#2C3E50;
  padding: 12px 0 12px 0;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 1px 8px #22304A22;
}
.projects-4col-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin: 0 auto;
  justify-content: center;
  align-items: stretch;
}
.project-main-card {
  background: linear-gradient(135deg, #202C41 0%, #324665 100%);
  border-radius: 14px;
  box-shadow: 0 2px 12px rgba(44,62,80,0.10);
  display: flex;
  flex-direction: column;
  align-items: center;
  min-width: 0;
  transition: transform 0.18s, box-shadow 0.18s;
  border: 1.5px solid #22304A2A;
  height: 100%;
  overflow: hidden;
}
.project-main-card:hover {
  transform: translateY(-4px) scale(1.024);
  box-shadow: 0 12px 32px #ffd1661c, 0 2px 8px #22304A19;
  z-index: 2;
}
.project-img-holder {
  width: 100%;
  background: #222E40;
  display: flex;
  align-items: center;
  justify-content: center;
  padding-top: 20px;
  padding-bottom: 10px;
}
.project-img-inner {
  width: 90px;
  height: 90px;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 10px #22304A11;
  display: flex;
  align-items: center;
  justify-content: center;
}
.project-img-inner img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .18s cubic-bezier(.4,1.6,.6,1);
  border-radius: 12px;
}
.project-main-card:hover .project-img-inner img {
  transform: scale(1.07);
}
.project-card-info {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 8px 16px 16px 16px;
}
.project-title {
  font-size: 1.07rem;
  font-weight: bold;
  color: #ffd166;
  margin-bottom: 6px;
  margin-top: 2px;
  text-align: center;
  min-height: 38px;
}
.project-desc {
  color: #fff;
  font-size: 0.98rem;
  margin-bottom: 10px;
  text-align: center;
  flex: 1 1 0;
}
.project-tools-list {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-bottom: 7px;
  justify-content: center;
}
.project-tool-badge {
  background: linear-gradient(135deg,#e2e2e2 0%,#ffd166 88%);
  color: #22304A;
  font-size: 0.88rem;
  border-radius: 9px;
  padding: 2px 9px 1.5px 9px;
  font-weight: 500;
  margin-bottom: 2px;
  box-shadow: 0 1px 3px #22304A13;
}
.project-card-link {
  text-align: center;
  margin-top: 6px;
}
.project-card-link a {
  color: #ADD8E6;
  font-size: 0.97rem;
  text-decoration: underline;
  font-weight: 600;
  transition: color 0.13s;
}
.project-card-link a:hover {
  color: #ffd166;
}
@media (max-width: 1200px) {
  .projects-4col-grid {grid-template-columns: repeat(3, 1fr);}
}
@media (max-width: 900px) {
  .projects-4col-grid {grid-template-columns: repeat(2, 1fr);}
}
@media (max-width: 600px) {
  .projects-4col-grid {grid-template-columns: 1fr;}
}
</style>
""", unsafe_allow_html=True)

projects_html = '''
<div class="card projects-gallery-pane hover-zoom">
  <div class="section-title">Projects Gallery</div>
  <div class="projects-4col-grid">
'''

for proj in projects:
    tools_html = ''.join(f'<span class="project-tool-badge">{tool}</span>' for tool in proj["tools"])
    projects_html += (
        f'<div class="project-main-card hover-zoom">'
        f'<div class="project-img-holder">'
        f'<div class="project-img-inner">'
        f'<img src="{proj["image"]}" alt="{proj["title"]}"/>'
        f'</div></div>'
        f'<div class="project-card-info">'
        f'<div class="project-title">{proj["title"]}</div>'
        f'<div class="project-desc">{proj["desc"]}</div>'
        f'<div class="project-tools-list">{tools_html}</div>'
        f'<div class="project-card-link"><a href="{proj["url"]}" target="_blank">View on GitHub &rarr;</a></div>'
        f'</div></div>'
    )

projects_html += '</div></div>'

st.markdown(projects_html, unsafe_allow_html=True)

# Skills Section
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.markdown("""
<style>
.skills-section {
  background: linear-gradient(120deg, #22304A 0%, #324665 100%);
  border-radius: 28px;
  padding: 36px 18px 32px 18px;
  margin-bottom: 22px;
  box-shadow: 0 8px 34px rgba(20,30,55,0.11), 0 2px 14px rgba(44,62,80,0.09);
}
.skills-header-title {
  font-size: 1.35rem;
  font-weight: bold;
  color: #ffd166;
  background: #2C3E50;
  border-radius: 10px;
  padding: 12px 0;
  margin-bottom: 22px;
  text-align: center;
  box-shadow: 0 1px 8px #22304A22;
}
.skill-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
}
.skill-card {
  background: #1F2A44;
  color: white;
  width: 250px;
  padding: 20px 16px;
  border-radius: 16px;
  text-align: center;
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
  transition: transform 0.25s ease, box-shadow 0.25s;
}
.skill-card:hover {
  transform: translateY(-6px) scale(1.04);
  box-shadow: 0 12px 28px rgba(255,209,102,0.15), 0 6px 16px rgba(44,62,80,0.12);
}
.skill-title {
  font-size: 1.1rem;
  color: #ffd166;
  margin-bottom: 12px;
  font-weight: bold;
}
.skill-list {
  font-size: 0.9rem;
  line-height: 1.6;
  margin-top: 8px;
}
.skill-list p {
  margin: 0;
  padding: 2px 0;
}
.hover-zoom {
  transition: transform 0.25s ease, box-shadow 0.25s;
}
.hover-zoom:hover {
  transform: scale(1.02);
  box-shadow: 0 14px 32px rgba(255,209,102,0.12), 0 8px 22px rgba(44,62,80,0.1);
}
</style>

<div class="skills-section hover-zoom">
  <div class="skills-header-title">Core Skills and Technologies</div>
  <div class="skill-grid">
<div class="skill-card">
  <div class="skill-title">Programming Languages</div>
  <div class="skill-list">
    <p>Python (Advanced)</p>
    <p>Java (Intermediate)</p>
    <p>C/C++ (Intermediate)</p>
    <p>JavaScript</p>
  </div>
</div>
<div class="skill-card">
  <div class="skill-title">AI & Machine Learning</div>
  <div class="skill-list">
    <p>TensorFlow & Keras</p>
    <p>PyTorch</p>
    <p>scikit-learn</p>
    <p>OpenCV</p>
  </div>
</div>
<div class="skill-card">
  <div class="skill-title">Data Science</div>
  <div class="skill-list">
    <p>Pandas & NumPy</p>
    <p>Data Visualization</p>
    <p>Statistical Modeling</p>
    <p>SQL</p>
  </div>
</div>
<div class="skill-card">
  <div class="skill-title">Tools & Platforms</div>
  <div class="skill-list">
    <p>Git & GitHub</p>
    <p>VS Code</p>
    <p>Jupyter Notebook</p>
    <p>Streamlit</p>
  </div>
</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="card hover-zoom">
      <div class="section-title" style="background:#34495E;">Get In Touch</div>
      <div style="text-align: center; padding: 20px;">
        <p style="font-size: 1.1rem; margin-bottom: 20px;">
          I'm always open to discussing new opportunities, interesting projects, or just having a chat about technology!
        </p>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
          <a href="mailto:aashaychahande1717@gmail.com" style="color: #ffd166; text-decoration: none;">📧 Email</a>
          <a href="https://www.linkedin.com/in/aashay-chahande-6928b1310" style="color: #ffd166; text-decoration: none;">💼 LinkedIn</a>
          <a href="https://github.com/theaashaychahande" style="color: #ffd166; text-decoration: none;">🐙 GitHub</a>
          <a href="https://theaashaychahande.netlify.app" style="color: #ffd166; text-decoration: none;">🌐 Portfolio</a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown("""
<hr style='border: 0; border-top: 1px solid #eee; margin-top: 50px;' />

<div style='text-align: center; font-size: 13px; color: #444;'>
    Developed by <strong>Aashay Chahande</strong><br>
    © 2025 | Powered by Python & Streamlit 
</div>
""", unsafe_allow_html=True)
