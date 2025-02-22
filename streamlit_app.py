import streamlit as st
import requests
import json

# Pre-configured API key
GROQ_API_KEY = "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"

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Initialize session state for user input
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""

# Page configuration
st.set_page_config(
    page_title="TrafficWise Urban Planner",
    page_icon="🚦",
    layout="wide"
)

# Sidebar configuration
st.sidebar.title("🚦 TrafficWise Urban Planner")
st.sidebar.markdown("Your AI Assistant for Traffic & Urban Planning")

# Temperature slider
temperature = st.sidebar.slider(
    "AI Response Variation:",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1,
    help="Higher values provide more varied suggestions, lower values offer more consistent advice"
)

# Main chat interface
st.title("🚦 TrafficWise Urban Planner")
st.markdown("""
### Your AI Assistant for:
- 🚗 Traffic Route Optimization
- 🌆 Urban Congestion Solutions
- 🚦 Traffic Flow Analysis
- 🛣️ Infrastructure Planning
""")

def chat_with_traffic_planner(user_message, temperature):
    """Send a message to Groq API's model and return the response."""
    # Enhance the prompt with traffic and urban planning context
    enhanced_prompt = f"""As a traffic and urban planning expert, help with the following question 
    about traffic routes, urban congestion, or city planning: {user_message}
    
    Consider factors like:
    - Traffic flow patterns
    - Peak hours and congestion points
    - Public transportation integration
    - Environmental impact
    - Safety considerations
    """
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": enhanced_prompt}],
        "temperature": temperature
    }
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"Error: Unable to connect to the API - {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"

def clear_chat():
    st.session_state.chat_history = []

# Display chat history with improved styling
for message in st.session_state.chat_history:
    role = message["role"]
    content = message["content"]
    
    if role == "user":
        st.markdown(f"**👤 You:** {content}")
    else:
        st.markdown(f"**🚦 TrafficWise:** {content}")
    st.markdown("---")

# Chat input area with callback
def submit_message():
    if st.session_state.user_input:
        user_message = st.session_state.user_input
        
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        
        # Show a spinner while waiting for the response
        with st.spinner('Analyzing traffic patterns...'):
            # Get bot response
            bot_response = chat_with_traffic_planner(user_message, temperature)
        
        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
        
        # Clear the input
        st.session_state.user_input = ""

# Create the text input
st.text_input(
    "Ask about traffic routes, urban planning, or congestion solutions...",
    key="user_input",
    on_change=submit_message,
    placeholder="Example: What are the best routes to reduce congestion during peak hours?"
)

# Clear chat button
if st.button("🗑️ Clear Chat"):
    clear_chat()

# Footer
st.markdown("---")
st.markdown("Powered by TrafficWise Urban Planning AI 🚦")

# Add traffic-specific information in the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 🚗 Traffic Guidelines:
1. 🕒 **Peak Hours**
   - Morning: 7-9 AM
   - Evening: 4-7 PM
   - Plan routes accordingly

2. 🚸 **Safety First**
   - Follow speed limits
   - Watch for pedestrians
   - Maintain safe distance

3. 🌍 **Eco-Friendly Options**
   - Consider public transport
   - Use carpooling
   - Check bike lanes

4. 🚦 **Smart Route Planning**
   - Check traffic updates
   - Use alternative routes
   - Avoid construction zones

5. 📱 **Stay Informed**
   - Monitor traffic alerts
   - Check weather conditions
   - Follow road closures
""")

# Additional resources
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📚 Useful Resources:
- 🚗 Local Traffic Laws
- 🗺️ City Planning Guidelines
- 🚌 Public Transport Schedules
- 🚧 Construction Updates
""")
