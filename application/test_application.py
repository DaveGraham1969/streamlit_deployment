import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

# set page title
st.markdown('# :blue[Dave\'s Dashboard Test - GDP vs Life Expectancy For Selected Year]')
st.markdown('### Markdown text test - exciting times :)')

# initialise "selection" and "df" variables on a global scope
selection = None
df = None


@st.cache_data
def load_data():
    df = pd.read_csv('./application/gapminder_data_graphs.csv')
    return df


if __name__ == '__main__':
    # Call the load_data function and assign the returned df to the df variable
    # store a list of unique years for the selectbox dropdown

    df = load_data()
    unique_years = df['year'].unique()

    # create the selectbox dropdown
    selection = st.selectbox(label='Select year from Dropdown',
                             options=unique_years,
                             help='Choose a Year'
                             )
# create the plot
# make 'year' column in the dataframe the index
df_plot = df[df['year'] == selection]

# # as a test display the data for the selected year on the webpage
# st.write(df_plot)

# create some variables to contain some averages -
average_gdp = round(df_plot['gdp'].mean(), 2)
average_life_exp = round(df_plot['life_exp'].mean(), 2)
average_hdi = round(df_plot['hdi_index'].mean(), 2)

# add three columns to contain the average values
col1, col2, col3 = st.columns([1, 1, 1])  # this will size each column equally on row

# add in three widgets to display the averages
col1.metric(label='Avg GDP', value=average_gdp)
col2.metric(label='Avg Life Expectancy', value=average_life_exp)
col3.metric(label='Avg HDI', value=average_hdi)

# st.markdown(f'### Plot of GDP vs Life expectancy for year {selection}')
st.divider()

# add a scatter plot
title = 'Plot of GDP vs Life expectancy for year {}'.format(selection)
scatter_plot = px.scatter(data_frame=df_plot,
                          x='gdp',
                          y='life_exp',
                          color='continent',
                          title=title
                          )
st.plotly_chart(scatter_plot)

st.divider()

# set up two mini charts under main scatter


# set up 2 columns in next row down
col4, col5 = st.columns(2)

# create boxplot for left column
title = 'Plot of GDP vs Continent for year {}'.format(selection)
box_plot1 = px.box(data_frame=df_plot,
                   title=title,
                   x='continent',
                   y='gdp',
                   color='continent'
                   )

title = 'Plot of CO2 Production vs Continent for year {}'.format(selection)
hist_plot1 = px.histogram(data_frame=df_plot,
                          title=title,
                          x='continent',
                          y='co2_consump',
                          color='continent'
                          )# Split by species, each gets a different color

col4.plotly_chart(box_plot1)
col5.plotly_chart(hist_plot1)