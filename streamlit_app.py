import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 🥗 🐔 🥑🍞Teasty & Healthy Fresh Tomato, Onion, Beens Upma with Nuts')
streamlit.text('🥣 🥗 🐔 🥑🍞Fresh Hot Tea')
streamlit.text('XYZ yyyy zzzzz aaaaaajdewdewdFresh Hot Tea')
streamlit.header('🥣 🥗 🐔 🥑🍞 End of Meny🥣 🥗 🐔 🥑🍞')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
