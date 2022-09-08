import streamlit as st
from PIL import Image
import time
image=("infocryptoapp.png")
def st_ui():
    st.balloons()   
    st.title("QR_CODE_GENERATOR_INFOCRYPTO_APP")
    st.caption("Get All The Info Regarding Your Favorite Crypto Currency")
    st.info("Developed by MOHAMED FARHUN M, NANDHAKUMAR S, DHIVAKAR S [Daisi Hackathon]", icon="©")
    st.header("Scan this Generated QRcode below to redirect into our Infocrypto Tracking Project")
    
    if st.button('Generate'):
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        col1, col2, col3 = st.columns([3,6,3])
        with col1:
            st.write("")
        with col2:
            st.image(image, caption='Live Crypto Tracking App')
        with col3:
            st.write("")        
     else:
         break:
 
   
if __name__ == "__main__":
    st_ui()

