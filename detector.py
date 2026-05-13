# A list of commonly used phishing trigger words
suspicious_keywords = ["urgent", "password", "bank", "invoice", "verify", "click", "crypto", "login"]

# A simulated incoming email message to analyze
email_content = "URGENT: Please login to your bank account immediately to verify yor secure password."

print("--- Running Automated Phishing Email Scan ---")

# Converts the email into lowercase and splits it into a list of individual words
email_words = email_content.lower().split(" ")

# Creates a variable to coun the number of dangerous words found
phishing_score = 0
found_keywords = []

# Loops through every word in the email
for word in email_words:
  # removes all punctuation from the word 
  clean_word = word.strip(".:,!?")

  # Loops through the backlist to see if a word matches one of the trigger words
  for keyword in suspicious_keywords:
    if clean_word == keyword:
      phishing_score += 1 

      if keyword not in found_keywords:
        found_keywords.append(keyword)

print(f"Total Suspicious Words Found: {phishing_score}")
print(f"Flagged Keywords: {found_keywords}")

# Risk Assessment Logic
if phishing_score >= 3:
  print("🚨 ALERT: High Risk! This email has been flagged as a PHISHING ATTEMPT.")
elif phishing_score >= 1:
  print("⚠️ WARNING: Moderate Risk. Exercise caution before clicking links.")
else:
  print("✅ SAFE: No common phishing indicators detected in this email.")
