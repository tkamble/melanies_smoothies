# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize your smoothie :cup_with_straw:")
st.write(
    """choose the fruits you want in your custom Smoothie!
    """
)



cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))



ingredients_list = st.multiselect(
   "Choose upto 5 ingredients :"
    ,my_dataframe
)
if ingredients_list : 


    ingredients_string = ''
    for fruit_chosen in ingredients_list : 
        ingredients_string += fruit_chosen + ' '

    st.write(ingredients_string)

    my_insert_stmt = """insert into SMOOTHIES.PUBLIC.ORDERS 
                     values ('""" + ingredients_string + """')"""
    time_to_insert = st.button("Submit Order")
    if time_to_insert :
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
