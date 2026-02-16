# OpenAI Quickstart Projects

A collection of OpenAI API quickstart projects demonstrating various capabilities including text generation, image analysis, and web search integration.

## Projects Overview

### 1. ST_App.py - Bedtime Story Generator (Streamlit)
A web application built with Streamlit that generates bedtime stories based on user-provided topics.

**Features:**
- Interactive web interface with Streamlit
- Generate one-paragraph bedtime stories on demand
- Real-time feedback with loading spinner
- Input validation and error handling

**Usage:**
```bash
streamlit run ST_App.py
```

Then open your browser and navigate to the provided URL (usually `http://localhost:8501`), enter a story topic, and click "Generate story".

---

### 2. UnicornText.py - Simple Story Generator
A minimal command-line script that generates a one-sentence bedtime story about a unicorn.

**Usage:**
```bash
python UnicornText.py
```

Perfect for quick testing of the OpenAI API integration.

---

### 3. TextFromImage.py - Image Analysis
Analyzes images using OpenAI's multimodal capabilities to extract information and answer questions about image content.

**Current Example:**
Analyzes a sports image to identify the teams and sport being played.

**Usage:**
```bash
python TextFromImage.py
```

You can modify the image URL and question in the script to analyze different images.

---

### 4. WebSrchTool.py - Web Search Integration
Demonstrates OpenAI's web search tool to fetch and summarize current information from the internet.

**Current Example:**
Searches for positive news stories from today.

**Usage:**
```bash
python WebSrchTool.py
```

---

## Installation

1. Clone or download this directory

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   Create a `.env` file in this directory with:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Requirements

- Python 3.8 or higher
- OpenAI API key (from https://platform.openai.com/api-keys)
- All dependencies listed in `requirements.txt`

Key packages:
- `openai` - OpenAI Python client
- `streamlit` - Web framework for ST_App.py
- `python-dotenv` - Environment variable management
- `requests` - HTTP library

## API Models Used

- **gpt-5** - Full GPT-5 model with advanced capabilities (image analysis, web search)
- **gpt-5-nano** - Lightweight GPT-5 model for simple text generation tasks

## Notes

- All scripts use the custom `responses.create()` API which appears to be a modified OpenAI client interface
- Ensure your OpenAI API key has appropriate permissions for all features used
- Some scripts may incur usage costs depending on your OpenAI plan
- The web search feature in WebSrchTool.py requires the OpenAI account to have web search enabled

## Troubleshooting

**"API key not found"**: Ensure your `.env` file exists in this directory with a valid `OPENAI_API_KEY`

**Streamlit connection errors**: Make sure you're running the streamlit command from the correct directory

**Image analysis errors**: Verify the image URL is accessible and the model supports image inputs

## File Structure

```
Quickstart/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this file)
├── ST_App.py             # Streamlit bedtime story web app
├── UnicornText.py        # Simple story generator script
├── TextFromImage.py      # Image analysis script
├── WebSrchTool.py        # Web search integration script
└── venv/                 # Virtual environment (optional)
```
