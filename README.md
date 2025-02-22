# Groq Chatbot with Streamlit

A web-based chatbot interface built with Streamlit that interacts with Groq's AI models. This application provides a user-friendly interface for having conversations with various Groq models.

## Features

- 💬 Interactive chat interface
- 🔄 Real-time responses from Groq AI models
- 🎛️ Adjustable AI parameters (temperature)
- 📝 Chat history maintenance
- 🔐 Secure API key handling
- 🤖 Multiple model support
- 🧹 Clear chat functionality

## Prerequisites

- Python 3.8 or higher
- Groq API key ([Get it here](https://console.groq.com))
- Internet connection

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd groq-chatbot
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. (Optional) Create a `.env` file in the project root and add your Groq API key:
```env
GROQ_API_KEY=your_api_key_here
```

2. If not using `.env`, you can input your API key directly in the Streamlit interface.

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. If you haven't set up the API key in `.env`, enter it in the sidebar

4. Select your preferred model and adjust the temperature as needed

5. Start chatting!

## Available Models

- `llama3-8b-8192`: Optimized for general conversation and tasks
- `gemma-7b-it`: Google's Gemma model for instruction-following tasks

## Application Structure

```
groq-chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (optional)
└── README.md          # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### Common Issues

1. **API Key Invalid**
   - Verify your API key is correct
   - Check if your API key has sufficient credits

2. **Connection Error**
   - Check your internet connection
   - Verify Groq API status at their status page

3. **Model Not Responding**
   - Try reducing the complexity of your prompt
   - Check if you've selected the correct model

## Security Notes

- Never commit your API key to version control
- Use environment variables or the Streamlit secrets management for API key storage
- Clear your chat history after sensitive conversations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/)

## Support

For issues and feature requests, please open an issue in the repository.
