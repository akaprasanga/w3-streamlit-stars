#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st



#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('CO2 Emissions and Fuel Consumption By Vehicle Class and Model in Canada EDA')

st.header('Masterminds behind this project: The Streamlit Stars')
st.write('Cash Popik: I am from Alberta, Canada, I enjoy playing piano and learning about computer science.')
st.write('Yunah Chung: I am from Los Angeles, California. I really like to go outside and take hikes and walks. I also love to learn about anything STEM related.')
st.write('Isaac Jung: Hello, I am from Los Angeles, California. I like reading books and swimming. I also enjoy playing the cello and solving math problems.')
st.write('Prasanga Neupane: Hi I am instructor of this group and I am from Louisiana. I love to travel and play guitar.')

st.markdown("""---""")
st.header('Our Dataset:')
st.write('An analysis comparing the effects of car brand, vehicle class, fuel type, and engine type on carbon dioxide emissions. The data was taken by the Canadian government over a 7 year period.')
#generate random data for my example dataframe -- howto: https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas
my_dataframe = pd.read_csv("CO2 Emissions_Canada.csv")
st.write(my_dataframe)


# Graph 1:
st.header('Co2 Emissions By Brand')
Brand_data = my_dataframe.groupby(['Make']).mean()
fig = px.bar(Brand_data, x = Brand_data.index,  y='CO2 Emissions(g/km)', title = "Mean Co2 Emissions by Brand (g/km)", color = "CO2 Emissions(g/km)")
#fig.update_traces(line_color='red')
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)
st.markdown("Conclusion: Luxury brand cars such as Bugatti and Lamborghini are much higher in Co2 emissions, and compact-car brands such as Honda or Smart create much smaller Co2 emissions due to their weaker, lighter cars.")
st.markdown("""---""")

# Graph 2: Mean CO2 Emissions per Vehicle Class 
st.header('Mean CO2 Emissions by Vehicle Class')
means = my_dataframe.groupby("Vehicle Class").mean()
vclass = px.bar(means, y = "CO2 Emissions(g/km)", title = "Mean Emissions per Vehicle Class", color = "CO2 Emissions(g/km)")
vclass.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
#vclass.update_traces(line_color='green')
st.plotly_chart(vclass)
st.markdown('Conclusion: Passenger and Cargo Vans have the highest environmental impact in terms of CO2 emissions, while Station Wagons and Compact vehicles have the lowest impact.')
st.markdown("""---""")

# Graph 3:
st.header('Fuel type vs carbon emissions ')
rename_mydataframe = my_dataframe.replace({ 'Fuel Type': { 'Z': 'Premium Gasoline', 'D': 'Diesel','X': 'Regular Gasoline','E': 'Ethanol (E85)', 'N': 'Natural gas'}})
fig = px.box(rename_mydataframe, x="Fuel Type", y="CO2 Emissions(g/km)")
st.plotly_chart(fig)
st.markdown("Conclusion: Diesel Gas is very consistent with its range of carbon emissions. Other fuels such as premium or regular gasoline have outliers which greatly exceed the expected range even though their median is very close to Diesel.")
st.markdown("""---""")


#Graph 4:
st.header('Car brand vs vehicle class (carbon emissions) ')
fig = px.scatter(my_dataframe, x='Make', y='Vehicle Class', color='Vehicle Class', size='CO2 Emissions(g/km)')
st.plotly_chart(fig)
st.markdown("Conclusion: The two seater cars have the highest carbon dioxide emissions rate than other vehicle classes. When comparing car brands, it can also be seen that Buggatti and Rolls Royce have much higher carbon dioxide emissions than brands such as Smart or Acura.")
st.markdown("""---""")


#Graph 5:
st.header("Fuel Type's Effect On Fuel Consumption (Combined)")
Fuel_Data = my_dataframe.groupby(['Fuel Type']).mean()
Fuel_data = Fuel_Data.rename(index={'D':"Diesel", 'E':"Ethanol (E85)","N":"Natural Gas","X":"Regular","Z":"Premium"})
st.write(Fuel_data)
fig = px.pie(Fuel_data, values='Fuel Consumption Comb (L/100 km)', names = Fuel_data.index, title = "Fuel Type's Effect on Fuel Consumption (Combined)" )
st.plotly_chart(fig)
st.markdown("Conclusion: Diesel is the most efficient of the fuels provided, with ethanol being the least efficient. Regular is more efficient than premium.")
st.markdown("""---""")

#Graph 6:
st.header("Transmission Effect On Mean Fuel Consumption (Combined)")
Transmission_data = my_dataframe.groupby(['Transmission']).mean()
fig = px.bar(Transmission_data, x = Transmission_data.index,  y='Fuel Consumption Comb (L/100 km)', title = "Mean Fuel Consumption (Combined) By Transmission")
# sorting required here
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)
st.markdown("Conclusion: The AM5 engine is the most efficient with the A4 engine being the least efficient, this implies that on average A4 cars will be less fuel-efficient. Manual cars tend to fall in the middle, often being more efficient than automatic.")
st.markdown("""---""")

#Graph 7: 
st.header('Engine Size Effect On Fuel Consumption (Combined)')
Engine_Data = my_dataframe.groupby(['Engine Size(L)']).mean()
fig = px.line(Engine_Data, x= Engine_Data.index, y="Fuel Consumption Comb (L/100 km)", title='Engine Size Effect On Fuel Consumption (Combined)' )
st.plotly_chart(fig)
st.markdown("Conclusion: Engine size peaks fuel consumption at 8 L, lower engine size generally results in less fuel consumption")
st.markdown("""---""")

#Graph 8:
st.header('Engine Size and Cylinders to Carbon Emissions and Fuel Consumption Correlation')
fig = my_dataframe[['Engine Size(L)', 'Cylinders', 'Fuel Consumption City (L/100 km)', 'Fuel Consumption Hwy (L/100 km)', 'Fuel Consumption Comb (L/100 km)', 'CO2 Emissions(g/km)']]
vals = fig.corr()
dat = px.imshow(vals, text_auto = True)
st.plotly_chart(dat)
st.markdown('Conclusion (from this heatmap): CO2 Emissions has its highest correleation with Fuel Consumption By City (L/100km). Engine Size highly correlates with CO2 Emissions')
st.markdown("""---""")

#Graph 9:
st.header("AI Prediction of Co2 Emissions Per Vehicle")
st.write('Description: For this graph, we utilized linear regression to predict CO2 Emission using four basic properties of a car such as engine size, cylinders, fuel consumption in the highway and city. With this, we used 80-20 train and test split to train and shown below is the final predictions of total CO2 emissions compared to the actual value.')
predicted_df = pd.read_csv("Regression_prediction.csv")
smaller_pred = predicted_df.head(100).sort_values(["Actual Values"], ignore_index=True)
fig = px.line(smaller_pred,x = smaller_pred.index, y=["Actual Values", "Predicted Values"], title = "AI Prediction of Co2 Emissions Per Vehicle")
fig.update_layout(yaxis_title='Predicted CO2 Emissions(g/km)', xaxis_title='Individual Vehicle')
st.plotly_chart(fig)

st.header("Conclusion")
st.write('These graphs demonstrate the correlation between a variety of factors. We compared how car brands, vehicles classes, and fuel types affect the emission of carbon dioxide. In addition, there is a comparision of fuel consumption based on fuel type, transmission of fuel, and engine size. We also made a heat map to combine the correlations between each of the factors. Finally, there is the AI model, which predicts the carbon emissions based on the factors of engine size, the number of cylinder, and fuel consumption on city streets and the highway. However, it should be noted that there are spikes in the predicted values which do not align with the actual values, which could indicate that other factors such as vehicle class or car brand are also playing a role.')

# #show off a bit of your data. 
# st.header('The Data')
# col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
# col1.dataframe(example_data.head())
# col2.markdown("\n") #add a line of empty space.
# col2.markdown('This is an example _dataframe_ I made up. You can put your teams dataframe here if you want!') #you can add multiple items to each column.
# col2.markdown('- **It is pretty cool that you can use multiple columns in streamlit** (and *markdown* too)!')
# st.markdown("""---""")



