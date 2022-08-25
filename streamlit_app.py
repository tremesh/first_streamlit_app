import streamlit
import pandas
streamlit.title (" My First Streamlit App")
mylist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(mylist)

