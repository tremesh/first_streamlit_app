import streamlit
import pandas
streamlit.title (" My First Streamlit App")
streamlit.header ("My Veg Basket")
mylist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(mylist.index))
streamlit.dataframe(mylist)

