import streamlit as st
import time
import pandas as pd
import plotly.express as px
import numpy as np
st.header("Hello Bros")

#  file uploader to the application
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

file_uploaded = st.file_uploader("Upload Data" ,type=["csv"])



if file_uploaded is not None:
    data = load_data(file_uploaded)

    number_rows = st.slider("Choose Number of Rows To Display",min_value= 5 , max_value=len(data) , step = 5)

    columns_to_show = st.multiselect("Select Columns",data.columns,default=data.columns)

    st.write(data[:number_rows][columns_to_show])

    col1,col2,col3 = st.columns(3)

    numerical_col = data.select_dtypes(include = 'number').columns
    tab1 , tab2 = st.tabs(["ScatterPlot","Histogram"])
    with tab1:
        with col1:
            ys = st.selectbox("Select Columns Y" ,numerical_col)
        with col2:
            xs = st.selectbox("Select Columns X" ,numerical_col) 
        with col3:
            color = st.selectbox("Select Color ",data.columns)
        
        with st.spinner("Processing...",show_time=True):
            time.sleep(1)
            #  scatter plot always work with [ numerical - numerical ]
            figure_Scatter = px.scatter(data , x = xs ,y=ys , color = color)
            st.plotly_chart(figure_Scatter)
    with tab2:
        histogrambox = st.selectbox("Select Column To PLOT" ,numerical_col)
    
        with st.spinner("Processing...",show_time=True):
            time.sleep(1)
            histogram = px.histogram(data , x = histogrambox)
            st.plotly_chart(histogram)
            