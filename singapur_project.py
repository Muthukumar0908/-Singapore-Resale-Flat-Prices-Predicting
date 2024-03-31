import streamlit as st
import webbrowser
import pandas as pd
import streamlit_pandas as sp
from PIL import Image
import plotly.express as px


# icon = Image.open(r"C:\Users\ADMIN\Downloads\photo_2023-12-15_22-33-02.jpg")
st.set_page_config(page_title="Singapore Resale Flat Prices Predicting",
                # page_icon= icon,  
                   layout="wide", initial_sidebar_state="auto") 
df=pd.read_csv(r"C:\Users\ADMIN\Videos\capstion_project\singapure\new_singapur.csv").drop(columns="Unnamed: 0")

with st.sidebar:
    st.sidebar.markdown("# :rainbow[Select an option to filter:]")
    selected = st.selectbox("**Menu**", ("Home","analysis","prediction",'data_frame'))
    

if selected== "Home":
    st.markdown('## :green[welcome to Home page]')
    with st.form(key = 'form',clear_on_submit=False):   
        st.markdown('## :blue[Project Title:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Singapore Resale Flat Prices Predicting")
        st.markdown('## :blue[Skills takes away From This project:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Data Wrangling, EDA, Model Building, Model Deployment")
        st.markdown('## :blue[Domain:]')
        st.subheader("&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Real Estate")
        st.markdown('## :blue[Problem:]')
        st.subheader('&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;The objective of this project is to develop a machine learning model and')
        st.subheader(" deploy it as a user-friendly web application that predicts the resale prices of")
        st.subheader('  flats Singapore. This predictive model will be based on historical data of')
        st.subheader(' resale flat transactions, and it aims to assist both potential buyers and')
        st.subheader(' sellers in estimating the resale value of a flat.')

        link="https://github.com/Muthukumar0908/Industrial-Copper-Modeling.git"
        link1='https://www.linkedin.com/in/muthukumar-r-44848416b/'
        colum3,colum4,colum5= st.columns([0.015,0.020,0.1])
        with colum3:
            if st.form_submit_button('GidHub',use_container_width=True):
                webbrowser.open_new_tab(link)
        with colum4:
            if st.form_submit_button("LinkedIn",use_container_width=True):
                webbrowser.open_new_tab(link1)
            
if selected== "data_frame":
    # with st.form(key = 'form',clear_on_submit=False):
        st.markdown("## :green[Filter the Data]")
        @st.cache_data
        def df12():
            df1=pd.read_csv(r"C:\Users\ADMIN\Videos\capstion_project\singapure\ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv")
            return df1
        df7=df12()
        # st.write(df)
        
        create_data={"month":"multiselect",
                    "flat_type":"multiselect",
                    'block':"multiselect",
                    "street_name":"multiselect",
                    "flat_model":'multiselect'}
        
        df1=df7.drop(columns=["storey_range",'floor_area_sqm',"town"])
        # st.write(df1)
        # df1.columns
        all_widgets=sp.create_widgets(df1,create_data)
        try:
            res=sp.filter_df(df1,all_widgets)
            if st.button("submit"):
                st.dataframe(res,use_container_width=True)
        except:
            st.warning("No Data in this filter")
           
if selected=="analysis" :
    with st.form(key = 'form',clear_on_submit=False):
        k=df.head(3)
        st.write(k,use_container_width=True)
        st.write(df.columns)
        
        data=df.groupby(['flat_type']).sum('resale_price').reset_index().sort_values('resale_price',ascending=False).head(20)
        st.markdown("##  &nbsp; :white[Sum if total price in flat_type:]")
        fig=px.area(data,x=data['flat_type'],y=['resale_price'], template="plotly_dark",)
        # fig.show()
        st.plotly_chart(fig,use_container_width=True) 
        
        if st.form_submit_button('px.area'):
            # pass
            st.write(data,use_container_width=True)           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
           
# [theme]
# primaryColor = '#F37F05'
# backgroundColor = '#FEFEFC'
# secondaryBackgroundColor = '#DFDFDB'
# textColor = "#050505"
# font = "sans serif"