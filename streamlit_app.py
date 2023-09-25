import snowflake.connector
import streamlit
import pandas
import requests
streamlit.title('    My parent new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🍞Idly')
streamlit.text('🥣Kale, Spinach & Rocket Smoothie')
streamlit.text('🥗Omega 3 & Blackberry Oatmeal')
streamlit.text('🥑 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

##After pulling the data into a pandas dataframe called my_fruit_list, we will ask the streamlit library to display it on the page by typing:
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')


try:
  
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
      streamlit.error('Please select a fruit to get information")
  else: 
      streamlit.write('The user entered ', fruit_choice)
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
      #streamlit.text(fruityvice_response.json())
      # write your own comment -what does the next line do? 
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      # write your own comment - what does this do?
      streamlit.dataframe(fruityvice_normalized)

except URLERROR as e:
  streamlit.error()
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")

my_data_rows = my_cur.fetchall()
streamlit.text("fruit load list contains")
streamlit.text(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like you like to add?','Jackfruit')
streamlit.write('The user entered ', add_my_fruit)


my_cur.execute("insert into fruit_load_list values('from streamlit')");
