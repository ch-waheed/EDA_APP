import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns
import numpy

# webapp title
st.markdown('''
#  **Exploratory Data Analysis web application**
            This app developed by  waheed champ''')

# how to upload a file from pc

with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file " , type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://health.data.ny.gov/Health/New-York-State-Statewide-COVID-19-Testing/xdss-u53e/data)")

# profling report for pandas

if uploaded_file is not None:
    @st.cache

    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df , explorative=True)
    st.header("**Input DF**")
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info("Awaiting for csv file , upload your data")
    if st.button('Press to use example data') :
       
    # example data

       def load_data():
           a = pd.DataFrame( np.random.rand(100,5),
                columns = ['age', 'champ', 'banana', 'Ear', ' Deutchland'])
           return a
       df = load_data()
       pr = ProfileReport(df , explorative=True)
    st.header("**Input DF**")
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report()