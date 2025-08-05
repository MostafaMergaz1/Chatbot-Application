import streamlit as st
import google.generativeai as genai
st.set_page_config(page_title="💬 Gemini AI Chat", page_icon="🤖", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Google AI Text Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Powered by <strong>Gemini 2.5 Pro</strong> | Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
st.divider()
api="AIzaSyBAmZtz2NZNE15MWeDzihUX72WHbMdjEc8"
# shure from API FIND
if api:
    genai.configure(api_key = api)
else:
    st.error('Your API Key is Not Found.')

# function Text
def Generate_Text(prompt):
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    return response.text


# عملية تخزين المحادثة

if "messages" not in st.session_state:
    st.session_state.messages = []

#عرض المحادثات السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):#role : user / assistant
        st.markdown(message["content"]) #content : user_input / response from model(رد المودل)

# المستخدم

if user_input := st.chat_input("💬 Please enter your message..."):

    # عرض رسالة المستخدم
    with st.chat_message("user"):
        st.markdown(user_input)
    # حفظ رسالة المستخدم
    st.session_state.messages.append({'role':'user','content':user_input})
    # الرد من Gemini
    with st.chat_message("assistant"):
        message_placeholder=st.empty()
        with st.spinner("🤔 Thinking..."):
            response_text=Generate_Text(user_input)
            message_placeholder.markdown(response_text)
    # حفظ رد المساعد
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    
    
    
