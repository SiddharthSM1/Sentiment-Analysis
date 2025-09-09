from textblob import TextBlob
text = input("Enter a sentence to analyze sentiment: ")

blob = TextBlob(text)

sentiment = blob.sentiment

print("\nSentiment Analysis Result:")
print(f"Polarity: {sentiment.polarity}")
print(f"Subjectivity: {sentiment.subjectivity}")
if sentiment.polarity > 0:
    print("The sentiment is Positive 😊")
elif sentiment.polarity < 0:
    print("The sentiment is Negative 😠")
else:
    print("The sentiment is Neutral 😐")