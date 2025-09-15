import re

#I. Extract all email addresses
text = "Contact us at support@example.com or admin@domain.org"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print("Emails:", emails)

# II. Validate a date (YYYY-MM-DDi
date = "2025-09-15"
if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
    print("Valid date format")
else:
    print("Invalid date format")

# III. Replace all occurrences of a word
sentence = "I love Python. Python is great!"
new_sentence = re.sub(r"Python", "Java", sentence)
print("Replaced sentence:", new_sentence)

# IV. Split string by non-alphanumeric characters
string = "Hello, world! Python_3.9 is cool."
parts = re.split(r"\W+", string)
print("Split parts:", parts)