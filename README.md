# 🎬 Sentiment Analysis

An end-to-end Natural Language Processing (NLP) project that classifies movie reviews as positive or negative using TF-IDF vectorization and Logistic Regression.

The project covers the complete machine learning workflow — from text preprocessing and feature extraction to model evaluation and deployment as an interactive Streamlit web application.

## 🚀 Live Demo

👉 "Try the Live Demo" https://sentiment-analysis-fswgshc8pqe4hegzajdzsb.streamlit.app/

Enter any movie review and the application predicts its sentiment along with a confidence score.

---

## 📌 Project Overview

Sentiment analysis is a Natural Language Processing task used to determine the emotional tone of text.

In this project, a Logistic Regression classifier is trained on the IMDb 50K Movie Reviews dataset to classify reviews into:

- 😊 Positive
- 😞 Negative

The final model uses TF-IDF (Term Frequency–Inverse Document Frequency) to convert text into numerical features before classification.

Final Result

Accuracy: 90.84%

---

## 🧠 Machine Learning Pipeline

IMDb Movie Reviews
        ↓
Data Cleaning & Preprocessing
        ↓
Train / Validation / Test Split
        ↓
Text Vectorization
        ↓
TF-IDF Features
        ↓
Logistic Regression
        ↓
Model Evaluation
        ↓
Streamlit Deployment

---

## 📊 Dataset

The project uses the IMDb 50K Movie Reviews dataset, containing:

- 50,000 movie reviews
- 25,000 training reviews
- 25,000 test reviews
- Two sentiment classes:
  - Positive
  - Negative

The dataset contains real movie reviews, making it a useful benchmark for binary sentiment classification.

---

## 🔧 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn
- Joblib
- Streamlit

---

## 📝 Text Preprocessing

Before training the model, the raw reviews are cleaned and prepared for machine learning.

The preprocessing pipeline includes:

- Removing HTML tags
- Converting text to lowercase
- Cleaning unnecessary characters
- Handling whitespace
- Preparing text for vectorization

The goal is to reduce irrelevant information while preserving useful sentiment-related information.

---

## 🔤 Feature Engineering

Two different text representation approaches were explored:

### 1. Bag of Words (BoW)

The Bag of Words approach represents text based on word occurrence frequencies.

### 2. TF-IDF

TF-IDF assigns higher importance to words that are informative for a document while reducing the influence of words that appear frequently across many documents.

The final model uses TF-IDF because it provided better performance for this task.

---

## 🤖 Model

### Logistic Regression

Logistic Regression was selected as the final classification algorithm because it works well for high-dimensional sparse text features and provides a strong baseline for binary text classification.

The model learns the relationship between TF-IDF features and the sentiment labels.

### Final Model

Vectorizer: TF-IDF
Classifier: Logistic Regression
Dataset: IMDb 50K
Accuracy: 90.84%

---

## 📈 Model Evaluation

The model was evaluated using multiple classification metrics rather than relying only on accuracy.

Evaluation included:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

These metrics provide a better understanding of how well the model performs on both positive and negative reviews.

---

## 🔍 Error Analysis

Error analysis was performed to understand cases where the model made incorrect predictions.

Some challenging examples include reviews containing:

- Mixed positive and negative opinions
- Sarcasm
- Negation
- Ambiguous language
- Context-dependent sentiment

For example, a review can contain many positive words while expressing an overall negative opinion. Traditional TF-IDF-based models can struggle with this type of contextual meaning.

---

## 🌐 Streamlit Web Application

The trained model was deployed using Streamlit to create an interactive sentiment analysis application.

Users can:

1. Enter a movie review.
2. Click Analyze Sentiment.
3. View the predicted sentiment.
4. View the model's confidence score.
5. View detailed sentiment probabilities.

Example

Input:
"This movie was absolutely fantastic. I loved every minute of it."

Prediction:
POSITIVE

Confidence:
70.39%

---

## 📂 Project Structure

```text
sentiment-analysis/
│   
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── models/
│   └── sentiment_pipeline.pkl 
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
«File names may differ depending on the final project structure.»

---

## ⚙️ Installation

Clone the repository:

git clone https://github.com/Manav-bidlan/sentiment-analysis
cd sentiment-analysis

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

---

## ▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your browser.

---

## 📦 Model Files

The trained model and TF-IDF vectorizer are saved separately so that the Streamlit application can load them directly without retraining the model every time.

model.pkl
vectorizer.pkl

---

## 💡 Key Learnings

Through this project, I worked with:

- Natural Language Processing
- Text preprocessing
- Feature engineering
- Bag of Words
- TF-IDF
- Logistic Regression
- Model evaluation
- Error analysis
- Model serialization
- Streamlit deployment
- End-to-end ML project development

---

## 🔮 Future Improvements

Possible improvements include:

- Experimenting with Linear SVM
- Using n-grams more extensively
- Hyperparameter tuning
- Improving text preprocessing
- Trying word embeddings
- Experimenting with transformer-based models such as BERT
- Adding more detailed prediction explanations
- Improving the UI and user experience

---

## 👨‍💻 Author

Manav Bidlan

B.Tech CSE Student | Machine Learning Developer

Interested in Machine Learning, NLP, and building practical AI applications.

---
