import streamlit as st
st.set_page_config(page_title="My Webpage",page_icon=":tada",layout="wide")

lottie_coding="https://lottiefiles.com/free-animation/coding-qNY7n4OjOK"

with st.container():
   st.title("Hello Manan!! :wave:")
   st.header("Computer Science Project")
with st.container():
   st.write("---")
   left_column, right_column=st.columns(2)
   with left_column:
      st.write('''
      Choosing a topic for a computer science project depends on your interests, the scope of your course, and the resources available. Below are some ideas across various subfields of computer science:
1. Artificial Intelligence & Machine Learning
AI Chatbot: Create a chatbot using NLP that can understand and respond intelligently to user inputs.
Emotion Recognition System: Build a system using computer vision and deep learning to identify human emotions from facial expressions.
Recommendation System: Develop a recommendation engine (e.g., for movies, music, products) using collaborative filtering or content-based filtering.
AI for Healthcare: Use machine learning to predict diseases based on medical data (e.g., predicting heart disease from patient data).
2. Data Science & Analytics
Predictive Analytics: Use machine learning algorithms to predict future trends based on historical data (e.g., stock market prediction, sports score prediction).
Data Visualization Tool: Create a platform that visualizes large datasets, such as COVID-19 statistics or climate data.
Sentiment Analysis: Build a model to analyze social media posts or reviews to determine public sentiment about a topic or brand.
Big Data Analysis: Develop a tool to process and analyze large datasets (using Hadoop or Spark).
3. Cybersecurity
Password Cracking Tool: Develop a tool that demonstrates how password cracking works using brute force or dictionary attacks.
Network Intrusion Detection System: Build a system to detect suspicious network activity using machine learning or pattern recognition.
Encrypted Chat Application: Create an application that encrypts messages for secure communication, ensuring privacy and integrity.
Phishing Detection Tool: Build a tool that identifies phishing websites using URL or domain analysis.
4. Software Development & Web Technologies
E-Commerce Website: Create a fully functional e-commerce site with features like product browsing, cart management, and online payment.
Task Management App: Build an app that helps users organize and track their tasks, with reminders and project management features.
Social Media Platform: Develop a basic social media platform with features like user registration, messaging, and posting.
Real-Time Chat Application: Use WebSockets to create a real-time messaging app, similar to Slack or WhatsApp.
5. Blockchain & Cryptography
Cryptocurrency Tracker: Create an application that tracks cryptocurrency prices in real-time and provides investment insights.
Blockchain Voting System: Develop a secure online voting system using blockchain to ensure transparency and prevent fraud.
Smart Contracts: Build a decentralized application (dApp) using Ethereum that utilizes smart contracts for a specific use case (e.g., crowdfunding).
Encrypted File Sharing System: Implement a file-sharing system where files are encrypted for secure sharing and storage.
6. Mobile Development
Fitness Tracker App: Develop a mobile app that tracks user fitness data, like steps, calories burned, or heart rate.
Weather App: Build an app that fetches real-time weather data and displays it to the user, integrating location services.
Expense Tracker: Create an app that helps users track their expenses, categorize transactions, and generate reports.
7. Computer Vision
Object Detection System: Build a system that can detect objects in images or video streams using deep learning.
Face Recognition System: Create a facial recognition system that can identify people from a database of images.
Document Scanner App: Develop an app that scans physical documents and converts them into editable text using OCR (Optical Character Recognition).
Hand Gesture Recognition: Create a system that recognizes hand gestures and translates them into commands for controlling a device.
''')
   st.write("[Learn more >](https://chat.openai.com/)")
