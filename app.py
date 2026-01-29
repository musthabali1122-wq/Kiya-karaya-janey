
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
    age = st.selectbox("आयु वर्ग:", ["00-25", "26-40", "41-60", "60+"])

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
    class WomensRightsAndHealth:
    def __init__(self):
        self.context = "भारतीय समाज में संपत्ति और मानसिक स्वास्थ्य का अंतर्संबंध"

    def get_social_challenges(self):
        return {
            "हक छीनने का डर": "रिश्ता टूटने के डर से संपत्ति में हिस्सा न मांगना।",
            "अंधविश्वास": "डिप्रेशन को 'किया-कराया' या 'ऊपरी हवा' समझना।",
            "आर्थिक असुरक्षा": "स्वयं की संपत्ति न होने से भविष्य की चिंता।"
        }

    def legal_reality(self):
        return "Hindu Succession Act: बेटियों का पिता की संपत्ति पर बेटों के बराबर कानूनी अधिकार है।"

    def health_fact(self):
        return "डिप्रेशन एक मेडिकल स्थिति (Chemical Imbalance) है, जादू-टोना नहीं।"

    def solutions(self):
        return [
            "संवाद (Communication): परिवार से स्पष्ट बात करें।",
            "काउंसलिंग: मनोवैज्ञानिक से सलाह लें।",
            "कानूनी जागरूकता: अपने अधिकारों को पहचानें।"
        ]

    def display_report(self):
        print(f"--- {self.context} --- \n")
        print("### सामाजिक और मनोवैज्ञानिक चुनौतियाँ:")
        for key, value in self.get_social_challenges().items():
            print(f"- {key}: {value}")
        
        print("\n### कानूनी हकीकत:")
        print(self.legal_reality())

        print("\n### स्वास्थ्य हकीकत:")
        print(self.health_fact())

   
        print(self.health_fact())
        
        print("\n### समाधान की दिशा:")
        for step in self.solutions():
            print(f"-> {step}")
        
        print("\n" + "="*50)
        print("नोट: संपत्ति से ज्यादा कीमती आपकी मानसिक शांति है।")

# प्रोग्राम को चलाना
report = WomensRightsAndHealth()
report.display_report()

