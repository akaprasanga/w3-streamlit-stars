#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st



#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('Write title here')
st.write('Descripton of our data')
st.markdown("""---""")
#generate random data for my example dataframe -- howto: https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas
my_dataframe = pd.read_csv("CO2 Emissions_Canada.csv")


# Graph 1:
st.header('Co2 emissions per brand')
Brand_data = my_dataframe.groupby(['Make']).mean()
fig = px.bar(Brand_data, x = Brand_data.index,  y='CO2 Emissions(g/km)', title = "Mean Co2 Emissions by Brand (g/km)", color = "CO2 Emissions(g/km)")
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)
st.markdown("Conclusion of the figure")
st.markdown("""---""")

# #show off a bit of your data. 
# st.header('The Data')
# col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
# col1.dataframe(example_data.head())
# col2.markdown("\n") #add a line of empty space.
# col2.markdown('This is an example _dataframe_ I made up. You can put your teams dataframe here if you want!') #you can add multiple items to each column.
# col2.markdown('- **It is pretty cool that you can use multiple columns in streamlit** (and *markdown* too)!')
# st.markdown("""---""")



#Always good to section out your code for readability.
st.header('Conclusions')
st.markdown('- **Data Science is Fun!**')
st.markdown('- **The [Streamlit Cheatsheet](https://docs.streamlit.io/library/cheatsheet) is really useful.**')
