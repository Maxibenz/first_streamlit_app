import streamlit
streamlit.title('    My parent new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞Idly')
streamlit.text('🥣Kale, Spinach & Rocket Smoothie')
streamlit.text('🥗Omega 3 & Blackberry Oatmeal')
streamlit.text('🥑 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

##After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:

my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
