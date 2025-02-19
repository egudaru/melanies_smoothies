# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Example Streamlit App :cup_with_straw:")
st.write(
    """Choose the fruits you want in your custum Smoothie!
    """)
title=st.text_input('Movie title','Life of Brian')
st.write('The movie title is ',title)

#option = st.selectbox(
#    "What is your favorite fruit?",
#   ("Banana","Strawberries","Peaches"))

#st.write("Your favourite fruit is:", option)
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect(
    'Choose up to 5 ingredients:',my_dataframe
)
if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string=''

    for fruit_chosen in ingredients_list:
     ingredients_string +=fruit_chosen+' '
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,NAME_ON_ORDER)
            values ('""" + ingredients_string + """','"""+title+"""')"""
#    st.write(my_insert_stmt)
#    st.stop()
    time_to_insert=st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered! '+ title, icon="✅")
