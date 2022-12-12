import streamlit as st
import docstring_creation as dc
st.title("Docstring generator for python")
st.subheader("Using OpenAI")
with st.form("input_def"):
    st.warning("Make Sure there are no empty lines above and below the function")
    input_def_txt = st.text_area('Enter the fucntion for which you want the Doc String')
    python_version = st.selectbox("Choose Python Version",('3.7','3.8','3.9'),index=0)
    submit_function = st.form_submit_button("Submit Function")

if submit_function:
    with open('input_def.txt','w') as file:
        file.write(input_def_txt)
    with st.spinner('Creating Doc String:'):
        function_as_string = dc.write_function_as_string('input_def.txt',python_version=python_version)
        dc.create_docstring(function_as_string=function_as_string)
    st.success('Docstring Sucessfully Created!', icon="✅")
    with open('docstring.txt','r') as file:
        docstring = file.read()
    st.download_button('Download Docstring',\
        data = docstring,help="Downlaod Docstring as a Text File",file_name='DocString.txt')
    
        