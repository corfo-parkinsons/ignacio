import streamlit as st
from awslib import s3_contents
from textlib import droplines
from linelib import simple_recorder # was linetabs
from datetime import datetime
##############################################
st.set_page_config(layout="wide")
fecha = datetime.now().strftime('%Y-%m-%d')

tab1, tab2 = st.tabs(['Grabación','Revisión'])
with tab1:
    st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
    for dropline in droplines:
        st.write(dropline)
    ############################
    # FUTURE: https://blog.streamlit.io/how-to-build-the-streamlit-webrtc-component/   
    simple_recorder()
with tab2:
    st.header('Contents of cetram-felix/AUDIO')
    contents = s3_contents()  
    st.table(contents)
