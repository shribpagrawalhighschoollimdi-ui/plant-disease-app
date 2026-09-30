import google.generativeai as genai
from PIL import Image
import streamlit as st

# ૧. API Key કન્ફિગરેશન (તમારી API Key અહીં લખો)
API_KEY = "AQ.Ab8RN6LeeE8vfJy5vVRm1UPpnLzwVkAmGCHJxoPbRvD7wrNwhA"
genai.configure(api_key=API_KEY)

# ૨. પેજ સેટઅપ
st.set_page_config(
    page_title="SHRI B. P. AGRWAL HIGH SCHOOL, LIMDI",
    page_icon="🌿",
    layout="centered",
)

# ૩. શાળા અને નિર્માતા હેડર
st.markdown(
    """
<div style='text-align: center; padding: 16px; background-color: #e8f5e9; border: 2px solid #1b4332; border-radius: 12px; margin-bottom: 20px;'>
    <h2 style='color: #1b4332; margin: 0; font-size: 22px; font-weight: bold;'>🏫 SHRI B. P. AGRWAL HIGH SCHOOL, LIMDI</h2>
    <h4 style='color: #2d6a4f; margin: 6px 0 10px 0; font-size: 16px;'>🌱 AI વનસ્પતિ પર્ણ રોગ નિદાન સોફ્ટવેર</h4>
    <div style='display: inline-block; background-color: #1b4332; color: #ffffff; padding: 5px 15px; border-radius: 15px; font-size: 13px; font-weight: bold;'>
        APP BY DHIRENDRA PARMAR
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.write(
    "પાકના પર્ણ (પાંદડાં) નો સ્પષ્ટ ફોટો અપલોડ કરો અને તુરંત સચોટ વૈજ્ઞાનિક વિશ્લેષણ મેળવો."
)

# ૪. ફોટો અપલોડર
uploaded_file = st.file_uploader(
    "પાંદડાનો ફોટો અપલોડ કરો (JPG, PNG)", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
  img = Image.open(uploaded_file)
  # અહીં use_container_width વાપરવાથી એરર સોલ્વ થઈ જશે
  st.image(img, caption="અપલોડ કરેલ પાંદડું", use_container_width=True)

  if st.button("🔍 રોગ શોધો અને ઉપાય જાણો"):
    with st.spinner("AI દ્વારા પાંદડાનું વિશ્લેષણ થઈ રહ્યું છે..."):
      try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = """
                તમે કૃષિ વિજ્ઞાનના શ્રેષ્ઠ નિષ્ણાત (Expert Plant Pathologist) છો. 
                આ પાંદડાના ફોટાનું બારીકાઈથી અવલોકન કરો અને ગુજરાતીમાં નીચે મુજબ સ્પષ્ટ મુદ્દાસર માહિતી આપો:
                ૧. વનસ્પતિ / પાકનું નામ
                ૨. રોગનું નામ (અથવા પોષક તત્વની ખામી)
                ૩. મુખ્ય લક્ષણો (Symptoms)
                ૪. સંભવિત કારણો (ફૂગ, જીવાણુ, વાયરસ કે વાતાવરણ)
                ૫. તાત્કાલિક નિવારણ (જૈવિક/ઓર્ગેનિક ઉપાયો અને યોગ્ય રાસાયણિક છંટકાવ પ્રમાણ સાથે)
                ૬. ભવિષ્ય માટે સાવચેતીના પગલાં
                """
        response = model.generate_content([prompt, img])
        st.success("✅ વિશ્લેષણ પૂર્ણ થયું!")
        st.markdown(response.text)
      except Exception as e:
        st.error(f"વિશ્લેષણમાં ભૂલ આવી: {e}")

# ૫. ફૂટર
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #555; font-size: 12px;'>પ્રોજેક્ટ"
    " સૌજન્ય: SHRI B. P. AGRWAL HIGH SCHOOL, LIMDI<br>APP BY DHIRENDRA"
    " PARMAR</div>",
    unsafe_allow_html=True,
)
