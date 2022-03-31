from turtle import st
import requests
import streamlit as pp

#dont move this line idk why everything breaks
pp.set_page_config(page_title="My Webpage", page_icon=":monkey:", layout="wide")
from streamlit_lottie import st_lottie

"""from PIL import Image
"""



#access json jazz
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#assets 
lottie_coding= load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_dqbik4tt.json")

#header section
#name
with pp.container():
    pp.subheader("Yo, I am Talha Ahmed :wave:")
    #short bio
    pp.title("A student attending Troy High School")
    pp.write(" A student entusiatic about the ever growing world of technology!")


#more text ig
with pp.container():
    pp.write("---")
    left_column, right_column = pp.columns(2)
    with left_column:
        pp.header("What I do")
        pp.write("##")
        pp.write("Come up with something to say lmao")
        pp.write("ty german man who i learned streamlit from :D")


    with right_column:
        st_lottie(lottie_coding, height=300,key= "coding")


#Education
with pp.container():
    pp.write("---")
    left_column, right_column = pp.columns(2)
    with left_column:
        pp.header("Education")
        pp.write("##")
        pp.subheader("Troy High School 2018-2022")
        pp.write("Coursework:")
        pp.subheader("Virginia Polytechnic Institute and State University  2022-2026")
        pp.write("Funny school")



#contine