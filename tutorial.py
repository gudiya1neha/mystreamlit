import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','FillForm','Download'))
st.image('https://onleitechnologies.com/wp-content/uploads/elementor/thumbs/cropped-Untitled_design__6_-removebg-preview-1-phm0gqnlwf776pdkuo8k2oko4zo2mskrgrrms3qitk.png')
st.title('Onlei Technologies')
st.header('By Neha Yadav')
st.text('This is atutorial on Streamlit Library')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=p7raJky2P4k')
elif(mymenu=='FillForm'):
    with st.form('My Form'):
        name=st.text_input('Enter Name')
        dob=st.date_input("Choose Date of Birth")
        marks=st.slider('Choose Marks')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
elif(mymenu=='Download'):
    st.header("Downloads")
    st.download_button('Download Now','hello this is the download data','onlei.txt')
    
