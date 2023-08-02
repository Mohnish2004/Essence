import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from annotated_text import annotated_text
from streamlit_extras.app_logo import add_logo
from streamlit_extras.let_it_rain import rain

# Function to analyze token sentiment
def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(i)
        elif res < -0.1:
            neg_list.append(i)
        else:
            neu_list.append(i)
    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result

# Landing Page
def landing():
    st.title("Welcome to")
    st.image("/Users/mohnish/Downloads/TAGG.png", use_column_width=True)
    st.write(
        "Harness the power of natural language processing to analyze text sentiment, "
        "discover emotions, and gain insights from textual data. Whether you're exploring "
        "reviews, tweets, or any form of text, Essence is your go-to tool for understanding the essence behind the words."
    )
    st.button("Get Started")

# Analysis Page
def analysis():
    st.image("/Users/mohnish/Downloads/text.png", use_column_width=True)
    st.markdown(
        "Uncover the sentiment behind your text and gain valuable insights. "
        "Enter the text you want to analyze, and let Essence reveal the emotions within."
    )

    with st.form(key='nlpForm'):
        raw_text = st.text_area("Enter Text Here", height=200)
        submit_button = st.form_submit_button(label='Analyze')

    if submit_button:
        st.markdown("---")
        st.info("Sentiment Analysis Results")

        sentiment = TextBlob(raw_text).sentiment
        polarity = sentiment.polarity

        if polarity > 0.1:
            sentiment_label = "Positive 😀"
            sentiment_color = "#2ecc71"
        elif polarity < -0.1:
            sentiment_label = "Negative 😔"
            sentiment_color = "#e74c3c"
        else:
            sentiment_label = "Neutral 😐"
            sentiment_color = "#f39c12"

        annotated_text(sentiment_label)

        st.markdown("---")
        st.info("Entered Text with Sentiment Annotations")

        sentiment_annotations = []

        for word in raw_text.split():
            if TextBlob(word).sentiment.polarity > 0.1:
                sentiment_annotations.append((word, "", "#2ecc71"))
            elif TextBlob(word).sentiment.polarity < -0.1:
                sentiment_annotations.append((word, "", "#e74c3c"))
            else:
                sentiment_annotations.append((word, "", "#f39c12"))

        annotated_text(*sentiment_annotations)

        st.markdown("---")
        st.info("Token Sentiment Analysis")

        token_sentiments = analyze_token_sentiment(raw_text)
        st.write(token_sentiments)

        st.markdown("---")
        st.info("Word Cloud")

        if raw_text.strip():
            language = detect(raw_text)

            if language == 'en':
                wordcloud = WordCloud(width=600, height=400, background_color='black').generate(raw_text)
                plt.figure(figsize=(8, 6))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                st.pyplot(plt)
            else:
                st.warning("Word cloud is available only for English text.")
        else:
            st.warning("Enter some text to generate the word cloud.")

# About Page
def about():
    st.image("/Users/mohnish/Downloads/about.png", use_column_width=True)
    st.write(
        "Essence is an advanced sentiment analysis NLP app built with Streamlit. "
        "It provides insights into text sentiment, performs token-level sentiment analysis, and generates "
        "a word cloud for English text. Experience the power of natural language processing with Essence!"
    )
    st.markdown("### Code Sample")
    st.code("""
    import streamlit as st
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from annotated_text import annotated_text
from streamlit_extras.app_logo import add_logo
from streamlit_extras.let_it_rain import rain

# Function to analyze token sentiment
def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(i)
        elif res < -0.1:
            neg_list.append(i)
        else:
            neu_list.append(i)
    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result

# Analysis Page
def analysis():
    st.title("Text Sentiment Analysis")
    st.markdown(
        "Uncover the sentiment behind your text and gain valuable insights. "
        "Enter the text you want to analyze, and let Essence reveal the emotions within."
    )

    with st.form(key='nlpForm'):
        raw_text = st.text_area("Enter Text Here", height=200)
        submit_button = st.form_submit_button(label='Analyze')

    if submit_button:
        st.markdown("---")
        st.info("Sentiment Analysis Results")

        sentiment = TextBlob(raw_text).sentiment
        polarity = sentiment.polarity

        if polarity > 0.1:
            sentiment_label = "Positive 😀"
            sentiment_color = "#2ecc71"
            rain(emoji="🎈", font_size=54, falling_speed=5, animation_length="10")
        elif polarity < -0.1:
            sentiment_label = "Negative 😔"
            sentiment_color = "#e74c3c"
            rain(emoji="💩", font_size=54, falling_speed=5, animation_length="10")
        else:
            sentiment_label = "Neutral 😐"
            sentiment_color = "#f39c12"
            rain(emoji="❓", font_size=54, falling_speed=5, animation_length="10")

        annotated_text(sentiment_label)

        st.markdown("---")
        st.info("Entered Text with Sentiment Annotations")

        sentiment_annotations = []

        for word in raw_text.split():
            if TextBlob(word).sentiment.polarity > 0.1:
                sentiment_annotations.append((word, "", "#2ecc71"))
            elif TextBlob(word).sentiment.polarity < -0.1:
                sentiment_annotations.append((word, "", "#e74c3c"))
            else:
                sentiment_annotations.append((word, "", "#f39c12"))

        annotated_text(*sentiment_annotations)

        st.markdown("---")
        st.info("Token Sentiment Analysis")

        token_sentiments = analyze_token_sentiment(raw_text)
        st.write(token_sentiments)

        st.markdown("---")
        st.info("Word Cloud")

        if raw_text.strip():
            language = detect(raw_text)

            if language == 'en':
                wordcloud = WordCloud(width=600, height=400, background_color='black').generate(raw_text)
                plt.figure(figsize=(8, 6))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis("off")
                st.pyplot(plt)
            else:
                st.warning("Word cloud is available only for English text.")
        else:
            st.warning("Enter some text to generate the word cloud.")

    """)

def main():
    st.set_page_config(
        page_title="Essence - Sentiment Analysis App",
        page_icon=":bar_chart:",
        layout="wide"
    )
    st.sidebar.image("/Users/mohnish/Desktop/Title.png", use_column_width=True)

    menu = ["Home", "Analysis", "About"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Home":
        landing()
    elif choice == "Analysis":
        analysis()
    else:
        about()

if __name__ == '__main__':
    main()
