import streamlit as st
from PIL import Image
image=("infocryptoapp.png")
def st_ui():
    st.title("QR_CODE_GENERATOR_INFOCRYPTO_APP")
    st.caption("Get All The Info Regarding Your Favorite Crypto Currency")
    st.info("Developed by MOHAMED FARHUN M, NANDHAKUMAR S, DHIVAKAR S [Daisi Hackathon]")
    st.header("Scan this Generated QRcode below to redirect into our Infocrypto Tracking Project")
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        st.image("infocryptoapp.png")

    with col3:
        st.write("")
    st.image(image, caption='Live Crypto Tracking App')
    st.balloons()
    

   
if __name__ == "__main__":
    st_ui()

