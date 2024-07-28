import streamlit as st
import pdfplumber
import docx2txt
import openai
import numpy as np
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
# Initialize the Groq client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

# Function to get embeddings using OpenAI API
def get_embeddings(text):
    client = openai.OpenAI()
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    embeddings = response.data[0].embedding
    return np.array(embeddings)

# Function to parse PDF files
def parse_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to parse DOCX files
def parse_docx(file):
    text = docx2txt.process(file)
    return text

# Function to handle file upload and parsing
def handle_file_upload(file, file_type):
    if file_type == 'pdf':
        return parse_pdf(file)
    elif file_type == 'docx':
        return parse_docx(file)
    elif file_type == 'txt':
        return file.read().decode('utf-8')
    else:
        return ""

# Function to get chat completions from Groq
def get_groq_response(messages):
    completion = groq_client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=messages,
        temperature=0.5,
        max_tokens=400,
        top_p=1,
        stream=True,
        stop=None,
    )
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response

# Main Streamlit app
def main():
    st.set_page_config(page_title="PerfectCandidate", page_icon=":rocket:", 
                       layout="wide")

    col1, col2 = st.columns((0.7,0.3))

    with col1:

        st.title("🚀 Asistente PerfectCandidate! 🚀")
    with col2:
        st.image("./img/bot.png")
    
    # File uploads
    cv_file = st.sidebar.file_uploader("Upload your CV (mandatory)", type=['pdf', 'docx', 'txt'])
    rec_letter_file = st.sidebar.file_uploader("Upload your Recommendation Letter (optional)", type=['pdf', 'docx', 'txt'])
    interests_file = st.sidebar.file_uploader("Upload your Personal Interests Document (optional)", type=['pdf', 'docx', 'txt'])
    job_desc_file = st.sidebar.file_uploader("Upload the Job Description (optional)", type=['pdf', 'docx', 'txt'])

    # Parsing the uploaded files
    if cv_file:
        cv_text = handle_file_upload(cv_file, cv_file.name.split('.')[-1])
        cv_embeddings = get_embeddings(cv_text)
    else:
        st.error("***Se debe introducir al menos el CV del candidato***")
        return

    rec_letter_text = handle_file_upload(rec_letter_file, rec_letter_file.name.split('.')[-1]) if rec_letter_file else "No info disponible"
    interests_text = handle_file_upload(interests_file, interests_file.name.split('.')[-1]) if interests_file else "No info disponible"
    job_desc_text = handle_file_upload(job_desc_file, job_desc_file.name.split('.')[-1]) if job_desc_file else "No info disponible"

    # Session state to store conversation history
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Chat input and message display
    input_text = st.chat_input("Pregunta lo que quieras respecto al candidato:")
    if input_text:
        user_message = {"role": "user", "content": input_text}
        st.session_state.messages.append(user_message)

        # Construct the context for the Groq model
        context = """Eres un experto asistente que ayudas a los reclutadores a ver el potencial
                    en el candidato del CV adjunto. Con la informacion aportada, 
                    ayudarás a los reclutadores a entender las cualidades de los candidatos
                    y su potencial para el puesto en caso de conocer este. En caso de no conocer el rol
                    al que postula, simplemente se valorarán sus competencias para cualquier puesto en general.
                    Sé conciso, riguroso, equitativo y constructivo en tu feedback.
                    """
        if cv_text:
            context += "\n\nCV:\n" + cv_text
        if rec_letter_text:
            context += "\n\nLetra de recomendacion:\n" + rec_letter_text
        if interests_text:
            context += "\n\nIntereses personales:\n" + interests_text
        if job_desc_text:
            context += "\n\nDescripcion del puesto al que postula:\n" + job_desc_text

        # Add the context to the messages
        messages_with_context = st.session_state.messages.copy()
        messages_with_context.insert(0, {"role": "system", "content": context})

        # Get the response from Groq
        response = get_groq_response(messages_with_context)
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Display conversation
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            st.chat_message("user").markdown(msg['content'])
        else:
            st.chat_message("assistant").markdown(msg['content'])

# Run the app
if __name__ == "__main__":
    main()
