import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

# Check for API key first
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OpenAI API key not found! Please add your OpenAI API key to your .env file and reload the page.")
    st.code("OPENAI_API_KEY=your_api_key_here")
    st.stop()

client = OpenAI(api_key=api_key)

st.title("Hire Tamzeed Chatbot")
st.write("""
         Interactive chatbot to ask about Tamzeed's skills and experiences. 
         The model has been fed my resume and some context about the position and the tech challenge. 
         The chatbot is set to use the GPT-3.5-turbo model using the OpenAI API to generate responses.
         """)
st.markdown("---")

# Init session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "resume" not in st.session_state:
    with open("model_context/Tamzeed_Quazi_Resume.txt", "r") as f:
        st.session_state.resume = f.read()

if "job_context" not in st.session_state:
    with open("model_context/Job_Context.txt", "r") as f:
        st.session_state.job_context = f.read()
if "initial_pitch_shown" not in st.session_state:
    st.session_state.initial_pitch_shown = False

# Prompt for the chatbot
system_prompt = f"""You are a specialized chatbot speaking to Dr. Lence and her team representing Tamzeed Quazi for a job application. 

Resume Information:
{st.session_state.resume}

Job Context:
{st.session_state.job_context}

Your role is to:
1. Highlight Tamzeed's relevant skills and experiences
2. Answer questions about his background professionally
3. Demonstrate why he's a great fit for this position
4. Be conversational but professional
5. Use specific examples from his resume when possible
6. Highlight his interest in machine learning and AI when appropriate

Always respond as if you're representing Tamzeed's best interests for this job opportunity."""

# Generate and display initial pitch
if not st.session_state.initial_pitch_shown:
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            pitch_prompt = "Please provide a compelling 2-3 sentence pitch about why Tamzeed would be perfect for this job based on his resume and the job context. Be specific and highlight key strengths."
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": pitch_prompt}
                ],
                temperature=0.7,
                stream=True
            )
            
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            st.session_state.initial_pitch_shown = True
            
        except Exception as e:
            st.error(f"Error generating pitch: {str(e)}")

# Display chat history
for i, message in enumerate(st.session_state.messages):
    if i == 0 and st.session_state.initial_pitch_shown:
        continue  
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat
if prompt := st.chat_input("Ask about Tamzeed..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # generate AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            messages = [{"role": "system", "content": system_prompt}]
            messages.extend(st.session_state.messages)
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                stream=True
            )
            
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error: {str(e)}")