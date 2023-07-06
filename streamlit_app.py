import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.markdown(
    """
    <h1 style='text-align: center;'><b>Quentin Hsia, AI Robot Mania</h1>
    """,
    unsafe_allow_html=True
)

image = Image.open('Quentin.png')
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{img_str}" width="300"/></div>', unsafe_allow_html=True)


st.markdown('## **Summary**', unsafe_allow_html=True)
st.info('''
- Highly skilled in multi-agent collaborative robotic systems and intelligent perception system development, with extensive experience in C++, Python, Linux, and ROS/ROS2, obtained through a Master's program at Tsinghua University and hands-on engineering projects.
- A proven track record of academic and project-based achievements, including multiple ACM publications, awards in competitive tech and development programs, and successful leadership roles in university clubs.
- Possessing broad professional experience, from machine learning and software engineering internships to involvement in complex system innovations and supply chain automation, showcasing robust technical skills, software development, automation, and system integration capabilities.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/quentin-hsia-71484b1b9/" target="_blank">Quentin Hsia</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#hands-on projects">Hands-On Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## **Education**
''')

txt('**Master of Data Science and Information Technology**, *Tsinghua University*, China',
'2021-2024')
st.markdown('''
- GPA: `3.50`
- Research thesis entitled `Informative Path Planning for Lost Person Search with Collaborative UAV Swarm`.
- *ACM Publications*: `"VisionARy: Exploratory research on Contextual Language Learning using AR glasses with ChatGPT"`, in CHITaly2023 
- *ACM Publications*: `"FireHunter: Adaptive and Non-Myopic UAV Swarm Collaboration for Proactive Fire Suppression with Incomplete Information"` in MobiCom '23 (under review)
''')

txt('**Bachelors of Engineering Science**, *National Cheng Kung University*, Taiwan',
'2017-2021')
st.markdown('''
- GPA: `3.43`
- Graduated with First Class Honors.
''')

#####################
st.markdown('''
## **Work Experience**
''')

txt('**Machine Learning Intern**, *Desktop Computing Development Lab*, Lenovo',
'2023.05- Now')
st.markdown('''
- Developed ROS-based control software for an autonomous vehicle, demonstrating expertise in robotics software and system control.
- Implemented object/gesture recognition and speech recognition with multi-AI modules
- Designed comprehensive system dataflow for backend and frontend operations, highlighting proficiency in software
integration
''')

txt('**Software Engineer Intern**, *Supply Chain*, Lumentum (LITE: NASDQ)',
'2021.02-2021.09')
st.markdown('''
- Automated reports using Python, VBA Macro, and AWS Athena DB, demonstrating expertise in software development and automation
- Developed a chip warehouse management app, further solidifying understanding of system integration
- Designed local database schema for reports allocation
''')

txt('**Software Development Engineer** *(Outsource)*, Knowledge Discovery Laboratory, National Cheng Kung University',
'2020.02-2020.09')
st.markdown('''
- Collaborated with Taiwan's Industrial Technology Research Institute (ITRI) to develop a data monitoring system for a factory in Taiwan
- Designed the PyQt5 user interface and managed subprocesses for frontend-backend interactions, showing skills in user interface design and system integration
- Design the system protection to prevent the system from being operated twice
''')


#####################
st.markdown('''
## **Hands-On Projects**
''')

txt('**VisionARy: AR glasses with ChatGPT**, *AIGC + CV + HCI*',
'2023.02- Now')
st.markdown('''
- Developed ROS-based control software for an autonomous vehicle, demonstrating expertise in robotics software and system control.
- Implemented object/gesture recognition and speech recognition with multi-AI modules
- Designed comprehensive system dataflow for backend and frontend operations, highlighting proficiency in software
integration
- [Demo](https://1drv.ms/v/s!Ar8Wp1Ye8gDYihVNRYtmiwJP09gQ?e=tYlpZL)
''')

image = Image.open('QwithCasey.JPG')
buffered = BytesIO()
image.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()
st.markdown(f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{img_str}" width="400"/></div>', unsafe_allow_html=True)
st.markdown('\n')


txt('**Human Drone Interaction**, *Robotic System + HCI*',
'2022.02- 2023.02')
st.markdown('''
- System Design: Incorporated visual perception, wireless communication, low-computational edge computing, and planning
control
- Perception: Utilized MediaPipe framework for face, gesture, speech recognition, and environmental perception
- Communication and Computation: Implemented SSH for wireless communication and Raspberry Pi for resolving multi-
video stream port occupancy issues, optimizing balance between transmission and computation
- Planning and Control: Developed task-specific algorithms and applied PID control for trajectory fitting and task completion
(reference [GitHub repository](https://github.com/handsomehsia/Human-Drone-Interaction.git))
''')
st.markdown(
    """
    <div style='display: flex; justify-content: center;'>
        <img src='https://media.giphy.com/media/vd3AIxSkZ17tIwMN3a/giphy-downsized-large.gif' alt='Alt Text'/>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('\n')

txt('**AIdear Competition: AI Mango Disease Recognition System**, *CV + ML*','2020.10-2021.02')
st.markdown('''
- Programmed SQL databases and facilitated frontend-backend communication through database implementation
- Expanded dataset using data augmentation techniques: rotation, horizontal/vertical flipping, Gaussian blur, and grayscale
- Researched and selected ResNet as the deep learning model for the competition, tuning model parameters for improved
''')

txt('**Taishin Bank Commercial Big Data Competition**, *ML*', '2019.03-2019.08')
st.markdown('''
- Predicted next-year fund and credit product purchases for customers based on 230,000 consumption records
- Implemented machine learning using R programming language
- Chose XGBoost as the competition model, tuning model parameters for improved performance
''')

#####################
# st.markdown('''
# ## Bioinformatics Tools
# ''')
# txt4('ABCpred', 'A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors', 'http://codes.bio/abcpred/')
# txt4('AutoWeka', 'An automated data mining software based on Weka', 'http://www.mt.mahidol.ac.th/autoweka/')
# txt4('ACPred', 'A computational tool for the prediction and analysis of anticancer peptides','http://codes.bio/acpred/')
# txt4('BioCurator', 'A web server for curating ChEMBL bioactivity data', 'http://codes.bio/biocurator/')
# txt4('CryoProtect', 'A web server for classifying antifreeze proteins from non-antifreeze proteins','http://codes.bio/cryoprotect/')
# txt4('ERpred', 'A web server for the prediction of subtype-specific estrogen receptor antagonists', 'http://codes.bio/erpred')
# txt4('HCVpred', 'A web server for predicting the bioactivity of Hepatitis C virus NS5B inhibitors', 'http://codes.bio/hemopred/')
# txt4('HemoPred', 'A web server for predicting the hemolytic activity of peptides', 'http://codes.bio/hemopred/')
# txt4('iQSP', 'A sequence-based tool for the prediction and analysis of quorum sensing peptides', 'http://codes.bio/iqsp/')
# txt4('Meta-iAVP', 'A sequence-based meta-predictor for improving the prediction of antiviral peptides', 'http://codes.bio/meta-iavp/')
# txt4('osFP', 'A web server for predicting the oligomeric state of fluorescent proteins', 'http://codes.bio/osfp/')
# txt4('PAAP', 'A web server for predicting antihypertensive activity of peptides', 'http://codes.bio/paap/')
# txt4('PepBio', 'A web server for predicting the bioactivity of host defense peptide', 'http://codes.bio/pepbio')
# txt4('PyBact', 'Open source software written in Python for bacterial identification', 'https://sourceforge.net/projects/pybact/')
# txt4('TargetAntiAngio', 'A sequence-based tool for the prediction and analysis of anti-angiogenic peptides','http://codes.bio/targetantiangio/')
# txt4('ThalPred', 'Development of decision model for discriminating Thalassemia trait and Iron deficiency anemia','http://codes.bio/thalpred/')
# txt4('THPep', 'A web server for predicting tumor homing peptides','http://codes.bio/thpep/')


#####################
st.markdown('''
## **Skills**
''')
txt3('Programming', '`Python`, `R`, `C++`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Deep Learning', '`PyTorch`, `TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Robotic Development', '`ROS`, `ROS2`')


#####################
st.markdown('''
## **Social Media**
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/quentin-hsia-71484b1b9/')
txt2('GitHub', 'https://github.com/handsomehsia')
txt2('ORCID', 'https://orcid.org/0009-0006-2901-3288')

