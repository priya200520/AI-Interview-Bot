# 🤖 AI Interview Bot

An AI-powered technical interview practice application built using Python, Streamlit, LangChain, and Google Gemini.

The application helps users practice technical interviews by generating questions, evaluating answers, tracking performance, and providing an AI-generated final performance report.

---

## 🚀 Features

- 🎯 Choose interview topics
- 📊 Select difficulty level: Easy, Medium, Hard
- 🔢 Choose interview length: 5, 10, or 15 questions
- 🤖 AI-generated technical interview questions
- 📝 Submit answers and receive AI evaluation
- ⭐ Automatic score calculation
- 📈 Overall performance tracking
- 📚 Interview history
- 📊 Score performance chart
- 🏆 Final interview report
- 🤖 AI-powered strengths and improvement analysis
- 📄 Download final interview report as PDF
- 🔄 Reset interview functionality

---

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini AI
- LangChain Google GenAI
- Pandas
- Matplotlib
- ReportLab
- Python Dotenv

---

## 📂 Project Structure

```text
AI_Interview_Bot/
│
├── app.py
├── utils.py
├── pdf_report.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Navigate to the project folder

```bash
cd AI_Interview_Bot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project folder and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

⚠️ Never upload your `.env` file or API key to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 How It Works

```text
Select Topic + Difficulty
            ↓
Generate AI Question
            ↓
Submit Your Answer
            ↓
AI Evaluation + Score
            ↓
Next Question
            ↓
Interview Completion
            ↓
Performance Chart
            ↓
AI Final Analysis
            ↓
Download PDF Report
```

---

## 🎯 Supported Topics

- Python
- SQL
- DBMS
- DSA
- OOPs
- Web Development

---

## 👩‍💻 Author

**Priya**  
B.Tech Computer Science Engineering

---

⭐ If you like this project, consider giving it a star!