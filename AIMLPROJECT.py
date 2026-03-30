# ==============================
# Spam / Phishing Detection System (Upgraded)
# ==============================

# Import required libraries
import pandas as pd
import pickle
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# Step 1: Load Dataset (FIXED)
# -----------------------------
data = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only required columns
data = data[['v1', 'v2']]
data.columns = ['label', 'text']

# Remove missing values
data = data.dropna()

# -----------------------------
# Step 2: Convert Labels
# -----------------------------
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# -----------------------------
# Step 3: Split Data
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42
)

# -----------------------------
# Step 4: TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# -----------------------------
# Step 5: Train Model
# -----------------------------
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# -----------------------------
# Step 6: Evaluate Model
# -----------------------------
y_pred = model.predict(X_test_vec)

print("\nModel Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# -----------------------------
# Step 7: Helper Functions
# -----------------------------

# Get fraud probability
def get_fraud_probability(msg):
    msg_vec = vectorizer.transform([msg])
    prob = model.predict_proba(msg_vec)[0][1]
    return round(prob * 100, 2)


# Detect URLs (Phishing signal)
def detect_urls(msg):
    url_pattern = r'(https?://\S+|www\.\S+)'
    return re.findall(url_pattern, msg)


# Suspicious words (top spam indicators)
def highlight_suspicious_words(msg):
    words = msg.split()
    suspicious_words = []

    feature_names = vectorizer.get_feature_names_out()
    spam_probs = model.feature_log_prob_[1]

    # Top 50 spam-indicative words
    top_spam_words = set([
        feature_names[i]
        for i in spam_probs.argsort()[-50:]
    ])

    for word in words:
        if word.lower() in top_spam_words:
            suspicious_words.append(word)

    return suspicious_words


# Highlight text visually
def highlight_text(msg, suspicious_words, urls):
    for word in suspicious_words:
        msg = msg.replace(word, f"[{word.upper()}]")

    for url in urls:
        msg = msg.replace(url, f"[LINK:{url}]")

    return msg


# -----------------------------
# Step 8: Save Model
# -----------------------------
pickle.dump(model, open("spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))


# -----------------------------
# Step 9: User Testing
# -----------------------------
print("\n---- Test Your Own Message ---")

while True:
    msg = input("\nEnter message (or type 'exit' to stop): ")

    if msg.lower() == 'exit':
        print("Exiting...")
        break

    msg_vec = vectorizer.transform([msg])
    prediction = model.predict(msg_vec)[0]

    fraud_percent = get_fraud_probability(msg)
    suspicious = highlight_suspicious_words(msg)
    urls = detect_urls(msg)

    print("\nAnalysis Result:")

    if prediction == 1:
        print(f"Phishing / Spam Detected ({fraud_percent}%)")
    else:
        print(f"Safe Message ({fraud_percent}% risk)")

    if suspicious:
        print("Suspicious Words:", ", ".join(suspicious))

    if urls:
        print("Suspicious Links Detected:", ", ".join(urls))

    print("\nHighlighted Message:")
    print(highlight_text(msg, suspicious, urls))