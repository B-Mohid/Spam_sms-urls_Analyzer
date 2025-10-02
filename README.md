Client-Side Spam Classifier AI
This is a production-ready, client-side web application that uses two pre-trained TensorFlow.js models to classify SMS messages and URLs as spam or not spam. The entire analysis happens within the user's browser, ensuring privacy and speed.

The application is served by a lightweight Streamlit wrapper, making it easy to deploy on the Streamlit Community Cloud for free.

Features
Dual Model System: Utilizes specialized models for both SMS and URL classification.

100% Client-Side: No user data is sent to a server for analysis. All predictions are performed in-browser using TensorFlow.js.

Futuristic UI/UX: A sleek, responsive, and modern interface built with Tailwind CSS.

Optimized Loading: Models and assets are loaded asynchronously with clear loading state indicators.

Easy Deployment: Architected for simple, one-click deployment on Streamlit Community Cloud.

Project Structure
.
├── .gitignore
├── README.md
├── app.py                 # Streamlit server
├── requirements.txt       # Python dependencies
├── models/                # <-- PLACE YOUR 6 MODEL FILES HERE
│   ├── sms_model.json
│   ├── sms_model.bin
│   ├── sms_word_index.json
│   ├── url_model.json
│   ├── url_model.bin
│   └── url_char_index.json
└── static/
    └── index.html         # Main web application

Setup & Local Development
Prerequisites:

Python 3.8+

pip package manager

Instructions:

Clone the repository:

git clone <https://github.com/B-Mohid/Spam_sms-urls_Analyzer>
cd <Spam_sms&urls_Analyzer>

Create and activate a virtual environment (recommended):

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Place your models: Ensure your six model files (sms_model.json, sms_model.bin, etc.) are placed inside the models/ directory.

Run the application:

streamlit run app.py

Your application will be available at http://localhost:8501.

Deployment to Streamlit Community Cloud
Push your code to a GitHub repository. Make sure it's a public repository.

Sign up or log in to Streamlit Community Cloud.

Click "New app" and connect your GitHub account.

Select your repository and the branch (usually main).

Ensure the "Main file path" is set to app.py and click "Deploy!".

Streamlit will handle the rest, and your web application will be live in minutes.

Built with professional-grade UI/UX design and robust, error-handled code.

