import streamlit
import pandas
streamlit.title (" My First Streamlit App")
streamlit.header ("My Veg Basket")
mylist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
mylist = mylist.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(mylist.index),['Avocado','Strawberries','Lime'])
streamlit.dataframe(mylist)



