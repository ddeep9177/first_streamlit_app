import streamlit
import pandas

streamlit.title('I will have healthy dinner')
streamlit.header('todays menu')
streamlit.text('🥣 rice')
streamlit.text('🥗chole')

streamlit.title('Build your own smoothy')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
