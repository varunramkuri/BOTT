import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("No GEMINI_API_KEY found in environment variables")
genai.configure(api_key=API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# Set up the model with system instructions
system_instruction = (
    "You are a helpful and intelligent AI assistant powered by Gemini. "
    "Your tone is professional yet friendly. "
    "Always use markdown for formatting when appropriate: "
    "use bold for emphasis, lists for multiple points, and code blocks with language identifiers for any code snippets. "
    "Keep responses concise and well-structured."
)

model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    generation_config=generation_config,
    system_instruction=system_instruction
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({"error": "No message provided"}), 400
    
    user_message = data.get('message')
    
    try:
        response = model.generate_content(user_message)
        if response.text:
            return jsonify({"response": response.text})
        else:
            return jsonify({"error": "Model returned an empty response"}), 500
    except Exception as e:
        print(f"Error calling Gemini API: {str(e)}")
        return jsonify({"error": "Failed to get response from AI"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
