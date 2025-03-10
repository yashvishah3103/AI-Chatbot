
from dotenv import load_dotenv
import os
import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI

# Load environment variables (API keys, etc.)
load_dotenv()

# Load CSS file
# Load CSS and force reload
with open("style.css","r") as f:
    css = f.read()
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Title & Chat Header
st.markdown('<h1 class="page-title">AI Chatbot</h1>', unsafe_allow_html=True)

st.divider()



# Ensure the assistant's initial message is only added once
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "How can I help you?"}]

# Render initial chat with the assistant's first message
def render_chat():
 chat_html = '<div class="chat-container" id="chatbox">'

 for msg in st.session_state.chat_history:
    if isinstance(msg, dict) and "role" in msg and "content" in msg:
        role_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-ai"
        chat_html += f'<div class="{role_class}">{msg["content"]}</div>'
    else:
        # Handle unstructured string messages
        chat_html += f'<div class="chat-bubble-ai">{msg}</div>'

 chat_html += '</div>'

# Auto-scroll JavaScript
 scroll_script = """
<script>
    var chatbox = document.getElementById("chatbox");
    chatbox.scrollTop = chatbox.scrollHeight;
</script>
"""

 st.markdown(chat_html + scroll_script, unsafe_allow_html=True)
render_chat()
st.divider()

prompt = st.text_input("", placeholder="Type here...")
if st.button("Send", use_container_width=True):
 if prompt.strip():
    
    
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    template = "You are a helpful assistant. Answer this prompt in this way:{user_prompt}"
    prompt_template = PromptTemplate(input_variables=["user_prompt"], template=template)
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)
    response = llm_chain.run(prompt)

    # Store chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.session_state.chat_history.append({"role": "assistant", "content": response})
   
    st.session_state.user_input = ""

st.divider()

# Chat History Display (Inside Scrollable Container)



