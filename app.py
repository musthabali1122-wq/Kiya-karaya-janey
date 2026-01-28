
import streamlit as st

# 1. पेज की सेटिंग
st.set_page_config(page_title="किया कराया पहचाने", page_icon="✨", layout="centered")

# 2. सुधारा हुआ CSS (Gemini Look)
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f4f9;
    }
    .main-title {
        font-family: 'Google Sans', sans-serif;
        color: #1a73e8;
        font-size: 40px;
        font-weight: 600;
        text-align: center;
        padding-bottom: 20px;
    }
    div.stButton > button {
        background-color: #1a73e8;
        color: white;
        border-radius: 50px;
        padding: 10px 30px;
        border: none;
        font-weight: bold;
    }
    /* कार्ड जैसा कंटेनर */
    .css-1r6slb0 {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. साइडबार
with st.sidebar:
    st.markdown("<h2 style='color: #1a73e8;'>✨ मेनू</h2>", unsafe_allow_html=True)
    st.write("यह ऐप आपकी समस्या को समझने में मदद करता है।")
    st.markdown("---")
    st.write("डेवलपर: **आपका नाम**")

# 4. मुख्य इंटरफेस
st.markdown("<h1 class='main-title'>✨ किया कराया पहचाने</h1>", unsafe_allow_html=True)

# इनपुट फील्ड्स
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("लिंग चुनें:", ["महिला (Female)", "पुरुष (Male)"], horizontal=True)
with col2:
    age = st.selectbox("आयु वर्ग:", ["15-25", "26-40", "41-60", "60+"])

symptoms = st.multiselect(
    "लक्षण चुनें:",
    ["अचानक स्वभाव बदलना", "काम में मन न लगना", "भारीपन महसूस होना", "नींद की समस्या", "लगातार तनाव"]
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("गहराई से विश्लेषण करें"):
    with st.spinner('Gemini AI विश्लेषण कर रहा है...'):
        st.balloons()
        st.success("विश्लेषण सफल रहा! यहाँ आपके परिणाम हैं...")

st.markdown("---")
st.warning("⚠️ अस्वीकरण: यह ऐप केवल सामान्य जानकारी के लिए है।")
