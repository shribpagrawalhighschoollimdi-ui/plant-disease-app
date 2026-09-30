import base64
import requests
import streamlit as st

# તમારી જે API Key છે તે અહીં મૂકો (AQ. વાળી કે AIzaSy વાળી બંને ચાલશે)
API_KEY = "AQ.Ab8RN6LeeE8vfjY5vVRm1UPpnLzwVkA..." 

st.set_page_config(
    page_title="SHRI B. P. AGRWAL HIGH SCHOOL, LIMDI",
    page_icon="🌿",
    layout="centered",
)

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

uploaded_file = st.file_uploader(
    "પાંદડાનો ફોટો અપલોડ કરો (JPG, PNG)", type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
  # ઇમેજ પ્રિવ્યૂ
  bytes_data = uploaded_file.getvalue()
  st.image(bytes_data, caption="અપલોડ કરેલ પાંદડું", use_container_width=True)

  if st.button("🔍 રોગ શોધો અને ઉપાય જાણો"):
    with st.spinner("AI દ્વારા પાંદડાનું વિશ્લેષણ થઈ રહ્યું છે..."):
      try:
        # ફોટાને Base64 માં ફેરવવો
        base64_image = base64.b64encode(bytes_data).decode("utf-8")
        mime_type = uploaded_file.type or "image/jpeg"

        prompt_text = (
            "તમે કૃષિ વિજ્ઞાનના શ્રેષ્ઠ નિષ્ણાત (Expert Plant Pathologist) છો. "
            "આ પાંદડાના ફોટાનું બારીકાઈથી અવલોકન કરો અને ગુજરાતીમાં નીચે મુજબ"
            " સ્પષ્ટ મુદ્દાસર માહિતી આપો:\n"
            "૧. વનસ્પતિ / પાકનું નામ\n"
            "૨. રોગનું નામ (અથવા પોષક તત્વની ખામી)\n"
            "૩. મુખ્ય લક્ષણો (Symptoms)\n"
            "૪. સંભવિત કારણો (ફૂગ, જીવાણુ, વાયરસ કે વાતાવરણ)\n"
            "૫. તાત્કાલિક નિવારણ (જૈવિક/ઓર્ગેનિક ઉપાયો અને યોગ્ય રાસાયણિક છંટકાવ"
            " પ્રમાણ સાથે)\n"
            "૬. ભવિષ્ય માટે સાવચેતીના પગલાં"
        )

        # Google Gemini v1beta Direct REST Endpoint
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt_text},
                    {
                        "inline_data": {
                            "mime_type": mime_type,
                            "data": base64_image,
                        }
                    },
                ]
            }]
        }

        headers = {"Content-Type": "application/json"}
        res = requests.post(url, json=payload, headers=headers)
        result = res.json()

        if "candidates" in result:
          answer = result["candidates"][0]["content"]["parts"][0]["text"]
          st.success("✅ વિશ્લેષણ સફળતાપૂર્વક પૂર્ણ થયું!")
          st.markdown(answer)
        elif "error" in result:
          st.error(f"Google API ભૂલ: {result['error'].get('message')}")
        else:
          st.error("માહિતી પ્રોસેસ કરવામાં અસમર્થ. ફરી પ્રયાસ કરો.")

      except Exception as e:
        st.error(f"વિશ્લેષણમાં ભૂલ આવી: {e}")

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #555; font-size: 12px;'>પ્રોજેક્ટ"
    " સૌજન્ય: SHRI B. P. AGRWAL HIGH SCHOOL, LIMDI<br>APP BY DHIRENDRA"
    " PARMAR</div>",
    unsafe_allow_html=True,
)
