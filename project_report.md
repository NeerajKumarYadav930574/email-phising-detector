#  Project Report  
## Spam / Phishing Detection System Using Machine Learning

---

## 1.  Introduction

With the rapid growth of digital communication, spam and phishing messages have become a major cybersecurity threat. These malicious messages aim to deceive users into revealing sensitive information such as passwords, bank details, or personal data.

This project presents a **machine learning-based Spam/Phishing Detection System** that classifies messages as *spam* or *safe (ham)*. It also enhances interpretability by highlighting suspicious words and detecting potentially harmful links.

---

## 2.  Objectives

- To build a system that can classify messages as spam or non-spam  
- To detect phishing indicators such as suspicious URLs  
- To provide a probability score indicating the likelihood of fraud  
- To highlight suspicious words within messages  
- To enable real-time user message testing  

---

## 3.  Technologies Used

- **Programming Language:** Python  
- **Libraries:**
  - pandas (data handling)
  - scikit-learn (machine learning)
  - re (regular expressions)
  - pickle (model persistence)

---

## 4.  Dataset Description

- Dataset: `spam.csv`
- Columns:
  - `v1`: Label (ham/spam)
  - `v2`: Message text

### Data Preprocessing

- Removed unnecessary columns  
- Renamed columns to `label` and `text`  
- Converted labels:
  - ham → 0 (safe)
  - spam → 1 (malicious)  
- Removed missing values  

---

## 5.  Methodology

### 5.1 Data Splitting

- Training Set: 80%  
- Testing Set: 20%  

### 5.2 Text Vectorization

- TF-IDF (Term Frequency–Inverse Document Frequency)  
- N-grams used: Unigrams + Bigrams (`ngram_range=(1,2)`)  
- Removed English stopwords  

### 5.3 Model Training

- Algorithm: **Multinomial Naive Bayes**  
- Suitable for text classification tasks  

### 5.4 Model Evaluation

- Accuracy Score  
- Confusion Matrix  
- Classification Report (Precision, Recall, F1-score)  

---

## 6.  System Features

### 6.1 Spam Detection
- Classifies messages as:
  - Spam / Phishing
  - Safe Message  

### 6.2 Fraud Probability
- Displays likelihood of spam in percentage  

### 6.3 URL Detection
- Detects suspicious links using regex  

### 6.4 Suspicious Word Highlighting
- Identifies high-risk words based on trained model  
- Highlights them in uppercase  

### 6.5 Interactive Testing
- Users can input custom messages  
- Real-time classification output  

---

## 7.  Results

- Achieved high accuracy (~95–98%) depending on dataset split  
- Successfully detects:
  - Promotional spam  
  - Fraudulent messages  
  - Suspicious links  

### Example Output

- **Spam Detected (92.5%)**  
- Suspicious Words: free, win, offer  
- Detected Links: http://example.com  

---

## 8.  Model Deployment

- Model saved as:
  - `spam_model.pkl`  
  - `vectorizer.pkl`  

- Enables reuse without retraining  

---

## 11.  Conclusion

This project demonstrates an effective approach to spam and phishing detection using machine learning. By combining classification with explainability features like suspicious word highlighting and URL detection, the system becomes both accurate and user-friendly.

It provides a strong foundation for advanced cybersecurity applications.

---

## 12.  References

1. Scikit-learn Documentation  
2. Python Documentation  
3. UCI Machine Learning Repository (SMS Spam Dataset)  
4. Research papers on spam detection  

---

##  Author

- **Project Title:** Spam / Phishing Detection System  
- **Developed By:** NEERAJ KUMAR 

---