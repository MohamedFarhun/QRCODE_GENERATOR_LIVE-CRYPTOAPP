import streamlit as st
from PIL import Image
import time
image=("infocryptoapp.png")
def st_ui(): 
    st.title("QR_CODE_GENERATOR_INFOCRYPTO_APP")
    st.caption(" Get All The Info Regarding Your Favorite Crypto Currency")
    st.info("Developed by MOHAMED FARHUN M, NANDHAKUMAR S, DHIVAKAR S [Daisi Hackathon]", icon="©")
    st.header("Scan this Generated QRcode below to redirect into our Infocrypto Tracking Project")
    with st.spinner('Generating...'):
        time.sleep(3)
    col1, col2, col3 = st.columns([3,6,3])
    with col1:
        st.write("")
    with col2:
        st.image(image, caption='Live Crypto Tracking App')
    with col3:
        st.write("")  
    st.success('QR code generated successfully!', icon= "✅")
with st.sidebar:
    st.image("Bitcoin.jpeg")
    st.header("TEKKYZZ")
    st.write("Leader   : MOHAMED FARHUN M")
    st.write("Member 1 : NANDHAKUMAR S")
    st.write("Member 2 : DHIVAKAR S")
    st.subheader("**_Do you like our Project_?**")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button('Yes'):
            st.write('Thanks for your valuable feedback...')
    with col2:
        if st.button('No'):
            st.write('Will update our app soon...')
            
            
if __name__ == "__main__":
    st_ui()
