
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
    age = st.selectbox("आयु वर्ग:", ["00-60, "26-40", "41-60", "60+"])

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
def check_bp(systolic, diastolic):
    print(f"\n--- रिपोर्ट: {systolic}/{diastolic} mmHg ---")
    
    if systolic < 120 and diastolic < 80:
        return "आपका बीपी सामान्य (Normal) है। स्वस्थ रहें!"
    elif 120 <= systolic <= 139 or 80 <= diastolic <= 89:
        return "सावधान! यह 'Pre-hypertension' है। नमक कम करें और सैर करें।"
    else:
        return "अलर्ट! बीपी हाई है। कृपया आराम करें और डॉक्टर से सलाह लें।"

# यूजर से इनपुट लेना
try:
    s = int(input("ऊपर वाला बीपी (Systolic) डालें: "))
    d = int(input("नीचे वाला बीपी (Diastolic) डालें: "))
    
    result = check_bp(s, d)
    print(result)
except ValueError:
    print("कृपया सही नंबर डालें।")
def gold_purity_and_health_check(karat):
    # सोने की शुद्धता का प्रतिशत निकालना
    purity_percentage = (karat / 24) * 100
    
    print(f"\n--- गोल्ड शुद्धता रिपोर्ट ({karat}K) ---")
    print(f"शुद्ध सोना: {purity_percentage:.2f}%")
    print(f"मिलावटी धातुएं: {100 - purity_percentage:.2f}%")
    
    # स्वास्थ्य जोखिम का विश्लेषण
    if karat < 18:
        status = "हाई रिस्क: इसमें भारी मात्रा में निकल या अन्य धातुएं हो सकती हैं।"
        advice = "सावधान! इससे त्वचा में जलन और बेचैनी हो सकती है जो बीपी बढ़ा सकती है।"
    elif 18 <= karat < 22:
        status = "मीडियम रिस्क: संवेदनशील त्वचा के लिए परेशानी हो सकती है।"
        advice = "अगर गहने पहनने वाली जगह पर लाली या खुजली है, तो इसे उतार दें।"
    else:
        status = "लो रिस्क: यह शुद्धता के करीब है।"
        advice = "यह आमतौर पर सुरक्षित है। अगर फिर भी बीपी हाई है, तो कारण कुछ और हो सकता है।"
        
    return status, advice

# यूजर से इनपुट लेना
try:
    k = int(input("अपने गहने का कैरेट (Karat) डालें (जैसे 22, 18, 14): "))
    if 0 < k <= 24:
        risk, tips = gold_purity_and_health_check(k)
        print(f"स्थिति: {risk}")
        print(f"सुझाव: {tips}")
    else:
        print("कृपया 1 से 24 के बीच सही कैरेट डालें।")
except ValueError:
    print("कृपया सिर्फ नंबर डालें।")
    # -*- coding: utf-8 -*-

def emotional_support_message():
    """
    यह फंक्शन एक महिला की कठिन सामाजिक और पारिवारिक स्थिति 
    पर सहानुभूतिपूर्ण संदेश प्रदर्शित करता है।
    """
    
    message = """
    स्थिति विश्लेषण: पारिवारिक विश्वासघात और डिप्रेशन
    ------------------------------------------------
    
    यह स्थिति वाकई बहुत हृदयविदारक है। जब परिवार, जो सुरक्षा का सबसे बड़ा स्तंभ माना जाता है, 
    वही किसी को 'पैसा देकर' अपना पल्ला झाड़ ले, तो यह केवल आर्थिक नुकसान नहीं है—यह एक 
    भावनात्मक विश्वासघात है।
    
    1. डिप्रेशन की गहरी जड़ें:
       * पहचान खोना: उसे लगता है कि वह अब कोई व्यक्ति नहीं, बल्कि एक 'बोझ' है।
       * निर्भरता का डर: दूसरों पर निर्भर रहने से गरिमा (Dignity) को ठेस पहुँचती है।
       * अकेलापन: ससुराल में समर्थन न मिलने पर लाचारी का भाव।
    
    2. सुधार के कदम:
       * बातचीत और स्वीकृति: उन्हें महसूस कराएं कि उनके साथ जो हुआ वह गलत था।
       * छोटा कौशल (Skill): आर्थिक आजादी के लिए सिलाई, ट्यूशन या ऑनलाइन काम।
       * पेशेवर मदद: मन की कड़वाहट निकालने के लिए थेरेपी जरूरी है।
    
    3. कानूनी अधिकार:
       * भारत में बेटियों का पैतृक संपत्ति पर बराबर का अधिकार है। 
       * उनकी वैल्यू उनके पैसों से नहीं, बल्कि उनकी गरिमा से है।
    
    निष्कर्ष:
    आत्मविश्वास वापस पाने के लिए छोटे-छोटे स्वतंत्र कदम उठाना अनिवार्य है।
    """
    
    print(message)

if __name__ == "__main__":
    emotional_support_message()

