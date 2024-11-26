import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://app.lottiefiles.com/animation/07a8dc5b-a928-4949-977e-6c5118546250")

st.set_page_config(page_title='CS PROJECT',page_icon=":tada:",layout='wide')

with st.container():
     st.subheader("Hi, I am Manan :wave:")
     st.title("Computer Science")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.subheader("CS project ideas-")
        st.write('''
1. Chatbot: Create a chatbot using NLP for customer support.\n
2.To-Do App: Build a productivity tool with reminders and categorization.\n
3.Budget Tracker: Develop an app to monitor income and expenses.\n
4.Fitness Tracker: Implement a system for tracking workouts and progress.\n
5.Quiz Game: Make a trivia or educational game with score tracking.\n
6.E-commerce Site: Design a basic online store with cart and payment features.\n
7.Social Media Clone: Create a lightweight version of a social media platform.\n
8.Weather App: Use an API to fetch and display current weather data.\n
9.Library System: Manage books, users, and lending records.\n
10.AI Image Classifier: Build a model to classify images into categories\n
             ''')
    st.write("[Learn more>](https://www.primevideo.com/storefront/home/ref=atv_nb_sf_hm)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

