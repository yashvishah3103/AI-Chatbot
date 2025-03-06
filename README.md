
#AI Chatbot with Streamlit & OpenAI

An interactive AI-powered chatbot built using Streamlit, LangChain, and OpenAI. The chatbot supports real-time streaming responses and maintains chat history for a seamless user experience.

🚀 Features

Real-time Streaming: AI-generated responses appear dynamically without refreshing the UI.

Chat History: Previous messages are saved for a continuous conversation flow.

Styled UI: Custom CSS enhances the chatbot interface.

OpenAI API Integration: Uses OpenAI's GPT models for intelligent responses.

Efficient Prompt Handling: LangChain-based prompt templates optimize response generation.

🛠️ Installation & Setup

Prerequisites

Make sure you have Python 3.8+ installed on your system.

1️⃣ Clone the Repository

git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Environment Variables

Create a .env file in the project directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

4️⃣ Run the Application

streamlit run app.py

🖥️ Usage

Open the Streamlit UI in your browser.

Type your message in the input field and press Send.

The chatbot will generate a streaming response inside the same chat bubble.

📂 Project Structure

├── app.py              # Main application script
├── style.css           # Custom CSS for UI styling
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API Key)
└── README.md           # Project documentation

🎨 Customization

Modify style.css to change the chatbot’s appearance.

Adjust PromptTemplate in app.py to fine-tune the chatbot’s responses.

🤝 Contributing

Pull requests are welcome! If you find any issues, feel free to open an Issue.

