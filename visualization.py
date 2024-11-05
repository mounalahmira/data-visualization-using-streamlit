import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set the title of the Streamlit app
st.title("Visualization")

# File uploader for users to upload CSV files
file = st.file_uploader("Upload a file",type=["csv"])

# Check if a file has been uploaded
if file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(file)

    # Slider for selecting the number of rows to display
    n_rows = st.slider("Choose number of rows to display",min_value=5,max_value=len(df),step=1)
    # Multiselect widget to choose columns to display
    columns_to_show = st.multiselect("Select columns to show",df.columns.to_list(),default=df.columns.to_list())

    # Select only numerical columns from the DataFrame for plotting
    numerical_columns = df.select_dtypes(include=np.number).columns.to_list()
    # Display the selected rows and columns of the DataFrame
    st.write(df[:n_rows][columns_to_show])

    col1, col2, col3 = st.columns(3)
    with col1:
        # Dropdown menu to select the x-axis column for the scatter plot
        x_column = st.selectbox("Select column on x axis :",numerical_columns)
    with col2:
        # Dropdown menu to select the y-axis column for the scatter plot
        y_column = st.selectbox("Select column on y axis :",numerical_columns)
    with col3:
        color = st.selectbox("Select column to be colored :",df.columns)

    # Create a scatter plot with the selected x and y columns
    fig_scatter = px.scatter(df,x = x_column,y = y_column,color = color)
    # Display the scatter plot in the Streamlit app
    st.plotly_chart(fig_scatter)
