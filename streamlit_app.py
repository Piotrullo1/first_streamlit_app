import streamlit
import pandas

streamlit.title('My parents new Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

#pick list so users can pick the fruit they want to include         | filters data based of fruits of customer choice like an example
fruits_selected = streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]



#Display the table on page
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like infromation about?', 'kiwi')
streamlit.write('The user entered', fruit_choice)


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the response and normalize it
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
# output it in screen as a table
streamlit.dataframe(fruityvice_normalize)

import snowflake.connector

