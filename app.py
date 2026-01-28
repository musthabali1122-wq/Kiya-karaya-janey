import streamlit as st

# पेज की सेटिंग और टाइटल
st.set_page_config(page_title="किया कराया पहचाने", page_icon="✨", layout="centered")

# --- CUSTOM CSS (Gemini Look-alike) ---
st.markdown("""
    <style>
    /* बैकग्राउंड और फॉन्ट */
    .stApp {
        background-color: #f8faff;
    }
    
    /* टाइटल को स्टाइलिश बनाना */
    .main-title {
        font-family: 'Google Sans', sans-serif;
        color: #1a73e8;
        font-size: 42px;
        font-weight: 600;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* कार्ड जैसा लुक */
    div.stButton > button {
        background-color: #1a73e8;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        border: none;
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background-color: #1557b0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* साइडबार को मॉडर्न बनाना */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_safe_area=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #1a73e8;'>✨ ऐप मेनू</h2>", unsafe_allow_safe_area=True)
    st.info("यह ऐप उन्नत तार्किक विश्लेषण पर आधारित है।")
    st.write("डेवलपर: **[आपका नाम]**")

# --- MAIN INTERFACE ---
st.markdown("<h1 class='main-title'>✨ किया कराया पहचाने</h1>", unsafe_allow_safe_area=True)

# इनपुट बॉक्स के लिए कंटेनर
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.radio("लिंग चुनें:", ["महिला (Female)", "पुरुष (Male)"], horizontal=True)
    
    with col2:
        age = st.selectbox("आपकी आयु:", ["15-25", "26-40", "41-60", "60+"])

    symptoms = st.multiselect(
        "लक्षण चुनें (जो आप महसूस कर रहे हैं):",
        ["अचानक स्वभाव बदलना", "काम में मन न लगना", "भारीपन महसूस होना", "नींद की समस्या", "लगातार तनाव"]
    )

    st.markdown("<br>", unsafe_allow_safe_area=True)
    
    # विश्लेषण बटन
    if st.button("गहराई से विश्लेषण करें"):
        with st.spinner('Gemini की तरह विश्लेषण किया जा रहा है...'):
            st.success("विश्लेषण पूर्ण! आपकी जानकारी प्रोसेस की जा रही है।")
            # यहाँ आपका लॉजिक आएगा

# --- FOOTER / DISCLAIMER ---
st.markdown("---")
st.caption("⚠️ **सावधानी:** यह केवल शैक्षणिक उद्देश्य के लिए है। किसी भी गंभीर स्थिति में विशेषज्ञ की सलाह अवश्य लें।")
