# Gemini AI Chatbot Documentation

## 1. Project Overview
This is a modern, feature-rich AI chatbot application built with **Flask (Python)** and **Google's Gemini API**. It features a premium user interface with Glassmorphism design, dark mode support, and rich text rendering capabilities (Markdown & Code Syntax Highlighting).

## 2. Key Features

### 🎨 User Interface (UI) / User Experience (UX)
- **Premium Design**: Clean, modern aesthetics using Google's color palette (Blue, Red, Yellow, Green) and glassmorphism effects.
- **Responsive Layout**: Fully responsive design that works seamlessly on desktop and mobile devices.
- **Smooth Animations**: Entrance animations for messages, welcome screen, and hover effects for a polished feel.
- **Dark Mode**: Built-in dark/light mode toggle that persists user preference using LocalStorage.

### 🛠️ Functionality
- **Generative AI**: Powered by Google's `gemini-flash-latest` model for fast and intelligent responses.
- **Rich Text Support**:
    - **Markdown Rendering**: Bold, italics, lists, and headers are rendered beautifully using `marked.js`.
    - **Code Highlighting**: Code blocks are automatically detected and highlighted using `highlight.js` (GitHub Dark theme).
- **History**: Conversation history is preserved within the current session.
- **Loading Indicators**: Visual feedback ("typing dots") while waiting for the AI response.

## 3. Project Structure

```text
d:/CHATBOT/
├── app.py                 # Main Flask application and API backend
├── .env                   # Environment variables (API Key)
├── requirements.txt       # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet (Variables, Dark Mode, Animations)
│   └── js/
│       └── script.js      # Frontend logic (Fetch API, Markdown, Theme Toggle)
└── templates/
    └── index.html         # Main HTML structure
```

## 4. Setup & Installation

### Prerequisites
- Python 3.8+ installed.
- A Google Cloud Project with the Gemini API enabled.
- An API Key from [Google AI Studio](https://aistudio.google.com/).

### Installation Steps

1.  **Clone/Open the Project**:
    Navigate to the project directory:
    ```bash
    cd d:/CHATBOT
    ```

2.  **Install Dependencies**:
    Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    *Dependencies found in `requirements.txt`: `flask`, `google-generativeai`, `python-dotenv`.*

3.  **Configure Environment**:
    Create a `.env` file in the root directory and add your API key:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    ```

4.  **Run the Application**:
    Start the Flask server:
    ```bash
    python app.py
    ```

### Accessing the App
Open your web browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## 5. Usage Guide

1.  **Start a Chat**: Type your message in the input box at the bottom and press **Enter** or click the **Send** button.
2.  **Toggle Theme**: Click the **Sun/Moon icon** in the top-right corner to switch between Light and Dark modes.
3.  **Code Examples**: Ask for code (e.g., "Write a Python script to scrape a website"). The response will display properly formatted and highlighted code blocks.
4.  **Clear Chat**: Refresh the page to start a new conversation session.

## 6. Technical Configuration

### Backend (`app.py`)
- **Model**: Currently configured to use `gemini-flash-latest` (Gemini 1.5 Flash).
- **System Instructions**: The model is instructed to be professional, friendly, and use markdown for formatting.
- **Error Handling**: Captures API errors (like quota limits) and returns friendly error messages to the frontend.

### Frontend (`index.html`, `style.css`, `script.js`)
- **Libraries**:
    - `marked.js` (CDN): For Markdown parsing.
    - `highlight.js` (CDN): For syntax highlighting.
    - Google Fonts: `Google Sans`, `Roboto`, `JetBrains Mono`.
- **Theme Logic**: Uses a `.dark-mode` class on the `<body>` tag and saves the state to `localStorage`.

## 7. Troubleshooting

**Issue: "Verification failed" or "Quota Exceeded"**
- **Cause**: The free tier of the Gemini API has rate limits (RPM/RPD). Experimental models (like `gemini-2.0-flash`) often have lower limits.
- **Solution**: The app is configured to use `gemini-flash-latest` which is stable. If you still hit limits, wait a minute before sending more requests.

**Issue: Browser won't open**
- **Cause**: Local environment issues.
- **Solution**: Open your preferred browser (Chrome, Edge, Firefox) manually and type `http://127.0.0.1:5000`.

**Issue: "Failed to connect to server"**
- **Cause**: The Flask server is not running.
- **Solution**: Check your terminal. If the server stopped, run `python app.py` again.
