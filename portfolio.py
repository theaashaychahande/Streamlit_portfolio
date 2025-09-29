import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import webbrowser
import base64
import plotly.graph_objects as go  

st.set_page_config(
    page_title="Aashay Chahande - AI/ML Portfolio",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .main {
        padding: 0rem 1rem;
    }
    
    .css-18e3th9 {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    .profile-img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        margin-bottom: 1rem;
    }
    
    .skill-bar {
        height: 20px;
        background: linear-gradient(90deg, #4CAF50 0%, #2E7D32 100%);
        border-radius: 10px;
        margin-bottom: 10px;
    }
    
    .project-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px;
        background-color: #f9f9f9;
        transition: transform 0.3s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    
    .dark-mode .project-card {
        background-color: #262730;
    }
    
    .header-text {
        background: linear-gradient(90deg, #4CAF50 0%, #2196F3 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    
    .social-icon {
        font-size: 24px;
        margin-right: 15px;
        color: #4CAF50;
    }
    
    .tag {
        display: inline-block;
        background-color: #e0f7fa;
        color: #006064; 
        padding: 4px 8px; 
        border-radius: 15px;
        font-size: 0.8rem;
        margin: 3px;
    }
    
    .dark-mode .tag {
        background-color: #006064;
        color: #e0f7fa;
    }
    
    .nav-link {
        display: block;
        padding: 10px 15px;
        margin: 5px 0;
        border-radius: 5px;
        color: #333;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    .nav-link:hover {
        background-color: #4CAF50;
        color: white;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)


if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False


with st.sidebar:
    st.title("Aashay Chahande")
    st.markdown('<p class="header-text">AI/ML Practitioner | Deep Learning Enthusiast</p>', unsafe_allow_html=True)
    
  
    try:
        image = Image.open("profile.jpg")
        st.image(image, width=200, caption="Aashay Chahande")
    except:
        st.warning("Add a profile.jpg file to show your image")
    
    st.write("📍 Maharashtra, India")
    
  
    st.markdown("### Connect with Me")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📧", help="Email"):
            webbrowser.open_new_tab("mailto:aashaychahande1717@gmail.com")
    with col2:
        if st.button("🔗", help="LinkedIn"):
            webbrowser.open_new_tab("https://www.linkedin.com/in/aashay-chahande-6928b1310")
    with col3:
        if st.button("🐙", help="GitHub"):
            webbrowser.open_new_tab("https://github.com/theaashaychahande")
    
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("🌐", help="Portfolio"):
            webbrowser.open_new_tab("https://theaashaychahande.netlify.app")
    with col5:
        if st.button("📱", help="Phone"):
            st.toast("Phone: +91 7507666700")
    
    st.markdown("---")
  
    st.markdown("### Navigation")
    if st.button("🏠 Summary"):
        st.session_state.nav_section = "summary"
    if st.button("💻 Technical Skills"):
        st.session_state.nav_section = "skills"
    if st.button("💼 Professional Experience"):
        st.session_state.nav_section = "experience"
    if st.button("🚀 Projects"):
        st.session_state.nav_section = "projects"
    if st.button("🎓 Education"):
        st.session_state.nav_section = "education"
    if st.button("📚 Publications"):
        st.session_state.nav_section = "publications"
    if st.button("🏆 Activities & Achievements"):
        st.session_state.nav_section = "activities"
    if st.button("📞 Get In Touch"):
        st.session_state.nav_section = "contact"
    
    st.markdown("---")
    
    try:
        with open("Aashay_Resume.pdf", "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="Aashay_Chahande_Resume.pdf">📄 Download Resume</a>'
        st.markdown(href, unsafe_allow_html=True)
    except:
        st.info("📄 Resume download will be available soon.")
    

    st.markdown("---")
    st.markdown("### Quick Stats")
    st.write("📊 Projects Completed: 4+")
    st.write("👨‍💻 Students Mentored: 100+")
    st.write("📚 Research Papers: 1")
    st.write("🎓 Dual Degrees in Progress")


if st.session_state.dark_mode:
    st.markdown("""
    <style>
        .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }
    </style>
    """, unsafe_allow_html=True)

st.title("Aashay Chahande")
tagline = "AI & Machine Learning Practitioner | Deep Learning & Data Science Enthusiast | Technology Educator"
st.write(tagline)

if 'nav_section' not in st.session_state or st.session_state.nav_section == "summary":
    st.header("Summary")
    st.write("""
    Passionate about advancing AI through rigorous research and practical applications. Currently pursuing dual degrees in 
    Data Science & ML (IIT Madras) and Mechanical Engineering (SVPCET) to bridge theoretical knowledge with real-world problem-solving. 
    Published work on adversarial defense mechanisms for neural networks. As Founder of Phoenix Algo, I lead tech education initiatives, 
    mentoring students in AI/ML. My interdisciplinary approach combines engineering principles with cutting-edge ML to build robust systems.
    """)

if 'nav_section' not in st.session_state or st.session_state.nav_section == "skills":
    st.header("Technical Skills")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Programming Languages")
        languages = {
            'Python': 90,
            'Java': 80,
            'C/C++': 75,
            'SQL': 85
        }
        
        for lang, level in languages.items():
            st.write(f"**{lang}**")
            st.progress(level/100)

    with col2:
        st.subheader("AI/ML Frameworks")
        frameworks = {
            'TensorFlow': 85,
            'PyTorch': 80,
            'Scikit-learn': 90,
            'OpenCV': 85,
            'Hugging Face Transformers': 75,
            'MediaPipe': 80,
            'spaCy': 75
        }
        
        for framework, level in frameworks.items():
            st.write(f"**{framework}**")
            st.progress(level/100)

    with col3:
        st.subheader("Data Science & Tools")
        tools = {
            'Pandas': 90,
            'NumPy': 85,
            'Matplotlib': 80,
            'Seaborn': 75,
            'Streamlit': 85,
            'Git/GitHub': 85,
            'Jupyter/Colab': 90
        }
        
        for tool, level in tools.items():
            st.write(f"**{tool}**")
            st.progress(level/100)

if 'nav_section' not in st.session_state or st.session_state.nav_section == "experience":
    st.header("Professional Experience")
    expander = st.expander("View Work History", expanded=True)
    with expander:
        st.subheader("Founder - Phoenix Algo (February 2025 - Present)")
        st.write("""
        - Oversee company vision and deliver high-quality education in Python, Java, C/C++, AI/ML, and full-stack development.
        - Design and conduct workshops using TensorFlow, PyTorch, scikit-learn, and OpenCV.
        - Mentor students to become industry-ready professionals.
        """)

        st.subheader("AI Developer - Microsoft Community (November 2024 - December 2024)")
        st.write("""
        - Implemented Artificial Neural Networks (ANN) for a personal health assistant project.
        - Focused on optimizing AI-driven insights to enhance user engagement and decision-making.
        - Used Python and OpenCV to ensure seamless and intelligent user experience.
        """)

        st.subheader("Graphic Design Artist - Freelancer.com (March 2019 - October 2023)")
        st.write("""
        - Created political posters, branding, logos, marketing materials, and social media graphics.
        - Delivered 50+ freelance design solutions tailored to client objectives.
        - Focused on impactful visuals and effective communication.
        """)

        st.subheader("UI Designer - Upwork (July 2021 - August 2022)")
        st.write("""
        - Designed intuitive and visually appealing user interfaces using Figma.
        - Ensured seamless integration of AI-driven features for client applications.
        - Prioritized user-centric designs to enhance engagement and usability.
        """)

        st.subheader("Internshala Student Partner (March 2025 - Present)")
        st.write("""
        - Promote Internshala Trainings via on-campus seminars, workshops, and social media.
        - Collaborate with student communities to drive engagement and organize marketing initiatives.
        - Help peers upskill through relevant courses.
        """)

        st.subheader("Operations Management - Ecell SVPCET (February 2025 - Present)")
        st.write("""
        - Optimize workflows and improve efficiency of entrepreneurial initiatives.
        - Streamline processes and facilitate collaboration to support startup growth.
        """)

        st.subheader("Student Volunteer - Code Crafters, IIT Madras (July 2024 - January 2025)")
        st.write("""
        - Participated in student-led tech society focused on coding and innovation.
        - Collaborated on projects and learning initiatives within IIT Madras ecosystem.
        """)

if 'nav_section' not in st.session_state or st.session_state.nav_section == "projects":
    st.header("Projects")
    projects = [
        {
            "title": "Smart Traffic Management AI 'Traffix'",
            "description": "AI system for vehicle detection and adaptive signal timing, reducing simulated congestion by 25%.",
            "technologies": ["Python", "OpenCV", "TensorFlow", "Computer Vision"],
            "github": "https://github.com/theaashaychahande/traffix",
            "image": "assets/traffix.png"
        },
        {
            "title": "AI-Powered HR Recruitment System 'Hive Minds'",
            "description": "NLP tool for automated resume screening and ranking, improving shortlisting speed by 30%.",
            "technologies": ["Python", "NLP", "spaCy", "Scikit-learn"],
            "github": "https://github.com/theaashaychahande/hive-minds",
            "image": "assets/hive_minds.png"
        },
        {
            "title": "Sign Language Detection System",
            "description": "Real-time ASL gesture recognition with 95% accuracy, translating signs to text/speech.",
            "technologies": ["Python", "MediaPipe", "OpenCV", "Deep Learning"],
            "github": "https://github.com/theaashaychahande/sign-language-detector",
            "image": "assets/sign_language.png"
        },
        {
            "title": "Financial Portfolio Analyzer",
            "description": "Financial portfolio analysis tool built with Python and Streamlit that provides investment recommendations and portfolio optimization.",
            "technologies": ["Python", "Streamlit", "Pandas", "Financial Analysis"],
            "github": "https://github.com/theaashaychahande/financial-analyzer",
            "image": "assets/financial_analyzer.png"
        }
    ]

    for i, project in enumerate(projects):
        st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        st.subheader(project["title"])
        st.write(project["description"])
        
       
        tags_html = "".join([f'<span class="tag">{tech}</span>' for tech in project["technologies"]])
        st.markdown(tags_html, unsafe_allow_html=True)
        
      
        try:
            project_img = Image.open(project["image"])
            st.image(project_img, caption=project["title"], use_column_width=True)
        except:
            st.info("Project image not available.")
            
        if st.button(f"View Code →", key=f"github_{i}"):
            webbrowser.open_new_tab(project["github"])
        st.markdown('</div>', unsafe_allow_html=True)


if 'nav_section' not in st.session_state or st.session_state.nav_section == "education":
    st.header("Education")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Indian Institute of Technology, Madras")
        st.write("**Bachelor of Science in Data Science and Machine Learning**")
        st.write("July 2024 - July 2028 | GPA: 9.5/10 (as per doc)")

    with col2:
        st.subheader("St. Vincent Pallotti College of Engineering & Technology")
        st.write("**Bachelor of Technology in Mechanical Engineering**")
        st.write("August 2024 - August 2028 | GPA: 7.6/10 (as per doc)")

if 'nav_section' not in st.session_state or st.session_state.nav_section == "publications":
    st.header("Publications")
    with st.expander("Research Paper Details", expanded=True):
        st.subheader("Evaluating Adversarial Training as a Defense Mechanism Against FGSM Attacks on ResNet50 for CIFAR-10 Classification")
        st.write("""
        Published on ResearchGate, this paper examines the role of adversarial training in improving 
        model robustness against FGSM attacks on ResNet50, with empirical results on the CIFAR-10 dataset.
        
        **Key Contributions:**
        - Analyzed effectiveness of adversarial training against Fast Gradient Sign Method (FGSM) attacks.
        - Evaluated performance trade-offs between clean accuracy and adversarial robustness.
        - Provided empirical evidence on ResNet50's defensive capabilities under adversarial conditions.
        
        **Technologies Used:** Python, TensorFlow, Scikit-learn, Adversarial Robustness Toolbox
        """)
        
        st.info("https://www.researchgate.net/profile/Aashay-Chahande?ev=hdr_xprf")

if 'nav_section' not in st.session_state or st.session_state.nav_section == "activities":
    st.header("Activities & Achievements")

    st.subheader("Activities")
    activities = [
        "**Operation Management, E-cell SVPCET** (Feb 2025 - Present)",
        "**Student Volunteer, Code Crafters IITM** (July 2024 - Jan 2025)",
        "**Internshala Student Partner** (Mar 2025 - Present)"
    ]
    for activity in activities:
        st.write(f"• {activity}")

    st.subheader("Achievements")
    achievements = [
        "**'Student of the Year'** by Academical Institution of Wardha (Aug 2023)",
        "**Published Research Paper** on adversarial ML defense mechanisms (2024)",
        "**Delivered 50+ freelance design solutions** across diverse domains"
    ]
    for achievement in achievements:
        st.write(f"• {achievement}")

if 'nav_section' not in st.session_state or st.session_state.nav_section == "contact":
    st.header("Get In Touch")
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        
        with col2:
            subject = st.text_input("Subject")
            phone = st.text_input("Phone (optional)")
        
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            if name and email and subject and message:
                st.success("Thank you for your message! I'll get back to you soon.")
            
            else:
                st.error("Please fill in all required fields (Name, Email, Subject, Message).")

    
    st.subheader(" Ask My AI Assistant ")

    user_question = st.text_input("Type your question (e.g., 'Tell me about Traffix' or 'How to contact Aashay?'):", key="chatbot_input")

    if user_question:
        user_question = user_question.lower()
        response = ""
        
        if any(word in user_question for word in ["research", "paper", "fgsm", "adversarial"]):
            response = "I published a research paper on defending AI models against adversarial attacks using FGSM on ResNet50. Check the 'Publications' section for details!"
        elif any(word in user_question for word in ["traffix", "traffic", "congestion"]):
            response = "Traffix is my AI project that uses computer vision to detect vehicles and optimize traffic light timing, reducing simulated congestion by 25%. Built with Python, OpenCV, and TensorFlow."
        elif any(word in user_question for word in ["hive minds", "hr", "recruitment", "resume"]):
            response = "Hive Minds is an NLP tool I built that automates resume screening and ranking, improving shortlisting speed by 30%. It uses spaCy and scikit-learn."
        elif any(word in user_question for word in ["sign language", "asl", "gesture"]):
            response = "My Sign Language Detection System recognizes ASL gestures in real-time with 95% accuracy and translates them to text or speech. It's powered by MediaPipe and OpenCV."
        elif any(word in user_question for word in ["contact", "email", "phone", "linkedin"]):
            response = "You can reach me at aashaychahande1717@gmail.com, call +91 7507666700, or connect with me on LinkedIn!"
        elif "phoenix algo" in user_question:
            response = "I'm the Founder of Phoenix Algo, where I lead tech education initiatives and mentor students in AI/ML and programming."
        else:
            response = "I'm an AI assistant trained on Aashay's portfolio. Try asking about his projects, research, or how to contact him!"

        st.info(f"**AI Assistant:** {response}")

st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.write("**Connect with me:**")
    st.write("[LinkedIn](https://linkedin.com/in/aashay-chahande-6928b1310) | [GitHub](https://github.com/theaashaychahande)")

with footer_col2:
    st.write("**Portfolio:**")
    st.write("[theaashaychahande.netlify.app](https://theaashaychahande.netlify.app)")

with footer_col3:
    st.write("**Email:** aashaychahande1717@gmail.com")
    st.write("**Phone:** +91 7507666700")

st.markdown("<p style='text-align: center; color: gray;'>© 2025 Aashay Chahande. All rights reserved.</p>", unsafe_allow_html=True)
