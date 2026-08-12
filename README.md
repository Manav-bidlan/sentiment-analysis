# 🎬 Movie Sentiment Analysis

A machine learning web application that analyzes the sentiment of movie reviews and classifies them as **Positive** or **Negative**.

The project uses **TF-IDF Vectorization + Logistic Regression** and is deployed as an interactive Streamlit application.

## 🚀 Live Demo

🔗 **Streamlit App:**  
[Add your deployed Streamlit URL here]

---

## 📌 Project Overview

Sentiment analysis is a Natural Language Processing (NLP) task used to determine the emotional tone of text.

In this project, I built an end-to-end sentiment classification system using the **IMDb Movie Reviews Dataset**.

The project covers:

- Data preprocessing
- Exploratory Data Analysis
- Bag of Words (BoW)
- TF-IDF Vectorization
- Logistic Regression
- Model comparison
- Model evaluation
- Confusion matrix analysis
- Error analysis
- Scikit-learn Pipeline
- Model serialization using Pickle
- Streamlit deployment

---

## 🧠 Approach

The complete workflow is:

```text
IMDb Reviews
     ↓
Data Cleaning & Preprocessing
     ↓
Train/Test Split
     ↓
┌─────────────────┬─────────────────┐
│   Bag of Words  │     TF-IDF      │
└────────┬────────┴────────┬────────┘
         ↓                 ↓
 Logistic Regression  Logistic Regression
         ↓                 ↓
     Evaluation        Evaluation
         └────────┬────────┘
                  ↓
          Select Best Model
                  ↓
      TF-IDF + Logistic Regression
                  ↓
               Pipeline
                  ↓
          Streamlit Application