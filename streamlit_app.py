import streamlit
import pandas

streamlit.title (" My First Streamlit App")
streamlit.header('Break Fast Menu')
streamlit.text ('3 Idli with Chutney and Sambar')
streamlit.text('A glass of Apple juice')
streamlit.header('Build our Own Menu')
my_fruit_list=pandas.read_cvs("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
