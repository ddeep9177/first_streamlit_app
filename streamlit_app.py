import streamlit
import pandas

streamlit.title('I will have healthy dinner')
streamlit.header('todays menu')
streamlit.text('🥣 rice')
streamlit.text('🥗chole')

streamlit.title('Build your own smoothy')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
