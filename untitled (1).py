import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Resume", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("Downloads/download.png")
img_lottie_animation = Image.open("Downloads/download.png")
img_contact_form1 = Image.open("Downloads/download (1).png")
img_lottie_animation1 = Image.open("Downloads/download (1).png")
img_contact_form2 = Image.open("Downloads/download (2).jpg")
img_lottie_animation2 = Image.open("Downloads/download (2).jpg")

with st.container():
    st.subheader("Hi, I am Eeshan :wave:")
    st.title("A Data Scientist From India")
    st.write("I'm a pre-final year student at IIT Roorkee looking for a ML/ DL/ Analyst internship. I have 5 research internships and UG Chanakya Fellow for 2022. Skilled, dedicated, and collaborative team player. Hardworking and experienced.")
    
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a highly qualified candidate with a strong background in AI and diverse experience across multiple domains. I have completed 10+ AI projects in fields such as chemical engineering, navigation, and medical applications. With a track record of mentoring over 50 students in AI, I have successfully guided them in developing their skills and completing projects. Additionally, I have gained valuable experience through 5 research internships, where I focused on areas such as machine learning and computer vision. I possess a unique ability to apply AI techniques to solve complex problems in various domains. My adaptability, problem-solving skills, and passion for continuous learning make me an asset to your organization. I am excited to contribute to your team and help achieve your goals.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Research Internship | Mitacs | Simon Fraser University")
        st.write(
            """
            - Collaborated with clinicians and data experts to develop tools for clinical EEG assessment, analyzing a unique dataset of 50,000 cases and corresponding reports from 4 hospitals in British Columbia.
            - Led a project integrating computational neuroscience and clinical neurophysiology of 21,000 paitents, utilizing machine learning and natural language processing to classify EEG reports.
            - Developed mathematical models to accurately classify EEG recordings as normal or abnormal, including subcategories such as seizures and encephalopathy.
            - Leveraged Compute Canada Super Cluster for efficient data analysis, optimizing the utilization of high-performance computing resources.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form1)
    with text_column:
        st.subheader("Research Intern | University of Chicago")
        st.write(
            """
            - Developed a deep learning-based Alzheimer's detection system using synthetic data generation and classification techniques for 1,296 images.
            - Applied the SMOTE algorithm to generate 3,000 synthetic images, improving performance on the imbalanced dataset.
            - Trained a ResNet50 convolutional neural network, achieving an impressive 93.2% classification accuracy.
            - Deployed the model as a user-friendly web application using Gradio, enhancing accessibility for medical professionals.
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("Research Intern | IIT Roorkee | Prof. Anand Radhyeshyam")
        st.write(
            """
            - Contributed to the development of a vehicle navigation system utilizing ultrasonic sensors, Raspberry Pi, OpenCV, and LED board to detect and prevent accidents.
            - Collaborated on ultrasonic and Raspberry Pi modules to detect vehicle position and speed, integrating OpenCV for object detection and recognition.
            - Engineered LED board display system to alert drivers about blind spot objects.
            - Secured Rs. 3,00,000 in funding under 'UG Chanakya Fellowship 2022' for product-level development
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form2)
    with text_column:
        st.subheader("Research Intern | IIT Roorkee | Prof. D. Bharat")
        st.write(
            """
            - The project aspires to calculate and rank the Indian States according to Economic Complexity Index.
            - Involves a detailed analysis of the export of various products and commodities of states both Nationally and Internationally, also taking Human Development Index under consideration.
            - By Feature Engineering of the given data, we aim to predict the ECI ranking of Indian States by Time Series Prediction.
            """
        )
        
