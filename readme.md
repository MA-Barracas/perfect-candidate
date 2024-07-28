# 🚀 PerfectCandidate - AI Recruitment Assistant

Welcome to **PerfectCandidate**, your AI-powered assistant designed to help recruiters evaluate candidates for various positions. This application leverages state-of-the-art AI models to analyze candidate information and provide insightful feedback. 

## Features ✨

- **Upload and Parse Documents**: Easily upload CVs, recommendation letters, personal interest documents, and job descriptions in PDF, DOCX, or TXT formats.
- **AI-Powered Analysis**: Uses advanced embeddings and natural language processing to evaluate candidate information.
- **Interactive Chat**: Ask questions about candidates and receive detailed, AI-generated responses to assist in the recruitment process.
- **Multi-Document Support**: Analyze multiple documents for a comprehensive candidate evaluation.

## Getting Started 🚀

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- Streamlit
- pdfplumber
- docx2txt
- openai
- groq
- dotenv
- numpy

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/perfectcandidate.git
    cd perfectcandidate
    ```

2. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables**

    Create a `.env` file in the root directory of your project and add your API keys:

    ```plaintext
    GROQ_API_KEY=your_groq_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

### Running the Application

To start the application, run the following command:

```bash
streamlit run app.py
```

## Usage 🛠️

1. **Upload Documents**: Use the sidebar to upload your CV, recommendation letter, personal interests document, and job description.
2. **Interact with the Chatbot**: Type your questions in the chat input field and receive insightful responses about the candidate's suitability for the role.

## How It Works 🔍

- **File Upload and Parsing**: The application supports uploading and parsing of PDF, DOCX, and TXT files. It extracts text from these documents for analysis.
- **Embeddings Generation**: Utilizes OpenAI's API to generate embeddings from the extracted text, enabling a deep understanding of the candidate's information.
- **Contextual Analysis**: Constructs a detailed context for the AI model to analyze, including the candidate's CV, recommendation letters, personal interests, and job description.
- **AI Responses**: Uses the Groq API to generate comprehensive and detailed responses to recruiters' questions.

## Contributing 🤝

We welcome contributions! Please fork the repository and submit a pull request.

1. **Fork the repository**
2. **Create a new branch**: `git checkout -b feature/your-feature-name`
3. **Commit your changes**: `git commit -m 'Add some feature'`
4. **Push to the branch**: `git push origin feature/your-feature-name`
5. **Open a pull request**

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📬

For any questions, feel free to open an issue or reach out directly to [jose.lgo.datascience@gmail.com](mailto:jose.lgo.datascience@gmail.com).

---

**PerfectCandidate** - Making recruitment smarter, one candidate at a time. 🚀

![PerfectCandidate](./img/bot.png)