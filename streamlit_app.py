import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 🥗 🐔 🥑🍞Teasty & Healthy Fresh Tomato, Onion, Beens Upma with Nuts')
streamlit.text('🥣 🥗 🐔 🥑🍞Fresh Hot Tea')
streamlit.text('XYZ yyyy zzzzz aaaaaajdewdewdFresh Hot Tea')
streamlit.header('🥣 🥗 🐔 🥑🍞 End of Meny🥣 🥗 🐔 🥑🍞')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
