import streamlit as st
from awslib import s3_contents
from textlib import droplines
from linelib import simple_recorder 
##############################################
st.set_page_config(layout="wide")
#fuente = st.selectbox('Choose Mode/Elija modo', ('CETRAM', 'inglés'))
#tab1, tab2 = st.tabs(['Grabación','Revisión'])
#with tab1:
if True:
    st.title('👨‍⚕️CETRAM QuantMed LLM Doctor🤖')
    for dropline in droplines(fuente):
        st.write(dropline+chr(10))
    simple_recorder(fuente)
#with tab2:
else:
    st.header('Contents of cetram-felix/AUDIO')
    contents = s3_contents()  
    st.table(contents)
