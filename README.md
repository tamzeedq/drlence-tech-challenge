# Tech Challenge

This repository contains my submission for the Tech Challenge, featuring three applications. 

## Requirements

### System Requirements
- Node.js 20+ and npm
- Python 3.12+
- OpenAI API key (for LLM app)

### Python Dependencies
See individual `requirements.txt` files in each Python project folder.

## Project Structure

```
drlence-tech-challenge/
├── hello-world-react/    # Task 1
├── streamlit-app/        # Task 2 
├── llm-app/              # Task 3 (Bonus)
└── README.md
```

## Applications

### Task 1. Hello World React (`hello-world-react/`)

A simple React Hello World application built using the latest React guidelines and Vite.

**To run:**
```bash
cd hello-world-react
npm install
npm run dev
```

### Task 2. Streamlit ML App (`streamlit-app/`)

A Streamlit application that uses the existing YOLOv5 model to perform object detection on an image.

**Setup:**
```bash
cd streamlit-app
pip install -r requirements.txt
```

> Note: Install PyTorch according to your system specs from here [Download PyTorch](https://pytorch.org/get-started/locally/). For reference, I'm using CUDA 12.6.


**To run:**
```bash
streamlit run app.py
```
A test image of a cluttered desk is included under the `test-image` directory as a sample input.

### Task 3. LLM App (`llm-app/`)

An interactive Streamlit chatbot that is preloaded with my resume and is ready to talk about my qualifications for the position using OpenAI's GPT API.

**Setup:**
```bash
cd llm-app
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

**To run:**
```bash
streamlit run app.py
```

### Task 4. Document Vibe Coding
I didn't vibe code for the challenges, but I did use Claude to help with tasks 2 and 3. For task 2, it helped me with some issues I was having with PyTorch and setting up the YOLO model. For task 3, it helped me with rendering the sequence of messages for the chat.

