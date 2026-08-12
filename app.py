import streamlit as st
import pickle

# -----------------------------
# Load trained model
# -----------------------------
with open("model/sentiment_pipeline.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="😊",
    layout="centered"
)


# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-top: 20px;
}

.sentiment {
    font-size: 38px;
    font-weight: 600;
}

.confidence {
    font-size: 32px;
    font-weight: 600;
}

.metric-label {
    font-size: 16px;
    color: #666;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🎬 Movie Sentiment Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze the sentiment of a movie review using Machine Learning</div>',
    unsafe_allow_html=True
)


# -----------------------------
# Input
# -----------------------------
review = st.text_area(
    "Enter your movie review",
    placeholder="Example: This movie was absolutely fantastic. I loved every minute of it.",
    height=180
)


# -----------------------------
# Analyze button
# -----------------------------
if st.button("🔍 Analyze Sentiment", use_container_width=True):

    if review.strip() == "":
        st.warning("Please enter a review first.")

    else:

        # Prediction
        prediction = model.predict([review])[0]

        # Probabilities
        probabilities = model.predict_proba([review])[0]

        # Get confidence
        confidence = max(probabilities) * 100

        # Determine sentiment
        if str(prediction) == 'positive':
            sentiment = "POSITIVE"
            emoji = "😊"
        else:
            sentiment = "NEGATIVE"
            emoji = "😞"


        # -----------------------------
        # Analysis Results
        # -----------------------------
        st.markdown("## Analysis Results")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                '<div class="metric-label">Predicted Sentiment</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="sentiment">{emoji} {sentiment}</div>',
                unsafe_allow_html=True
            )

            st.success(f"↑ {confidence:.2f}%")


        with col2:
            st.markdown(
                '<div class="metric-label">Confidence Score</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="confidence">{confidence:.2f}%</div>',
                unsafe_allow_html=True
            )


        # -----------------------------
        # Detailed Scores
        # -----------------------------
        st.markdown("## Detailed Scores")

        negative_confidence = probabilities[0] * 100
        positive_confidence = probabilities[1] * 100

        score_data = {
            "": ["😞", "😊"],
            "Sentiment": ["NEGATIVE", "POSITIVE"],
            "Confidence": [
                f"{negative_confidence:.2f}%",
                f"{positive_confidence:.2f}%"
            ]
        }

        st.table(score_data)


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

if st.button("🔄 Clear and analyze another text", use_container_width=True):
    st.rerun()