# 📨 Automated Phishing Email Detector 

## What it does
This Python script acts as an email gateway security filter. It takes the incoming email and compares every word to a list of commonly used phishing words to detect likely phishing emails.

## Computer Science Concepts Applied
* **String Sanitization**: Utilizing '.lower()' and '.strip()' to prevent punctuation from breaking key matching and change all letter cases accordingly.
* **Nested Loop Structures**: Implementing an outer loop to iterate through text inputs and an inner loop to evaluate data against a security blacklist.
* **Algorithmic Scoring**: Developing a threshold-based risk matrix to determine system output based on variable accumulation.
